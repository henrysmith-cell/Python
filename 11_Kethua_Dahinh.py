class ThanhVienTruongHoc:
    """Lớp cha (Base Class) đại diện cho một thành viên chung trong trường"""

    def __init__(self, ten, ma_so, email):
        self.ten = ten
        self.ma_so = ma_so
        self.email = email

    def hien_thi_thong_tin(self):
        """Hàm dùng chung cho tất cả các lớp con"""
        return f"Mã số: {self.ma_so} | Tên: {self.ten} | Email: {self.email}"


class GiangVien(ThanhVienTruongHoc):
    """Lớp con kế thừa từ ThanhVienTruongHoc"""

    def __init__(self, ten, ma_so, email, khoa, luong_co_ban):
        # Gọi hàm khởi tạo của lớp cha bằng super()
        super().__init__(ten, ma_so, email)
        self.khoa = khoa
        self.luong_co_ban = luong_co_ban

    def hien_thi_thong_tin(self):
        """Ghi đè (Override) phương thức của lớp cha - Tính đa hình"""
        thong_tin_goc = super().hien_thi_thong_tin()
        return f"[Giảng viên] {thong_tin_goc} | Khoa: {self.khoa} | Lương: {self.luong_co_ban:,} VND"


class SinhVien(ThanhVienTruongHoc):
    """Lớp con kế thừa từ ThanhVienTruongHoc"""

    def __init__(self, ten, ma_so, email, nganh_hoc, diem_gpa):
        super().__init__(ten, ma_so, email)
        self.nganh_hoc = nganh_hoc
        self.diem_gpa = diem_gpa

    def hien_thi_thong_tin(self):
        """Ghi đè (Override) phương thức để hiển thị thông tin đặc thù của sinh viên"""
        thong_tin_goc = super().hien_thi_thong_tin()
        return f"[Sinh viên]  {thong_tin_goc} | Ngành: {self.nganh_hoc} | Đao tạo GPA: {self.diem_gpa}"


def in_danh_sach_thanh_vien(danh_sach):
    print("\n--- XUẤT DANH SÁCH NHÂN SỰ / HỌC VIÊN ---")
    for tv in danh_sach:
        # Nhờ tính đa hình, Python tự biết gọi hàm hien_thi_thong_tin của lớp con tương ứng
        print(tv.hien_thi_thong_tin())


def main():
    # Khởi tạo danh sách chứa nhiều loại đối tượng khác nhau nhưng chung gốc
    danh_sach_truong = [
        GiangVien(
            "Nguyễn Minh Triết",
            "GV01",
            "trietnm@school.edu.vn",
            "Công nghệ Thông tin",
            15000000,
        ),
        SinhVien(
            "Lê Hoài Nam", "SV102", "namlh.sv@school.edu.vn", "Sư phạm Tin học", 8.7
        ),
        SinhVien("Trần Thị Hồng", "SV103", "hongtt.sv@school.edu.vn", "Kế toán", 7.9),
    ]

    in_danh_sach_thanh_vien(danh_sach_truong)


if __name__ == "__main__":
    main()
