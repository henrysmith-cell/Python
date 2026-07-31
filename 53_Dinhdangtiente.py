import locale


def main():
    print("--- DEMO ĐỊNH DẠNG SỐ & TIỀN TỆ VỚI LOCALE ---")

    so_tien = 1250000000.75  # 1.25 tỷ

    # Set locale về mặc định hệ thống hoặc Việt Nam (nếu hệ thống hỗ trợ)
    try:
        # Trên Windows/Linux tên locale tiếng Việt có thể là 'vi_VN' hoặc 'vietnamese'
        locale.setlocale(locale.LC_ALL, "vi_VN.UTF-8")
    except locale.Error:
        # Fallback về locale mặc định nếu OS chưa cài locale vi_VN
        locale.setlocale(locale.LC_ALL, "")

    # Định dạng số có phân cách hàng nghìn
    so_dinh_dang = locale.format_string("%.2f", so_tien, grouping=True)
    print(f"Số nguyên gốc : {so_tien}")
    print(f"Định dạng chuẩn: {so_dinh_dang}")


if __name__ == "__main__":
    main()
