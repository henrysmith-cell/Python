import time


class QuanLyThoiGianGiaoDich:
    """
    Context Manager tự định nghĩa dùng để giám sát và đảm bảo
    các giao dịch/thao tác không vượt quá thời gian cho phép.
    """

    def __init__(self, ten_thao_tac):
        self.ten_thao_tac = ten_thao_tac

    def __enter__(self):
        """Được gọi tự động khi bắt đầu khối lệnh 'with'"""
        print(f"[BẮT ĐẦU] {self.ten_thao_tac}...")
        self.start_time = time.perf_counter()
        return self  # Có thể trả về đối tượng để dùng bên trong 'with ... as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Được gọi tự động khi THOÁT khỏi khối 'with',
        kể cả khi có ngoại lệ (exception) xảy ra bên trong.
        """
        duration = time.perf_counter() - self.start_time
        print(f"[KẾT THÚC] {self.ten_thao_tac} hoàn tất trong {duration:.4f} giây.")

        # Nếu có lỗi xảy ra bên trong khối 'with'
        if exc_type is not None:
            print(f"[CẢNH BÁO] Phát hiện lỗi '{exc_val}' trong quá trình xử lý!")
            # Trả về True nếu muốn 'nuốt' lỗi, trả về False để lỗi tiếp tục văng ra ngoài
            return True


def main():
    print("--- DEMO CONTEXT MANAGER TỰ ĐỊNH NGHĨA ---")

    # 1. Trường hợp chạy bình thường
    with QuanLyThoiGianGiaoDich("Tải dữ liệu cấu hình"):
        time.sleep(0.5)
        print(" -> Đang ghi dữ liệu vào RAM...")

    print("-" * 40)

    # 2. Trường hợp xẩy ra lỗi bên trong khối lệnh
    with QuanLyThoiGianGiaoDich("Xử lý tính toán bị lỗi"):
        time.sleep(0.2)
        print(" -> Đang thực hiện phép chia...")
        ket_qua = 10 / 0  # Lỗi ZeroDivisionError

    print("\n[Hệ thống] Chương trình vẫn tiếp tục chạy an toàn không bị crash!")


if __name__ == "__main__":
    main()
