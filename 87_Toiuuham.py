import time
from functools import lru_cache


# Khai báo cache tối đa 128 kết quả gần nhất
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """Tính số Fibonacci thứ n có sử dụng Caching"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("--- DEMO TỐI ƯU TỐC ĐỘ BẰNG FUNCTOOLS.LRU_CACHE ---")

    start = time.perf_counter()
    n = 35
    ket_qua = fibonacci(n)
    end = time.perf_counter()

    print(f"Số Fibonacci thứ {n} là: {ket_qua}")
    print(f"⏱️  Thời gian tính toán (nhờ Cache): {(end - start) * 1000:.4f} ms")

    # Kiểm tra thông tin hiệu suất của Cache (hits, misses, maxsize, currsize)
    print("\nThống kê hoạt động của Cache:")
    print(fibonacci.cache_info())


if __name__ == "__main__":
    main()
