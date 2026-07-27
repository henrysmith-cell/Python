import time
from contextlib import contextmanager


@contextmanager
def do_thoi_gian_thuc_thi(ten_cong_viec: str):
    """
    Context Manager tự động đo thời gian chạy của khối lệnh bên trong 'with'.
    Phần trước 'yield' = code chạy lúc bắt đầu (__enter__)
    Phần sau 'yield'  = code chạy lúc kết thúc (__exit__)
    """
    print(f"⏱️ [Bắt đầu] {ten_cong_viec}...")
    start_time = time.perf_counter()
    try:
        # Nhường quyền điều khiển cho khối lệnh bên trong câu lệnh 'with'
        yield
    finally:
        # Luôn luôn thực thi đoạn code dọn dẹp/đo đạc này kể cả khi có lỗi
        thoi_gian = time.perf_counter() - start_time
        print(f"✅ [Hoàn thành] {ten_cong_viec} trong {thoi_gian:.4f} giây\n")


def main():
    print("--- DEMO @contextmanager DECORATOR ---")

    # Đo thời gian tính toán một tác vụ
    with do_thoi_gian_thuc_thi("Tính tổng 10 triệu số"):
        tong = sum(range(10_000_000))

    # Đo thời gian tạo danh sách
    with do_thoi_gian_thuc_thi("Tạo danh sách bình phương"):
        danh_sach = [x**2 for x in range(1_000_000)]


if __name__ == "__main__":
    main()
