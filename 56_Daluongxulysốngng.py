from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random


def xu_ly_tac_vu(id_tac_vu: int) -> str:
    """Hàm giả lập tác vụ tốn thời gian I/O"""
    thoi_gian = random.uniform(0.5, 1.5)
    time.sleep(thoi_gian)
    return f"Tác vụ #{id_tac_vu} hoàn thành sau {thoi_gian:.2f}s"


def main():
    print("--- DEMO THREAD POOL EXECUTOR (MULTITHREADING) ---")
    start_time = time.perf_counter()

    so_tac_vu = 6
    max_threads = 3  # Chỉ cho phép tối đa 3 Thread chạy đồng thời

    print(
        f"Bắt đầu thực thi {so_tac_vu} tác vụ với Thread Pool ({max_threads} worker threads)...\n"
    )

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Submit tất cả công việc vào Pool
        futures = [executor.submit(xu_ly_tac_vu, i) for i in range(1, so_tac_vu + 1)]

        # Lấy kết quả ngay khi có bất kỳ Thread nào hoàn thành trước
        for future in as_completed(futures):
            res = future.result()
            print(f" -> [Kết quả] {res}")

    total_time = time.perf_counter() - start_time
    print(f"\n✅ Hoàn thành toàn bộ trong: {total_time:.2f} giây!")


if __name__ == "__main__":
    main()
