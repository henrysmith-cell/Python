from abc import ABC, abstractmethod


# 1. State Interface
class TrangThaiDonHang(ABC):
    @abstractmethod
    def xu_ly(self, don_hang):
        pass


# 2. Concrete States
class TrangThaiMoiTao(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print("-> [Mới tạo] Đang xác thực thông tin và thanh toán...")
        don_hang.set_trang_thai(TrangThaiDaThanhToan())


class TrangThaiDaThanhToan(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print("-> [Đã thanh toán] Đang đóng gói và bàn giao cho đơn vị vận chuyển...")
        don_hang.set_trang_thai(TrangThaiDangGiao())


class TrangThaiDangGiao(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print("-> [Đang giao] Khách hàng đã nhận hàng thành công!")
        don_hang.set_trang_thai(TrangThaiHoanThanh())


class TrangThaiHoanThanh(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print("-> [Hoàn thành] Đơn hàng đã kết thúc. Không thể chuyển trạng thái nữa.")


# 3. Context - Đơn hàng
class DonHang:
    def __init__(self, ma_don: str):
        self.ma_don = ma_don
        self._trang_thai = TrangThaiMoiTao()  # Trạng thái ban đầu

    def set_trang_thai(self, trang_thai: TrangThaiDonHang):
        self._trang_thai = trang_thai

    def buoc_tiep_theo(self):
        self._trang_thai.xu_ly(self)


def main():
    print("--- DEMO STATE DESIGN PATTERN (QUẢN LÝ ĐƠN HÀNG) ---")
    don_hang = DonHang("DH_1002")

    # Giả lập chuyển trạng thái liên tục
    for _ in range(4):
        don_hang.buoc_tiep_theo()


if __name__ == "__main__":
    main()
