"""
测试日志系统修复效果
"""
import asyncio
import threading
import time
from loguru import logger
from plumelog_loguru import PlumelogSettings, create_redis_sink, OverflowStrategy


def test_high_volume_logging():
    """测试高并发日志场景"""
    print("\n" + "="*60)
    print("测试高并发日志场景")
    print("="*60)

    # 配置：小队列 + 缓冲策略
    config = PlumelogSettings(
        app_name="test_app",
        env="test",
        queue_max_size=100,  # 故意设置小队列测试溢出
        batch_size=10,
        batch_interval_seconds=1.0,
        temp_buffer_max_size=5000,
        overflow_strategy=OverflowStrategy.BUFFER,  # 使用缓冲策略
        redis_host="localhost",
        redis_port=6379
    )

    sink = create_redis_sink(config)
    logger.add(sink, format="{message}")

    print(f"配置信息：")
    print(f"  队列大小: {config.queue_max_size}")
    print(f"  缓冲区大小: {config.temp_buffer_max_size}")
    print(f"  溢出策略: {config.overflow_strategy}")
    print(f"  批处理大小: {config.batch_size}")

    # 生产大量日志的函数
    def produce_logs(thread_id: int, count: int):
        """在单个线程中生产日志"""
        for i in range(count):
            logger.info(f"[Thread-{thread_id}] Log message {i+1}/{count}")
            if i % 100 == 0:
                print(f"  Thread-{thread_id}: 已生产 {i+1} 条日志")

    # 创建多个线程并发生产日志
    threads = []
    thread_count = 3
    logs_per_thread = 200

    print(f"\n启动 {thread_count} 个线程，每个线程生产 {logs_per_thread} 条日志...")
    start_time = time.time()

    for i in range(thread_count):
        thread = threading.Thread(target=produce_logs, args=(i+1, logs_per_thread))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    end_time = time.time()
    total_logs = thread_count * logs_per_thread
    duration = end_time - start_time

    print(f"\n日志生产完成:")
    print(f"  总日志数: {total_logs}")
    print(f"  耗时: {duration:.2f} 秒")
    print(f"  速率: {total_logs/duration:.0f} 条/秒")

    # 给一些时间让日志发送到 Redis
    print("\n等待日志发送到 Redis...")
    time.sleep(5)

    # 清理
    logger.remove()

    # 异步关闭 sink
    async def close_sink():
        await sink.close()

    asyncio.run(close_sink())

    print("\n测试完成！系统没有被卡住 ✅")


def test_overflow_strategies():
    """测试不同的溢出策略"""
    print("\n" + "="*60)
    print("测试不同溢出策略")
    print("="*60)

    strategies = [
        OverflowStrategy.DROP_NEW,
        OverflowStrategy.DROP_OLD,
        OverflowStrategy.BUFFER
    ]

    for strategy in strategies:
        print(f"\n测试策略: {strategy}")
        print("-" * 40)

        config = PlumelogSettings(
            app_name="test_app",
            env="test",
            queue_max_size=50,  # 非常小的队列
            batch_size=5,
            batch_interval_seconds=0.5,
            temp_buffer_max_size=100,
            overflow_strategy=strategy,
            redis_host="localhost",
            redis_port=6379
        )

        sink = create_redis_sink(config)
        logger.add(sink, format="{message}")

        # 快速生产日志
        for i in range(100):
            logger.info(f"[{strategy}] Message {i+1}")

        # 等待处理
        time.sleep(2)

        # 清理
        logger.remove()

        async def close_sink():
            await sink.close()

        asyncio.run(close_sink())

        print(f"  策略 {strategy} 测试完成 ✅")


if __name__ == "__main__":
    print("\n" + "🚀" * 30)
    print("开始测试日志系统修复效果")
    print("🚀" * 30)

    # 运行测试
    try:
        test_high_volume_logging()
        test_overflow_strategies()

        print("\n" + "✨" * 30)
        print("所有测试完成！日志系统正常工作，没有卡死现象")
        print("✨" * 30)
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        raise