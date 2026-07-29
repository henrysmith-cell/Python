from abc import ABC, abstractmethod


# 1. Interface đại diện cho Trạng thái
class TrangThaiDonHang(ABC):
    @abstractmethod
    def xu_ly_thanh_toan(self, context):
        pass

    @abstractmethod
    def giao_hang(self, context):
        pass


# 2. Trạng thái cụ thể: Chờ thanh toán
class TrangThaiChoThanhToan(TrangThaiDonHang):
    def xu_ly_thanh_toan(self, context):
        print(
            "[Thành công] Đã nhận thanh toán! Chuyển đơn hàng sang trạng thái 'ĐÁ BÀO CÓ / ĐÃ THANH TOÁN'."
        )
        context.chuyen_trang_thai(TrangThaiDaThanhToan())

    def giao_hang(self, context):
        print("[Thất bại] Chưa thể giao hàng vì đơn chưa được thanh toán!")


# 3. Trạng thái cụ thể: Đã thanh toán
class TrangThaiDaThanhToan(TrangThaiDonHang):
    def xu_ly_thanh_toan(self, context):
        print(
            "[Cảnh báo] Đơn hàng này đã được thanh toán rồi, không thể thanh toán lại."
        )

    def giao_hang(self, context):
        print("[Thành công] Đang đóng gói và bàn giao cho đơn vị vận chuyển!")
        context.chuyen_trang_thai(TrangThaiDaGiaoHang())


# 4. Trạng thái cụ thể: Đã giao hàng
class TrangThaiDaGiaoHang(TrangThaiDonHang):
    def xu_ly_thanh_toan(self, context):
        print("[Lỗi] Đơn hàng đã hoàn tất giao, không thể thanh toán lại.")

    def giao_hang(self, context):
        print("[Lỗi] Đơn hàng đã giao xong trước đó rồi.")


# 5. Context - Đơn hàng
class DonHangContext:
    def __init__(self):
        self._trang_thai_hien_tai = TrangThaiChoThanhToan()

    def chuyen_trang_thai(self, trang_thai_moi: TrangThaiDonHang):
        self._trang_thai_hien_tai = trang_thai_moi

    def thanh_toan(self):
        self._trang_thai_hien_tai.xu_ly_thanh_toan(self)

    def giao_hang(self):
        self._trang_thai_hien_tai.giao_hang(self)


def main():
    print("--- DEMO STATE DESIGN PATTERN ---")
    don_hang = DonHangContext()

    # Thử giao hàng khi chưa thanh toán
    don_hang.giao_hang()

    # Thanh toán đơn hàng
    print()
    don_hang.thanh_toan()

    # Giao hàng sau khi đã thanh toán
    print()
    don_hang.giao_hang()


if __name__ == "__main__":
    main()
