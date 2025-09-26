"""背压与饱和行为测试

验证当 Redis 发送持续失败、且内存队列容量较小时，队列会在约定容量处饱和，
从而表现为“写到约 300 多条后就不再继续”的现象（生产端继续投递但后台消费无法推进）。
"""

import datetime
import threading
import time
from types import SimpleNamespace

from plumelog_loguru import PlumelogSettings
from plumelog_loguru.redis_sink import RedisSink


def _build_message(content: str) -> SimpleNamespace:
    """构造与 Loguru Record 接口兼容的简易对象"""
    level = SimpleNamespace(name="INFO")
    return SimpleNamespace(
        record={
            "message": content,
            "level": level,
            "time": datetime.datetime.now(),
        }
    )


class FailingAsyncRedisClient:
    """始终发送失败的 Redis 客户端替身

    用于触发 RedisSink 的失败重排队逻辑，促使队列在写入压力下达到饱和。
    设置 retry_count=1 可以避免指数退避造成的长时间等待。
    """

    def __init__(self, config) -> None:  # noqa: D401
        self.config = config
        self.calls = 0

    async def send_log_records(self, records, key=None) -> bool:  # noqa: D401
        self.calls += 1
        return False  # 始终失败，触发重新入队

    async def disconnect(self) -> None:  # noqa: D401
        return None


def test_queue_saturates_when_redis_send_fails(monkeypatch):
    """当发送失败且队列容量较小时，队列应在容量上限处饱和并保持满载"""

    # 使用发送失败的客户端替身
    monkeypatch.setattr(
        "plumelog_loguru.redis_sink.AsyncRedisClient", FailingAsyncRedisClient
    )

    # 将队列容量设置为 300，批量/间隔较小以加速循环；retry_count=1 避免指数退避
    cfg = PlumelogSettings(
        app_name="bp_test",
        env="test",
        batch_size=50,
        batch_interval_seconds=0.05,
        queue_max_size=300,
        retry_count=1,
    )

    sink = RedisSink(cfg)

    # 高速生产日志，远超队列容量
    def producer(total: int) -> None:
        for i in range(total):
            sink(_build_message(f"log-{i}"))  # type: ignore[arg-type]

    t = threading.Thread(target=producer, args=(1000,))
    t.start()

    # 等待队列初始化并逐步填满，最多等待 5 秒
    deadline = time.time() + 5
    while time.time() < deadline:
        q = sink._log_queue  # type: ignore[attr-defined]
        if q is not None and q.qsize() >= cfg.queue_max_size:
            break
        time.sleep(0.01)

    t.join(timeout=2)

    # 断言：队列已达到上限（或接近上限，考虑异步时序），并在短时间内保持不下降
    assert sink._log_queue is not None  # type: ignore[attr-defined]
    qsize1 = sink._log_queue.qsize()  # type: ignore[union-attr]
    assert qsize1 >= int(cfg.queue_max_size * 0.95)

    time.sleep(0.5)
    qsize2 = sink._log_queue.qsize()  # type: ignore[union-attr]
    # 仍应维持在较高水位（>= 80% 容量），体现饱和/背压状态
    assert qsize2 >= int(cfg.queue_max_size * 0.8)

    # 不调用 sink.close() 以避免在失败重排队场景下阻塞 join；
    # 背景线程为 daemon，不会阻塞测试进程退出。
