from abc import ABC, abstractmethod


# 1. Visitor Interface
class VisitorBaoCao(ABC):
    @abstractmethod
    def visit_may_tinh(self, may_tinh):
        pass

    @abstractmethod
    def visit_dien_thoai(self, dien_thoai):
        pass


# 2. Element Interface
class ThietBi(ABC):
    @abstractmethod
    def accept(self, visitor: VisitorBaoCao):
        pass


# 3. Concrete Elements
class MayTinh(ThietBi):
    def __init__(self, ten: str, gia: float):
        self.ten = ten
        self.gia = gia

    def accept(self, visitor: VisitorBaoCao):
        visitor.visit_may_tinh(self)


class DienThoai(ThietBi):
    def __init__(self, ten: str, gia: float):
        self.ten = ten
        self.gia = gia

    def accept(self, visitor: VisitorBaoCao):
        visitor.visit_dien_thoai(self)


# 4. Concrete Visitor - Tính Thue VAT riêng cho từng loại thiết bị
class VisitorTinhThue(VisitorBaoCao):
    def __init__(self):
        self.tong_thue = 0

    def visit_may_tinh(self, may_tinh):
        thue = may_tinh.gia * 0.10  # Thuế máy tính 10%
        print(
            f" 💻 Máy tính '{may_tinh.ten}' (Giá: {may_tinh.gia:,}) -> Thuế 10%: {thue:,}"
        )
        self.tong_thue += thue

    def visit_dien_thoai(self, dien_thoai):
        thue = dien_thoai.gia * 0.05  # Thuế điện thoại 5%
        print(
            f" 📱 Điện thoại '{dien_thoai.ten}' (Giá: {dien_thoai.gia:,}) -> Thuế 5%: {thue:,}"
        )
        self.tong_thue += thue


def main():
    print("--- DEMO VISITOR DESIGN PATTERN ---")
    danh_sach_thiet_bi = [
        MayTinh("Laptop Gaming", 25000000),
        DienThoai("Smartphone Flagship", 15000000),
        MayTinh("PC Workstation", 40000000),
    ]

    tinh_thue_visitor = VisitorTinhThue()
    print("Áp dụng Visitor để tính thuế từng sản phẩm mà không sửa Class thiết bị:\n")
    for tb in danh_sach_thiet_bi:
        tb.accept(tinh_thue_visitor)

    print(f"\n👉 Tổng tiền thuế hệ thống thu được: {tinh_thue_visitor.tong_thue:,} VNĐ")


if __name__ == "__main__":
    main()
