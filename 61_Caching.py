from functools import lru_cache
import time


# Không có cache: Tính toán đệ quy thuần túy (Cực kỳ chậm)
def fibonacci_thuong(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_thuong(n - 1) + fibonacci_thuong(n - 2)


# Có cache: Tự động lưu nhớ kết quả đã tính
@lru_cache(maxsize=None)
def fibonacci_cache(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


def main():
    print("--- DEMO TỐI ƯU TỐC ĐỘ VỚI LRU CACHE ---")
    n = 35

    # 1. Đo thời gian không dùng cache
    start = time.perf_counter()
    res1 = fibonacci_thuong(n)
    time1 = time.perf_counter() - start
    print(f"Không Cache : F({n}) = {res1} | Thời gian: {time1:.4f} giây")

    # 2. Đo thời gian có dùng cache
    start = time.perf_counter()
    res2 = fibonacci_cache(n)
    time2 = time.perf_counter() - start
    print(f"Có LRU Cache: F({n}) = {res2} | Thời gian: {time2:.6f} giây")

    print(f"\n⚡ Tốc độ tăng gấp hơn {int(time1 / time2):,} lần!")


if __name__ == "__main__":
    main()
