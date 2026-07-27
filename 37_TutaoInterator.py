class BoDemLui:
    """Class tạo ra một bộ đếm lùi có thể duyệt bằng vòng lặp for"""

    def __init__(self, bat_dau: int):
        self.hien_tai = bat_dau

    def __iter__(self):
        # Trả về chính đối tượng này để bắt đầu quá trình lặp
        return self

    def __next__(self):
        # Nếu đã đếm tới 0 thì dừng vòng lặp
        if self.hien_tai < 1:
            raise StopIteration

        gia_tri = self.hien_tai
        self.hien_tai -= 1
        return gia_tri


def main():
    print("--- CUSTOM ITERATOR TRONG PYTHON ---")
    bo_dem = BoDemLui(bat_dau=5)

    print("Bắt đầu đếm lùi:")
    for so in bo_dem:
        print(f" -> {so}...")
    print("🚀 Bắt đầu!")


if __name__ == "__main__":
    main()
