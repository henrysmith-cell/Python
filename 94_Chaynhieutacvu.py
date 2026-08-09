import asyncio
import time


async def crawl_api(domain: str, delay: int):
    """Giả lập hàm tải dữ liệu từ API tốn thời gian"""
    print(f" 🔄 [Bắt đầu] Đang cày dữ liệu từ: {domain} (Mất {delay}s)...")
    await asyncio.sleep(delay)  # Tác vụ I/O không chặn (non-blocking)
    print(f" ✅ [Hoàn thành] Đã lấy xong dữ liệu từ: {domain}")
    return f"Data từ {domain}"


async def main():
    print("--- DEMO ASYNCIO.GATHER XỬ LÝ BẤT ĐỒNG BỘ ---")
    start_time = time.perf_counter()

    # Chạy đồng thời 3 Task API khác nhau
    ket_qua = await asyncio.gather(
        crawl_api("api.server1.com", 2),
        crawl_api("api.server2.com", 3),
        crawl_api("api.server3.com", 1),
    )

    end_time = time.perf_counter()
    print("\nKết quả thu thập được:")
    for res in ket_qua:
        print(f" - {res}")

    print(f"\n⏱️  Tổng thời gian chạy thực tế: {end_time - start_time:.2f} giây")
    print("👉 (Thay vì mất 2 + 3 + 1 = 6s nếu chạy tuần tự!)")


if __name__ == "__main__":
    # Chạy Event Loop của Asyncio
    asyncio.run(main())
