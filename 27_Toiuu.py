import time
import functools


def tinh_fibo_thuong(n):
    """Tính Fibonacci đệ quy thông thường - Không có Cache (Cực chậm khi n lớn)"""
    if n <= 1:
        return n
    return tinh_fibo_thuong(n - 1) + tinh_fibo_thuong(n - 2)


@functools.lru_cache(maxsize=128)  # Tự động lưu tối đa 128 kết quả gần nhất vào RAM
def tinh_fibo_co_cache(n):
    """Tính Fibonacci đệ quy có Caching - Siêu nhanh!"""
    if n <= 1:
        return n
    return tinh_fibo_co_cache(n - 1) + tinh_fibo_co_cache(n - 2)


def main():
    N = 35
    print(f"--- SO SÁNH HIỆU NĂNG KHI DÙNG @lru_cache (N = {N}) ---")

    # 1. Đo thời gian KHÔNG dùng Cache
    start = time.perf_counter()
    kq1 = tinh_fibo_thuong(N)
    time1 = time.perf_counter() - start
    print(f"1. Không dùng Cache : F({N}) = {kq1:,} | Thời gian: {time1:.4f} giây")

    # 2. Đo thời gian CÓ dùng Cache
    start = time.perf_counter()
    kq2 = tinh_fibo_co_cache(N)
    time2 = time.perf_counter() - start
    print(f"2. Có dùng LRU Cache: F({N}) = {kq2:,} | Thời gian: {time2:.6f} giây")

    print(f"\n => Caching giúp thuật toán chạy nhanh gấp ~{int(time1 / time2):,} lần!")


if __name__ == "__main__":
    main()
