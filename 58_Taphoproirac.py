class DisjointSetUnion:
    """Cấu trúc dữ liệu DSU (Union-Find)"""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        """Tìm gốc của phần tử i (có Path Compression)"""
        if self.parent[i] == i:
            return i
        # Gán trực tiếp nút cha về gốc để thu ngắn đường đi
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x: int, y: int) -> bool:
        """Gộp 2 tập hợp chứa x và y. Trả về False nếu x và y đã chung tập hợp (phát hiện chu trình)"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Đã thuộc cùng tập hợp -> Tạo thành chu trình!

        # Tối ưu Union by Rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def main():
    print("--- DEMO DISJOINT SET UNION (DSU) PHÁT HIỆN CHU TRÌNH ---")
    num_nodes = 4
    dsu = DisjointSetUnion(num_nodes)

    # Danh sách các cạnh trong đồ thị: (u, v)
    danh_sach_canh = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    ]  # 0-1-2-3-0 tạo thành hình vuông đóng kín

    print(f"Kiểm tra danh sách cạnh: {danh_sach_canh}\n")
    for u, v in danh_sach_canh:
        thanh_cong = dsu.union(u, v)
        if not thanh_cong:
            print(f"⚠️ Phát hiện CHU TRÌNH tại cạnh ({u} - {v})!")
            break
        else:
            print(f"✅ Đã thêm cạnh ({u} - {v}) thành công.")


if __name__ == "__main__":
    main()
