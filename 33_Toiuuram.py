import sys


class SinhVienThuong:
    """Class thông thường (Sử dụng __dict__ mặc định)"""

    def __init__(self, ma_sv, ho_ten, gpa):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gpa = gpa


class SinhVienToiUu:
    """Class tối ưu bằng __slots__ (Không tạo __dict__)"""

    __slots__ = ("ma_sv", "ho_ten", "gpa")

    def __init__(self, ma_sv, ho_ten, gpa):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gpa = gpa


def main():
    print("--- SO SÁNH DUNG LƯỢNG BỘ NHỚ KHI DÙNG __slots__ ---")

    sv1 = SinhVienThuong("SV01", "Nguyễn Văn A", 3.8)
    sv2 = SinhVienToiUu("SV02", "Trần Thị B", 3.9)

    # Kích thước RAM cơ bản của object
    size_sv1 = sys.getsizeof(sv1) + sys.getsizeof(sv1.__dict__)
    size_sv2 = sys.getsizeof(sv2)

    print(f"Kích thước SinhVienThuong (dùng dict) : {size_sv1} bytes")
    print(f"Kích thước SinhVienToiUu (dùng slots): {size_sv2} bytes")

    ti_le = ((size_sv1 - size_sv2) / size_sv1) * 100
    print(f" -> Tiết kiệm được khoảng {ti_le:.1f}% bộ nhớ RAM cho mỗi object!")


if __name__ == "__main__":
    main()
