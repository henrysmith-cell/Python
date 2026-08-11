from collections import deque


class MinCostMaxFlow:
    def __init__(self, so_dinh: int):
        self.V = so_dinh
        self.capacity = [[0] * so_dinh for _ in range(so_dinh)]
        self.cost = [[0] * so_dinh for _ in range(so_dinh)]
        self.adj = [[] for _ in range(so_dinh)]

    def them_canh(self, u: int, v: int, cap: int, c: int):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.capacity[u][v] = cap
        self.cost[u][v] = c
        self.cost[v][u] = -c  # Cạnh ngược có chi phí âm

    def _spfa(self, s: int, t: int, parent: list, dist: list) -> bool:
        """Tìm đường đi có chi phí thấp nhất bằng thuật toán SPFA"""
        for i in range(self.V):
            dist[i] = float("inf")
        in_queue = [False] * self.V
        queue = deque([s])
        dist[s] = 0
        in_queue[s] = True

        while queue:
            u = queue.popleft()
            in_queue[u] = False

            for v in self.adj[u]:
                # Nếu còn sức chứa thặng dư và tìm thấy đường đi chi phí rẻ hơn
                if self.capacity[u][v] > 0 and dist[v] > dist[u] + self.cost[u][v]:
                    dist[v] = dist[u] + self.cost[u][v]
                    parent[v] = u
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True

        return dist[t] != float("inf")

    def tinh_mcmf(self, source: int, sink: int) -> tuple[int, int]:
        parent = [-1] * self.V
        dist = [0] * self.V
        max_flow = 0
        min_cost = 0

        while self._spfa(source, sink, parent, dist):
            # 1. Tìm luồng có thể tăng thêm nhỏ nhất trên đường đi
            push_flow = float("inf")
            curr = sink
            while curr != source:
                p = parent[curr]
                push_flow = min(push_flow, self.capacity[p][curr])
                curr = p

            # 2. Cập nhật luồng, chi phí và sức chứa thặng dư
            curr = sink
            while curr != source:
                p = parent[curr]
                self.capacity[p][curr] -= push_flow
                self.capacity[curr][p] += push_flow
                min_cost += push_flow * self.cost[p][curr]
                curr = p

            max_flow += push_flow

        return max_flow, min_cost


def main():
    print("--- DEMO THUẬT TOÁN MIN-COST MAX-FLOW (MCMF) ---")
    g = MinCostMaxFlow(4)

    # them_canh(u, v, capacity, cost)
    g.them_canh(0, 1, 2, 4)  # Nguồn 0 -> 1: Sức chứa 2, Chi phí 4/đơn vị
    g.them_canh(0, 2, 3, 1)  # Nguồn 0 -> 2: Sức chứa 3, Chi phí 1/đơn vị
    g.them_canh(1, 3, 2, 2)  # 1 -> Đích 3: Sức chứa 2, Chi phí 2/đơn vị
    g.them_canh(2, 3, 1, 6)  # 2 -> Đích 3: Sức chứa 1, Chi phí 6/đơn vị
    g.them_canh(2, 1, 1, 1)  # Cầu nối 2 -> 1: Sức chứa 1, Chi phí 1/đơn vị

    source, sink = 0, 3
    luong_toi_da, chi_phi_toi_thieu = g.tinh_mcmf(source, sink)

    print(f"Luồng cực đại (Max Flow) chuyển từ {source} -> {sink}: {luong_toi_da}")
    print(f"Tổng chi phí tối thiểu (Min Cost) tương ứng: {chi_phi_toi_thieu}")


if __name__ == "__main__":
    main()
