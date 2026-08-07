from collections import UserString


class ChuoiBaoMat(UserString):
    """Lớp quản lý chuỗi tự động che giấu thông tin nhạy cảm khi hiển thị"""

    def an_danh(self, ky_tu_thay_the: str = "*") -> str:
        """Che tất cả ký tự trừ 2 ký tự đầu và 2 ký tự cuối"""
        if len(self.data) <= 4:
            return ky_tu_thay_the * len(self.data)
        return self.data[:2] + (ky_tu_thay_the * (len(self.data) - 4)) + self.data[-2:]

    def dem_tu(self) -> int:
        """Đếm số từ trong chuỗi"""
        return len(self.data.split())


def main():
    print("--- DEMO TÙY BIẾN CHUỖI VỚI USERSTRING ---")

    s1 = ChuoiBaoMat("nguyenlehuuthoai2506@gmail.com")
    print(f"Chuỗi gốc: {s1}")
    print(f"Chuỗi sau khi che thông tin: {s1.an_danh()}")
    print(f"Số từ trong chuỗi: {s1.dem_tu()}")

    # Các thao tác chuỗi thông thường vẫn hoạt động bình thường
    s2 = s1 + " [ĐÃ XÁC THỰC]"
    print(f"Chuỗi sau khi cộng: {s2}")


if __name__ == "__main__":
    main()
