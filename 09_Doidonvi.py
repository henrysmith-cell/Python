def kiem_tra_nhap_so(thong_bao):
    """Hàm đảm bảo người dùng nhập đúng số dương, tránh crash chương trình"""
    while True:
        try:
            gia_tri = float(input(thong_bao))
            if gia_tri >= 0:
                return gia_tri
            print("[Lỗi] Vui lòng nhập một số lớn hơn hoặc bằng 0!")
        except ValueError:
            print("[Lỗi] Định dạng không hợp lệ! Vui lòng nhập số.")


def tinh_lai_suat():
    print("\n--- CÔNG CỤ TÍNH LÃI SUẤT TIẾT KIỆM (TÍNH CUỐI KỲ) ---")
    so_tien_goc = kiem_tra_nhap_so("Nhập số tiền gửi (VND): ")
    lai_suat_nam = kiem_tra_nhap_so("Nhập lãi suất phần trăm năm (ví dụ: 5.5): ")
    so_thang = int(kiem_tra_nhap_so("Nhập số tháng gửi: "))

    # Công thức tính lãi đơn giản cuối kỳ
    # Tiền lãi = Số tiền gốc * (Lãi suất năm / 100) * (Số tháng gửi / 12)
    tien_lai = so_tien_goc * (lai_suat_nam / 100) * (so_thang / 12)
    tong_nhan = so_tien_goc + tien_lai

    print("\n[KẾT QUẢ TÍNH TOÁN]")
    print(f" - Tiền gốc ban đầu : {so_tien_goc:,.0f} VND")
    print(f" - Tiền lãi nhận được: {tien_lai:,.0f} VND")
    print(f" - Tổng tiền nhận được: {tong_nhan:,.0f} VND")


def doi_ngoai_te():
    # Tỷ giá giả định làm mẫu
    TY_GIA_USD = 25000
    print("\n--- CÔNG CỤ QUY ĐỔI TIỀN TỆ (VND -> USD) ---")
    so_tien_vnd = kiem_tra_nhap_so("Nhập số tiền VND muốn đổi: ")

    so_tien_usd = so_tien_vnd / TY_GIA_USD
    print(
        f"\n[KẾT QUẢ] {so_tien_vnd:,.0f} VND = {so_tien_usd:,.2f} USD (Tỷ giá: 1 USD = {TY_GIA_USD:,.0f} VND)"
    )


def main():
    while True:
        print("\n=== CÔNG CỤ TÀI CHÍNH MINI ===")
        print("1. Tính lãi suất tiết kiệm")
        print("2. Đổi tiền VND sang USD")
        print("3. Thoát")

        lua_chon = input("Chọn chức năng (1-3): ").strip()
        if lua_chon == "1":
            tinh_lai_suat()
        elif lua_chon == "2":
            # Sửa nhẹ lỗi typo biến hiển thị nếu chạy thực tế
            TY_GIA_USD = 25000
            so_tien_vnd = kiem_tra_nhap_so("Nhập số tiền VND muốn đổi: ")
            print(
                f"[KẾT QUẢ] {so_tien_vnd:,.0f} VND = {so_tien_vnd / TY_GIA_USD:,.2f} USD"
            )
        elif lua_chon == "3":
            print("Tạm biệt em!")
            break
        else:
            print("[Lỗi] Vui lòng chọn từ 1 đến 3.")


if __name__ == "__main__":
    main()
