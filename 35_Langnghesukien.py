from abc import ABC, abstractmethod


# 1. Interface cho Observer (Người nhận thông báo)
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


# 2. Subject (Kênh phát tin tức)
class KenhTinTuc:
    def __init__(self, ten_kenh: str):
        self.ten_kenh = ten_kenh
        self._doc_gia = []

    def dang_ky(self, observer: Observer):
        """Thêm người theo dõi"""
        self._doc_gia.append(observer)

    def huy_dang_ky(self, observer: Observer):
        """Xóa người theo dõi"""
        self._doc_gia.remove(observer)

    def phat_ban_tin(self, tin_tuc: str):
        """Phát tin nhắn tới TOÀN BỘ độc giả đã đăng ký"""
        print(f"\n[{self.ten_kenh}] PHÁT TIN MỚI: {tin_tuc}")
        for doc_gia in self._doc_gia:
            doc_gia.update(f"[{self.ten_kenh}] -> {tin_tuc}")


# 3. Các Observers thực tế
class NguoiDungApp(Observer):
    def __init__(self, ten: str):
        self.ten = ten

    def update(self, message: str):
        print(f" -> Push Notification tới máy của {self.ten}: '{message}'")


def main():
    print("--- DEMO OBSERVER DESIGN PATTERN ---")
    kenh_cong_nghe = KenhTinTuc("Kênh Công Nghệ 24h")

    user_a = NguoiDungApp("Thoại")
    user_b = NguoiDungApp("Minh")

    # Đăng ký theo dõi
    kenh_cong_nghe.dang_ky(user_a)
    kenh_cong_nghe.dang_ky(user_b)

    # Phát tin lần 1
    kenh_cong_nghe.phat_ban_tin("Python ra mắt phiên bản mới!")

    # User B hủy theo dõi
    kenh_cong_nghe.huy_dang_ky(user_b)

    # Phát tin lần 2 (Chỉ User A nhận được)
    kenh_cong_nghe.phat_ban_tin("AI thế hệ mới đạt cột mốc ấn tượng.")


if __name__ == "__main__":
    main()
