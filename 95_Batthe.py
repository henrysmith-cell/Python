import re


def main():
    print("--- DEMO TRÍCH XUẤT VÀ VỊ TRÍ CHUỖI VỚI RE.FINDITER ---")

    van_ban = "Mã đơn hàng DH-102 có giá 150000 VNĐ, mã DH-105 giá 450000 VNĐ."
    pattern = r"DH-\d+"  # Biểu thức chính quy tìm định dạng DH-số

    print(f"Văn bản gốc: '{van_ban}'\n")
    print("Các mã đơn hàng tìm thấy:")

    # Duyệt qua từng match thu được từ finditer
    for match in re.finditer(pattern, van_ban):
        ma_dh = match.group()
        vitri_bd = match.start()
        vitri_kt = match.end()
        print(f" - Mã: {ma_dh:<8} | Vị trí: từ ký tự {vitri_bd} đến {vitri_kt}")


if __name__ == "__main__":
    main()
