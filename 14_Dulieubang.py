import csv
import os

FILE_CSV = "bang_diem.csv"


def tao_file_csv_mau():
    """Tạo file CSV chứa bảng điểm sinh viên làm dữ liệu thử nghiệm"""
    du_lieu = [
        ["MaSV", "HoTen", "DiemToan", "DiemTin"],
        ["SV01", "Nguyễn Văn A", 8.5, 9.0],
        ["SV02", "Trần Thị B", 6.0, 7.5],
        ["SV03", "Lê Hữu C", 9.5, 10.0],
    ]
    with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(du_lieu)
    print(f"[Khởi tạo] Đã tạo file mẫu '{FILE_CSV}' thành công.")


def doc_va_tinh_trung_binh():
    if not os.path.exists(FILE_CSV):
        tao_file_csv_mau()

    print("\n--- ĐỌC VÀ XỬ LÝ DỮ LIỆU TỪ FILE CSV ---")
    with open(FILE_CSV, mode="r", encoding="utf-8") as f:
        # Sử dụng DictReader để ánh xạ mỗi dòng thành một dictionary với key là tiêu đề cột
        reader = csv.DictReader(f)

        print(f"{'Mã SV':<8} | {'Họ và Tên':<15} | {'ĐTB':<6} | {'Xếp loại'}")
        print("-" * 45)

        for row in reader:
            diem_toan = float(row["DiemToan"])
            diem_tin = float(row["DiemTin"])
            dtb = (diem_toan + diem_tin) / 2

            xep_loai = "Giỏi" if dtb >= 8.0 else ("Khá" if dtb >= 6.5 else "Trung bình")
            print(f"{row['MaSV']:<8} | {row['HoTen']:<15} | {dtb:<6.1f} | {xep_loai}")


def main():
    tao_file_csv_mau()
    doc_va_tinh_trung_binh()


if __name__ == "__main__":
    main()
