import time
import functools


def doi_thoi_gian_thuc_thi(func):
    """
    Decorator dùng để tính thời gian chạy của bất kỳ hàm nào.
    Sử dụng @functools.wraps để giữ nguyên tên và docstring gốc của hàm.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Đo thời gian với độ chính xác cao
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(
            f"[BENCHMARK] Hàm '{func.__name__}' mất {execution_time:.6f} giây để hoàn thành."
        )
        return result

    return wrapper


# --- THỬ NGHIỆM SỬ DỤNG DECORATOR ---


@doi_thoi_gian_thuc_thi
def tinh_tong_mang_lon(n):
    """Hàm tạo danh sách n phần tử và tính tổng"""
    return sum(range(n))


@doi_thoi_gian_thuc_thi
def xu_ly_gia_lap_delay(so_giay):
    """Hàm giả lập công việc tốn thời gian chờ"""
    time.sleep(so_giay)
    return "Đã hoàn thành công việc"


def main():
    print("--- DEMO DECORATOR TRONG PYTHON ---")

    # Gọi hàm như bình thường, Decorator sẽ tự động đo thời gian
    tong = tinh_tong_mang_lon(10_000_000)
    print(f" -> Kết quả tính tổng: {tong:,}\n")

    thong_bao = xu_ly_gia_lap_delay(1.5)
    print(f" -> Trạng thái: {thong_bao}")


if __name__ == "__main__":
    main()
