import re


def kiem_tra_dinh_dang_email(email):
    # Regex cơ bản cho email: username@domain.ext
    pattern = r"^[a-zA-Blob0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def trich_xuat_so_dien_thoai(van_ban):
    """Tìm tất cả các số điện thoại dạng 10 chữ số (bắt đầu bằng số 0) trong đoạn văn"""
    pattern = r"\b0\d{9}\b"
    return re.findall(pattern, van_ban)


def main():
    print("--- DEMO XỬ LÝ CHUỖI VỚI REGEX ---")

    # 1. Kiểm tra Validate Email
    danh_sach_email = [
        "user.test@gmail.com",
        "sai-dinh-dang@domain",
        "hocvien123@dthu.edu.vn",
    ]

    print("1. Kiểm tra Email:")
    for email in danh_sach_email:
        hop_le = kiem_tra_dinh_dang_email(email)
        trang_thai = "Hợp lệ ✓" if hop_le else "Không hợp lệ ✗"
        print(f" - Email '{email}': {trang_thai}")

    # 2. Trích xuất thông tin từ đoạn văn bản thô
    doan_van_tho = """
    Mọi thắc mắc xin liên hệ bộ phận hỗ trợ qua hotline 0912345678 hoặc 0987654321.
    Lưu ý không gọi vào số máy lẻ 12345 hoặc số thừa chữ số 012345678901.
    """

    print("\n2. Trích xuất số điện thoại từ văn bản:")
    sdt_tim_thay = trich_xuat_so_dien_thoai(doan_van_tho)
    print(f" -> Các SĐT hợp lệ tìm được: {sdt_tim_thay}")


if __name__ == "__main__":
    main()
