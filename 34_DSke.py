from collections import defaultdict


class DoThi:
    """Biểu diễn Đồ thị vô hướng bằng Adjacency List"""

    def __init__(self):
        # Mặc định mỗi đỉnh sẽ chứa một danh sách (list) các đỉnh kề với nó
        self.danh_sach_ke = defaultdict(list)

    def them_canh(self, u, v):
        """Thêm cạnh nối giữa 2 đỉnh u và v (Đồ thị 2 chiều)"""
        self.danh_sach_ke[u].append(v)
        self.danh_sach_ke[v].append(u)

    def hien_thi(self):
        print("--- DANH SÁCH KỀ CỦA ĐỒ THỊ ---")
        for dinh, danh_sach in self.danh_sach_ke.items():
            cac_dinh_ke = ", ".join(map(str, danh_sach))
            print(f" Đỉnh [{dinh}] nối với -> {cac_dinh_ke}")


def main():
    g = DoThi()
    # Giả lập mạng xã hội (Cạnh giữa 2 người = Bạn bè của nhau)
    g.them_canh("An", "Bình")
    g.them_canh("An", "Cường")
    g.them_canh("Bình", "Dũng")
    g.them_canh("Cường", "Dũng")
    g.them_canh("Cường", "Giang")

    g.hien_thi()


if __name__ == "__main__":
    main()
