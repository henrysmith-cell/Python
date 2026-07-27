from abc import ABC, abstractmethod


# 1. Interface chung cho các Chiến lược Giảm giá
class ChienLuocGiamGia(ABC):
    @abstractmethod
    def tinh_giam_gia(self, tong_tien: float) -> float:
        pass


# 2. Các chiến lược cụ thể
class KhongGiamGia(ChienLuocGiamGia):
    def tinh_giam_gia(self, tong_tien: float) -> float:
        return 0.0


class GiamGiaPhanTram(ChienLuocGiamGia):
    def __init__(self, phan_tram: float):
        self.phan_tram = phan_tram

    def tinh_giam_gia(self, tong_tien: float) -> float:
        return tong_tien * (self.phan_tram / 100)


class GiamGiaCoDinh(ChienLuocGiamGia):
    def __init__(self, so_tien_giam: float):
        self.so_tien_giam = so_tien_giam

    def tinh_giam_gia(self, tong_tien: float) -> float:
        return min(self.so_tien_giam, tong_tien)


# 3. Context - Đơn hàng sử dụng Chiến lược
class DonHang:
    def __init__(self, tong_tien: float, chien_luoc_giam_gia: ChienLuocGiamGia):
        self.tong_tien = tong_tien
        self.chien_luoc = chien_luoc_giam_gia

    def tinh_tien_thanh_toan(self) -> float:  # Đã sửa thành một dấu ngoặc đơn (self)
        giam = self.chien_luoc.tinh_giam_gia(self.tong_tien)
        return self.tong_tien - giam


def main():
    print("--- DEMO STRATEGY DESIGN PATTERN ---")
    tong_tien_hang = 1000000.0  # 1 triệu VND

    # Đơn 1: Không áp mã
    don1 = DonHang(tong_tien_hang, KhongGiamGia())
    print(f"Đơn 1 (Không giảm giá) : {don1.tinh_tien_thanh_toan():,.0f} VND")

    # Đơn 2: Áp mã giảm 15%
    don2 = DonHang(tong_tien_hang, GiamGiaPhanTram(phan_tram=15))
    print(f"Đơn 2 (Giảm 15%)       : {don2.tinh_tien_thanh_toan():,.0f} VND")

    # Đơn 3: Áp voucher 100k
    don3 = DonHang(tong_tien_hang, GiamGiaCoDinh(so_tien_giam=100000))
    print(f"Đơn 3 (Voucher 100k)   : {don3.tinh_tien_thanh_toan():,.0f} VND")


if __name__ == "__main__":
    main()
