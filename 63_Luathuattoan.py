from abc import ABC, abstractmethod


# 1. Strategy Interface
class ChienLuocThanhToan(ABC):
    @abstractmethod
    def thanh_toan(self, so_tien: int):
        pass


# 2. Concrete Strategies
class ThanhToanMoMo(ChienLuocThanhToan):
    def thanh_toan(self, so_tien: int):
        print(f"📱 Quét mã QR MoMo để thanh toán: {so_tien:,} VNĐ thành công!")


class ThanhToanTheTinDung(ChienLuocThanhToan):
    def thanh_toan(self, so_tien: int):
        print(f"💳 Quẹt thẻ tín dụng (VISA/Mastercard): {so_tien:,} VNĐ thành công!")


class ThanhToanBanking(ChienLuocThanhToan):
    def thanh_toan(self, so_tien: int):
        print(f"🏦 Chuyển khoản ngân hàng trực tuyến: {so_tien:,} VNĐ thành công!")


# 3. Context - Giỏ hàng
class GioHang:
    def __init__(self, tong_tien: int):
        self.tong_tien = tong_tien
        self._chien_luoc = None

    def dat_chien_luoc_thanh_toan(self, chien_luoc: ChienLuocThanhToan):
        self._chien_luoc = chien_luoc

    def xu_ly_thanh_toan(self):
        if not self._chien_luoc:
            print("❌ Lỗi: Vui lòng chọn phương thức thanh toán!")
            return
        self._chien_luoc.thanh_toan(self.tong_tien)


def main():
    print("--- DEMO STRATEGY DESIGN PATTERN ---")
    gio_hang = GioHang(tong_tien=500000)

    # Khách hàng chọn thanh toán qua MoMo
    print("1. Khách chọn MoMo:")
    gio_hang.dat_chien_luoc_thanh_toan(ThanhToanMoMo())
    gio_hang.xu_ly_thanh_toan()

    # Đổi ý chuyển sang quẹt thẻ ngay lập tức mà không đổi logic giỏ hàng
    print("\n2. Đổi sang Thanh toán qua Thẻ tín dụng:")
    gio_hang.dat_chien_luoc_thanh_toan(ThanhToanTheTinDung())
    gio_hang.xu_ly_thanh_toan()


if __name__ == "__main__":
    main()
