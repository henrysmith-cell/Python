from enum import Enum, auto


class TrangThaiThanhToan(Enum):
    CHO_XU_LY = auto()  # Tự động gán giá trị tăng dần (1)
    THANH_TOAN_THANH_CONG = auto()  # (2)
    THAT_BAI = auto()  # (3)
    DA_HOAN_TIEN = auto()  # (4)


def kiem_tra_trang_thai(status: TrangThaiThanhToan):
    if status == TrangThaiThanhToan.THANH_TOAN_THANH_CONG:
        print("✅ Giao dịch hợp lệ. Bắt đầu xuất kho sản phẩm!")
    elif status == TrangThaiThanhToan.CHO_XU_LY:
        print("⏳ Đang chờ phản hồi từ cổng thanh toán...")
    elif status == TrangThaiThanhToan.THAT_BAI:
        print("❌ Thanh toán thất bại. Vui lòng thử lại!")


def main():
    print("--- DEMO ENUM TRONG PYTHON ---")

    # 1. Sử dụng Enum
    trang_thai_hien_tai = TrangThaiThanhToan.THANH_TOAN_THANH_CONG
    print(
        f"Trạng thái: {trang_thai_hien_tai.name} (Value: {trang_thai_hien_tai.value})"
    )

    kiem_tra_trang_thai(trang_thai_hien_tai)

    # 2. Duyệt qua tất cả trạng thái hợp lệ trong hệ thống
    print("\nDanh sách tất cả trạng thái thanh toán:")
    for status in TrangThaiThanhToan:
        print(f" - {status.name:<25}: {status.value}")


if __name__ == "__main__":
    main()
