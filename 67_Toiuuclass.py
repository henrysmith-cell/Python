import sys


# Class thông thường (Tạo __dict__ ngầm)
class SinhVienThuong:
    def __init__(self, mssv, ho_ten):
        self.mssv = mssv
        self.ho_ten = ho_ten


# Class tối ưu bộ nhớ với __slots__
class SinhVienToiUu:
    __slots__ = ["mssv", "ho_ten"]  # Cố định danh sách thuộc tính

    def __init__(self, mssv, ho_ten):
        self.mssv = mssv
        self.ho_ten = ho_ten


def main():
    print("--- DEMO TỐI ƯU BỘ NHỚ VỚI __SLOTS__ ---")

    sv1 = SinhVienThuong("22001", "Nguyen Van A")
    sv2 = SinhVienToiUu("22002", "Tran Thi B")

    # Đo kích thước đối tượng gốc (chưa tính dữ liệu con)
    size1 = sys.getsizeof(sv1) + sys.getsizeof(sv1.__dict__)
    size2 = sys.getsizeof(sv2)

    print(f"Kích thước SinhVienThuong (có __dict__): {size1} bytes")
    print(f"Kích thước SinhVienToiUu  (dùng __slots__): {size2} bytes")
    print(f"⚡ Tiết kiệm bộ nhớ đáng kể cho từng Object!")


if __name__ == "__main__":
    main()
