from functools import total_ordering


@total_ordering
class SanPhamToiUu:
    def __init__(self, ten: str, gia: float):
        self.ten = ten
        self.gia = gia

    def __eq__(self, other):
        """So sánh bằng nhau theo giá"""
        if not isinstance(other, SanPhamToiUu):
            return NotImplemented
        return self.gia == other.gia

    def __lt__(self, other):
        """So sánh nhỏ hơn theo giá"""
        if not isinstance(other, SanPhamToiUu):
            return NotImplemented
        return self.gia < other.gia


def main():
    print("--- DEMO @functools.total_ordering ---")
    sp1 = SanPhamToiUu("Laptop", 15000000)
    sp2 = SanPhamToiUu("Điện thoại", 8000000)
    sp3 = SanPhamToiUu("Tai nghe", 8000000)

    # Nhờ @total_ordering, em có thể dùng MỌI phép so sánh:
    print(f"1. Laptop > Điện thoại?     : {sp1 > sp2}")  # Tự suy ra từ __lt__
    print(f"2. Điện thoại <= Laptop?   : {sp2 <= sp1}")  # Tự suy ra
    print(f"3. Điện thoại == Tai nghe?  : {sp2 == sp3}")  # Dùng __eq__
    print(f"4. Điện thoại != Laptop?   : {sp2 != sp1}")  # Tự suy ra


if __name__ == "__main__":
    main()
