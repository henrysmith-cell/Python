from abc import ABC, abstractmethod


# 1. Visitor Interface
class BieuPhiVisitor(ABC):
    @abstractmethod
    def visit_sach(self, sach):
        pass

    @abstractmethod
    def visit_thiet_bi(self, thiet_bi):
        pass


# 2. Element Interface
class SanPham(ABC):
    @abstractmethod
    def accept(self, visitor: BieuPhiVisitor):
        pass


# 3. Concrete Elements
class Sach(SanPham):
    def __init__(self, ten: str, gia: float):
        self.ten = ten
        self.gia = gia

    def accept(self, visitor: BieuPhiVisitor):
        return visitor.visit_sach(self)


class ThietBiDienTu(SanPham):
    def __init__(self, ten: str, gia: float):
        self.ten = ten
        self.gia = gia

    def accept(self, visitor: BieuPhiVisitor):
        return visitor.visit_thiet_bi(self)


# 4. Concrete Visitor - Tính phí vận chuyển theo loại sản phẩm
class TinhPhiVanChuyenVisitor(BieuPhiVisitor):
    def visit_sach(self, sach: Sach) -> float:
        # Sách đồng giá phí vận chuyển 10.000 VNĐ
        return 10_000.0

    def visit_thiet_bi(self, thiet_bi: ThietBiDienTu) -> float:
        # Thiết bị điện tử tính 5% giá trị sản phẩm
        return thiet_bi.gia * 0.05


def main():
    print("--- DEMO VISITOR DESIGN PATTERN ---")

    # Dùng dấu _ để phân cách hàng nghìn thay cho dấu .
    gio_hang = [
        Sach("Lập trình Python Nâng cao", 150_000),
        ThietBiDienTu("Bàn phím Cơ", 1_200_000),
        ThietBiDienTu("Chuột Không dây", 400_000),
    ]

    visitor_van_chuyen = TinhPhiVanChuyenVisitor()
    tong_phi_ship = 0.0

    print("Chi tiết phí vận chuyển:")
    for sp in gio_hang:
        phi = sp.accept(visitor_van_chuyen)
        tong_phi_ship += phi
        # Định dạng in số tiền dùng dấu phẩy cho hàng nghìn
        print(f" - {sp.ten:<30}: {phi:,.0f} VNĐ")

    print(f"\n👉 Tổng phí vận chuyển đơn hàng: {tong_phi_ship:,.0f} VNĐ")


if __name__ == "__main__":
    main()
