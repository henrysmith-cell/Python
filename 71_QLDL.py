from dataclasses import dataclass, field


@dataclass(order=True)
class SanPham:
    # Trường sort_index được dùng để so sánh/sắp xếp các đối tượng SanPham
    sort_index: float = field(init=False, repr=False)

    ten_sp: str
    gia_tien: float
    so_luong: int = 0

    def __post_init__(self):
        # Tự động tính sort_index theo giá tiền để tiện so sánh
        self.sort_index = self.gia_tien


def main():
    print("--- DEMO PYTHON DATACLASS ---")

    sp1 = SanPham("Bàn phím Cơ", 1200000, 5)
    sp2 = SanPham("Chuột Lập trình", 800000, 10)
    sp3 = SanPham("Bàn phím Cơ", 1200000, 5)

    # Automatically supports clear string representation (__repr__)
    print(f"Sản phẩm 1: {sp1}")

    # Auto-supports value equality comparison (__eq__)
    print(f"Sản phẩm 1 bằng Sản phẩm 3? -> {sp1 == sp3}")

    # Auto-supports order comparison based on sort_index (__lt__, __gt__)
    print(f"Sản phẩm 1 đắt hơn Sản phẩm 2? -> {sp1 > sp2}")


if __name__ == "__main__":
    main()
