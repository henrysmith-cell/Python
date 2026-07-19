import random


class TaiKhoanNganHang:
    """Lớp đại diện cho một tài khoản ngân hàng thông thường"""

    def __init__(self, ten_chu_tk, so_du_ban_dau=0):
        self.ten_chu_tk = ten_chu_tk
        # Sử dụng dấu gạch dưới kép '__' để tạo biến private, tránh chỉnh sửa trực tiếp bên ngoài
        self.__so_tk = str(random.randint(100000000, 999999999))
        self.__so_du = so_du_ban_dau if so_du_ban_dau >= 0 else 0

    # Getter để xem số tài khoản
    @property
    def so_tk(self):
        return self.__so_tk

    # Getter để xem số dư an toàn
    @property
    def so_du(self):
        return self.__so_du

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"[+] Nạp thành công {so_tien:,} VND vào TK {self.__so_tk}.")
            self.kiem_tra_so_du()
        else:
            print("[-] Số tiền nạp vào phải lớn hơn 0!")

    def rut_tien(self, so_tien):
        if so_tien <= 0:
            print("[-] Số tiền rút không hợp lệ!")
            return False
        if so_tien > self.__so_du:
            print(
                f"[-] Rút tiền thất bại! Số dư hiện tại không đủ ({self.__so_du:,} VND)."
            )
            return False

        self.__so_du -= so_tien
        print(f"[-] Rút thành công {so_tien:,} VND từ TK {self.__so_tk}.")
        self.kiem_tra_so_du()
        return True

    def kiem_tra_so_du(self):
        print(
            f"[Thông tin] Tài khoản: {self.ten_chu_tk} | STK: {self.__so_tk} | Số dư: {self.__so_du:,} VND"
        )


def main():
    # Khởi tạo hai tài khoản demo
    print("--- Khởi tạo tài khoản ---")
    tk_an = TaiKhoanNganHang("Nguyễn Văn An", 500000)
    tk_binh = TaiKhoanNganHang("Trần Thị Bình", 1000000)

    tk_an.kiem_tra_so_du()
    tk_binh.kiem_tra_so_du()

    print("\n--- Thực hiện giao dịch trên tài khoản cá nhân ---")
    # Thử nạp tiền
    tk_an.nap_tien(200000)
    # Thử rút tiền quá số dư
    tk_an.rut_tien(1000000)
    # Thử rút tiền hợp lệ
    tk_an.rut_tien(300000)


if __name__ == "__main__":
    main()
