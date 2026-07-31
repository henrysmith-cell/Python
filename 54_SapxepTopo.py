from collections import defaultdict, deque


class DoThiDAG:
    """Đồ thị có hướng không chu trình (DAG)"""

    def __init__(self, so_dinh):
        self.V = so_dinh
        self.do_thi = defaultdict(list)
        self.in_degree = {i: 0 for i in range(so_dinh)}

    def them_canh(self, u, v):
        """Thêm cạnh u -> v (Công việc u phải làm TRƯỚC v)"""
        self.do_thi[u].append(v)
        self.in_degree[v] += 1

    def sap_xep_topo(self):
        """Thuật toán Kahn tìm thứ tự thực hiện hợp lệ"""
        queue = deque([node for node in self.in_degree if self.in_degree[node] == 0])
        thu_tu_topo = []

        while queue:
            u = queue.popleft()
            thu_tu_topo.append(u)

            # Giảm in-degree của các đỉnh kề
            for v in self.do_thi[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)

        # Nếu số lượng đỉnh sắp xếp != tổng số đỉnh -> Đồ thị bị dính chu trình vòng (Lỗi lặp vô tận)
        if len(thu_tu_topo) != self.V:
            return None
        return thu_tu_topo


def main():
    print("--- THUẬT TOÁN SẮP XẾP TOPO (KAHN'S ALGORITHM) ---")
    # Giả lập lộ trình các môn học bắt buộc:
    # 0: Nhập môn Lập trình -> 1: Cấu trúc dữ liệu -> 2: Giải thuật nâng cao -> 3: BTL Tốt nghiệp
    mon_hoc = {0: "Lập trình C", 1: "CTDL & GT", 2: "OOP Python", 3: "Đồ án Tốt nghiệp"}

    g = DoThiDAG(so_dinh=4)
    g.them_canh(0, 1)  # Lập trình C -> CTDL & GT
    g.them_canh(1, 2)  # CTDL & GT -> OOP Python
    g.them_canh(2, 3)  # OOP Python -> Đồ án Tốt nghiệp

    thu_tu = g.sap_xep_topo()
    if thu_tu:
        print("Lộ trình học tập hợp lý theo đúng môn tiên quyết:")
        for idx, m in enumerate(thu_tu, 1):
            print(f" Bước {idx}: {mon_hoc[m]}")
    else:
        print("❌ Lỗi: Có xung đột chu trình giữa các môn học!")


if __name__ == "__main__":
    main()
