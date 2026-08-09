from abc import ABC, abstractmethod


# Interface Trạng thái
class TrangThaiDonHang(ABC):
    @abstractmethod
    def xu_ly(self, don_hang):
        pass


# Concrete States
class ChoXacNhan(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print(
            "1. [Chờ xác nhận] Đơn hàng đang được xác thực. Chuyển sang: ĐÃ THANH TOÁN."
        )
        don_hang.set_state(DaThanhToan())


class DaThanhToan(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print(
            "2. [Đã thanh toán] Đang đóng gói và bàn giao shipper. Chuyển sang: ĐANG GIAO."
        )
        don_hang.set_state(DangGiao())


class DangGiao(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print(
            "3. [Đang giao] Khách hàng đã nhận hàng thành công. Chuyển sang: HOÀN THÀNH."
        )
        don_hang.set_state(HoanThanh())


class HoanThanh(TrangThaiDonHang):
    def xu_ly(self, don_hang):
        print("4. [Hoàn thành] Đơn hàng đã đóng. Không thể chuyển trạng thái nữa!")


# Context Class
class DonHang:
    def __init__(self):
        self._state = ChoXacNhan()  # Trạng thái ban đầu

    def set_state(self, state: TrangThaiDonHang):
        self._state = state

    def buoc_tiep_theo(self):
        self._state.xu_ly(self)


def main():
    print("--- DEMO STATE DESIGN PATTERN ---")
    dh = DonHang()

    # Chạy quy trình chuyển trạng thái đơn hàng
    dh.buoc_tiep_theo()
    dh.buoc_tiep_theo()
    dh.buoc_tiep_theo()
    dh.buoc_tiep_theo()


if __name__ == "__main__":
    main()
