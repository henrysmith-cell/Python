from collections import deque


class DoThi:
    """Biểu diễn đồ thị vô hướng bằng Danh sách kề (Adjacency List)"""

    def __init__(self):
        self.danh_sach_ke = {}

    def them_canh(self, u, v):
        """Thêm cạnh nối giữa 2 đỉnh u và v"""
        if u not in self.danh_sach_ke:
            self.danh_sach_ke[u] = []
        if v not in self.danh_sach_ke:
            self.danh_sach_ke[v] = []

        self.danh_sach_ke[u].append(v)
        self.danh_sach_ke[v].append(u)

    def duyet_bfs(self, dinh_bat_dau):
        """Thuật toán BFS sử dụng Hang đợi (Queue)"""
        da_tham = set()
        hang_doi = deque([dinh_bat_dau])
        da_tham.add(dinh_bat_dau)

        ket_qua_duyet = []

        while hang_doi:
            dinh_hien_tai = hang_doi.popleft()  # Lấy phần tử đầu hàng đợi
            ket_qua_duyet.append(dinh_hien_tai)

            # Duyệt qua tất cả các hàng xóm kề với đỉnh hiện tại
            for hang_xom in self.danh_sach_ke.get(dinh_hien_tai, []):
                if hang_xom not in da_tham:
                    da_tham.add(hang_xom)
                    hang_doi.append(hang_xom)

        return ket_qua_duyet


def main():
    # Khởi tạo mô hình mạng xã hội thu nhỏ (đỉnh là tên người, cạnh là quan hệ bạn bè)
    graph = DoThi()
    graph.them_canh("An", "Bình")
    graph.them_canh("An", "Cường")
    graph.them_canh("Bình", "Dũng")
    graph.them_canh("Cường", "Giang")
    graph.them_canh("Dũng", "Hoa")

    print("--- THUẬT TOÁN DUYỆT ĐỒ THỊ BFS (BREADTH-FIRST SEARCH) ---")
    dinh_xuat_phat = "An"
    thu_tu_duyet = graph.duyet_bfs(dinh_xuat_phat)

    print(f"Thứ tự lan truyền/duyet từ nút '{dinh_xuat_phat}':")
    print(" -> ".join(thu_tu_duyet))


if __name__ == "__main__":
    main()
