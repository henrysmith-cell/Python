import fnmatch


def main():
    print("--- DEMO LỌC TÊN FILE BẰNG FNMATCH ---")

    danh_sach_files = [
        "baicao_01.py",
        "baicao_02.cpp",
        "report_2026.pdf",
        "image_test.PNG",
        "temp_data.tmp",
        "data_2026_final.csv",
    ]

    # 1. Tìm tất cả file Python (.py)
    python_files = fnmatch.filter(danh_sach_files, "*.py")
    print(f"1. Các file Python: {python_files}")

    # 2. Tìm tất cả file chứa số '2026'
    report_files = fnmatch.filter(danh_sach_files, "*2026*")
    print(f"2. Các file năm 2026: {report_files}")

    # 3. Kiểm tra không phân biệt chữ hoa/thường bằng fnmatchcase
    is_png = fnmatch.fnmatchcase("image_test.PNG", "*.PNG")
    print(f"3. File image_test.PNG có đúng định dạng .PNG? -> {is_png}")


if __name__ == "__main__":
    main()
