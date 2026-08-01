from collections import namedtuple


def main():
    print("--- DEMO NAMEDTUPLE TRONG PYTHON ---")

    # Định nghĩa cấu trúc SinhVien với các trường thông tin
    SinhVien = namedtuple("SinhVien", ["mssv", "ho_ten", "gpa"])

    # Khởi tạo đối tượng
    sv1 = SinhVien(mssv="220011", ho_ten="Nguyễn Văn A", gpa=3.8)
    sv2 = SinhVien(mssv="220012", ho_ten="Trần Thị B", gpa=3.6)

    # Truy cập thông tin bằng tên thuộc tính thay vì chỉ số index
    print(f"Mã số SV: {sv1.mssv}")
    print(f"Họ và tên: {sv1.ho_ten}")
    print(f"Điểm GPA: {sv1.gpa}")

    # namedtuple cho phép Unpacking cực kỳ tiện lợi
    mssv, ten, gpa = sv2
    print(f"\nUnpack SV2: {ten} - GPA: {gpa}")


if __name__ == "__main__":
    main()
