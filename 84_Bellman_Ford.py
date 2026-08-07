class DoThi:
    def __init__(self, so_dinh: int):
        self.V = so_dinh
        self.danh_sach_canh = []  # Lưu các cạnh dạng (u, v, w)

    def them_canh(self, u: int, v: int, w: int):
        self.danh_sach_canh.append((u, v, w))

    def bellman_ford(self, dinh_nguon: int):
        dist = [float("inf")] * self.V
        dist[dinh_nguon] = 0

        # Lặp V - 1 lần để thực hiện nới cạnh (relaxation)
        for _ in range(self.V - 1):
            for u, v, w in self.danh_sach_canh:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Lần lặp thứ V để kiểm tra chu trình âm
        for u, v, w in self.danh_sach_canh:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print(
                    "⚠️ Đồ thị chứa CHU TRÌNH ÂM! Không thể tính khoảng cách ngắn nhất."
                )
                return None

        return dist


def main():
    print("--- DEMO THUẬT TOÁN BELLMAN-FORD ---")

    # Khởi tạo đồ thị 5 đỉnh (0 đến 4)
    g = DoThi(5)
    g.them_canh(0, 1, -1)
    g.them_canh(0, 2, 4)
    g.them_canh(1, 2, 3)
    g.them_canh(1, 3, 2)
    g.them_canh(1, 4, 2)
    g.them_canh(3, 2, 5)
    g.them_canh(3, 1, 1)
    g.them_canh(4, 3, -3)

    dinh_xuat_phat = 0
    ket_qua = g.bellman_ford(dinh_xuat_phat)

    if ket_qua:
        print(f"Khoảng cách ngắn nhất từ đỉnh {dinh_xuat_phat}:")
        for i in range(len(ket_qua)):
            print(f" - Đến đỉnh {i}: {ket_qua[i]}")


if __name__ == "__main__":
    main()
