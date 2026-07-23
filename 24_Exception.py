class LoiHeThongBase(Exception):
    """Lớp Exception cơ sở cho toàn bộ ứng dụng"""

    pass


class LoiSoDuKhongDu(LoiHeThongBase):
    """Xảy ra khi tài khoản không đủ tiền thực hiện giao dịch"""

    def __init__(self, so_du_hien_tai, so_tien_rut):
        self.so_du_hien_tai = so_du_hien_tai
        self.so_tien_rut = so_tien_rut
        super().__init__(
            f"Lỗi số dư: Hiện có {so_du_hien_tai:,} VND nhưng muốn rút {so_tien_rut:,} VND."
        )


class LoiHackerTruyCap(LoiHeThongBase):
    """Xảy ra khi phát hiện hành vi nghi vấn bảo mật"""

    def __init__(self, ip_address):
        self.ip_address = ip_address
        super().__init__(
            f"Cảnh báo an ninh: Truy cập bất hợp pháp từ địa chỉ IP {ip_address}!"
        )


# --- HÀM NGHIỆP VỤ SỬ DỤNG CUSTOM EXCEPTION ---


def xu_ly_chuyen_tien(so_du, so_tien, ip):
    if ip.startswith("192.168.0."):
        raise LoiHackerTruyCap(ip)
    if so_tien > so_du:
        raise LoiSoDuKhongDu(so_du, so_tien)

    return so_du - so_tien


def main():
    print("--- HỆ THỐNG XỬ LÝ NGOẠI LỆ TỰ ĐỊNH NGHĨA (CUSTOM EXCEPTIONS) ---")

    tai_khoan_demo = [
        {"so_du": 500_000, "rut": 1_000_000, "ip": "10.0.0.1"},  # Sẽ bị lỗi số dư
        {
            "so_du": 2_000_000,
            "rut": 100_000,
            "ip": "192.168.0.99",
        },  # Sẽ bị lỗi security
        {"so_du": 1_000_000, "rut": 200_000, "ip": "10.0.0.5"},  # Hợp lệ
    ]

    for idx, tk in enumerate(tai_khoan_demo, 1):
        print(f"\n[Giao dịch {idx}] Đang xử lý...")
        try:
            so_du_moi = xu_ly_chuyen_tien(tk["so_du"], tk["rut"], tk["ip"])
            print(f" -> Giao dịch thành công! Số dư còn lại: {so_du_moi:,} VND")
        except LoiSoDuKhongDu as e:
            print(f" -> [Xử lý Lỗi Nghiệp Vụ] {e}")
        except LoiHackerTruyCap as e:
            print(f" -> [Xử lý Lỗi An Ninh] {e} -> Đã khóa IP!")
        except LoiHeThongBase as e:
            print(f" -> [Lỗi Hệ Thống Chung] {e}")


if __name__ == "__main__":
    main()
