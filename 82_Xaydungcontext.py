import time


class QuanLyThoiGianThucThi:
    """Context Manager đo thời gian chạy của một khối lệnh và xử lý ngoại lệ an toàn"""

    def __init__(self, ten_khoi_lenh: str):
        self.ten_khoi_lenh = ten_khoi_lenh

    def __enter__(self):
        print(f"⏱️  [Bắt đầu] Khối lệnh: '{self.ten_khoi_lenh}'")
        self.start_time = time.perf_counter()
        return self  # Giá trị trả về cho biến sau từ khóa 'as' (nếu có)

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.perf_counter() - self.start_time
        print(
            f"⏱️  [Kết thúc] Khối lệnh: '{self.ten_khoi_lenh}' hoàn thành trong {duration:.4f} giây."
        )

        # Nếu có ngoại lệ xảy ra trong khối with
        if exc_type is not None:
            print(
                f"⚠️ Phát hiện lỗi: {exc_val} (Đã được Context Manager bắt lại an toàn)"
            )
            return True  # Trả về True để nuốt ngoại lệ, không làm crash ứng dụng!


def main():
    print("--- DEMO CUSTOM CONTEXT MANAGER ---")

    # 1. Trường hợp thực thi bình thường
    with QuanLyThoiGianThucThi("Tính toán vòng lặp"):
        tong = sum(i * i for i in range(1_000_000))
        print(f"   Kết quả tính toán: {tong}")

    print("\n" + "=" * 40 + "\n")

    # 2. Trường hợp xảy ra lỗi bên trong khối with
    with QuanLyThoiGianThucThi("Xử lý chia cho 0"):
        print("   Đang thực hiện phép tính nguy hiểm...")
        ket_qua = 10 / 0  # Gây ra ZeroDivisionError

    print("\n👉 Chương trình vẫn tiếp tục chạy bình thường mà không bị crash!")


if __name__ == "__main__":
    main()
