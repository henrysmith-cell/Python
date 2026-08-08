from abc import ABC, abstractmethod


# 1. Observer Interface
class NguoiNhanThongBao(ABC):
    @abstractmethod
    def cap_nhat(self, ten_san_pham: str, gia_moi: float):
        pass


# 2. Subject Class
class SanPhamTheoDoi:
    def __init__(self, ten_sp: str, gia_bandau: float):
        self.ten_sp = ten_sp
        self._gia = gia_bandau
        self._danh_sach_observers = []

    def dang_ky(self, observer: NguoiNhanThongBao):
        if observer not in self._danh_sach_observers:
            self._danh_sach_observers.append(observer)

    def huydang_ky(self, observer: NguoiNhanThongBao):
        self._danh_sach_observers.remove(observer)

    def thay_doi_gia(self, gia_moi: float):
        print(
            f"\n📢 [Hệ thống] Giá sản phẩm '{self.ten_sp}' thay đổi: {self._gia:,.0f} -> {gia_moi:,.0f} VNĐ"
        )
        self._gia = gia_moi
        self._thong_bao_tat_ca()

    def _thong_bao_tat_ca(self):
        for obs in self._danh_sach_observers:
            obs.cap_nhat(self.ten_sp, self._gia)


# 3. Concrete Observers
class KhachHangEmail(NguoiNhanThongBao):
    def __init__(self, email: str):
        self.email = email

    def cap_nhat(self, ten_san_pham: str, gia_moi: float):
        print(
            f" ✉️  [Email gửi tới {self.email}]: '{ten_san_pham}' hiện có giá mới là {gia_moi:,.0f} VNĐ!"
        )


class BoLuuVetLichSu(NguoiNhanThongBao):
    def cap_nhat(self, ten_san_pham: str, gia_moi: float):
        print(f" 📝 [Log Hệ thống]: Đã ghi nhận biến động giá của {ten_san_pham}.")


def main():
    print("--- DEMO OBSERVER DESIGN PATTERN ---")
    iphone = SanPhamTheoDoi("iPhone 15 Pro", 28_000_000)

    user1 = KhachHangEmail("thoai@gmail.com")
    logger = BoLuuVetLichSu()

    # Đăng ký nhận thông báo
    iphone.dang_ky(user1)
    iphone.dang_ky(logger)

    # Kích hoạt sự kiện thay đổi giá
    iphone.thay_doi_gia(25_500_000)


if __name__ == "__main__":
    main()
