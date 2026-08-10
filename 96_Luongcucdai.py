from collections import deque


class LuongCucDai:
    def __init__(self, so_dinh: int):
        self.V = so_dinh
        # Đồ thị lưu sức chứa residual capacity
        self.graph = [[0] * so_dinh for _ in range(so_dinh)]

    def them_canh(self, u: int, v: int, suc_chua: int):
        self.graph[u][v] = suc_chua

    def _bfs(self, s: int, t: int, parent: list) -> bool:
        """Tìm đường tăng luồng từ s đến t bằng BFS"""
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v in range(self.V):
                # Nếu v chưa thăm và đường truyền còn sức chứa dư > 0
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, source: int, sink: int) -> int:
        parent = [-1] * self.V
        max_flow = 0

        # Lặp lại chừng nào còn đường tăng luồng từ source đến sink
        while self._bfs(source, sink, parent):
            # Tìm sức chứa dư nhỏ nhất trên đường vừa tìm được
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Cập nhật sức chứa dư của các cạnh và cạnh ngược
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


def main():
    print("--- DEMO THUẬT TOÁN FORD-FULKERSON (MAX FLOW) ---")
    g = LuongCucDai(6)
    # Nguồn s = 0, Đích t = 5
    g.them_canh(0, 1, 16)
    g.them_canh(0, 2, 13)
    g.them_canh(1, 2, 10)
    g.them_canh(1, 3, 12)
    g.them_canh(2, 1, 4)
    g.them_canh(2, 4, 14)
    g.them_canh(3, 2, 9)
    g.them_canh(3, 5, 20)
    g.them_canh(4, 3, 7)
    g.them_canh(4, 5, 4)

    luong_toi_da = g.ford_fulkerson(0, 5)
    print(f"Luồng cực đại truyền từ Nguồn (0) đến Đích (5) là: {luong_toi_da}")


if __name__ == "__main__":
    main()
