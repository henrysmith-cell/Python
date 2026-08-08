class DoThiTarjan:
    def __init__(self, so_dinh: int):
        self.V = so_dinh
        self.adj = [[] for _ in range(so_dinh)]
        self.Time = 0

    def them_canh(self, u: int, v: int):
        self.adj[u].append(v)

    def _scc_util(self, u, disc, low, stack, in_stack, scc_list):
        disc[u] = low[u] = self.Time
        self.Time += 1
        stack.append(u)
        in_stack[u] = True

        for v in self.adj[u]:
            if disc[v] == -1:  # Nếu v chưa được thăm
                self._scc_util(v, disc, low, stack, in_stack, scc_list)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:  # Nếu v đang nằm trong Stack
                low[u] = min(low[u], disc[v])

        # Nếu u là đỉnh gốc của SCC
        if low[u] == disc[u]:
            scc = []
            while True:
                w = stack.pop()
                in_stack[w] = False
                scc.append(w)
                if w == u:
                    break
            scc_list.append(scc)

    def tim_scc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        in_stack = [False] * self.V
        stack = []
        scc_list = []

        for i in range(self.V):
            if disc[i] == -1:
                self._scc_util(i, disc, low, stack, in_stack, scc_list)

        return scc_list


def main():
    print("--- DEMO THUẬT TOÁN TARJAN (TÌM SCC) ---")
    g = DoThiTarjan(5)
    g.them_canh(1, 0)
    g.them_canh(0, 2)
    g.them_canh(2, 1)
    g.them_canh(0, 3)
    g.them_canh(3, 4)

    cac_scc = g.tim_scc()
    print("Các Thành phần Liên thông Mạnh (SCC) tìm được:")
    for idx, scc in enumerate(cac_scc, 1):
        print(f" - SCC #{idx}: {scc}")


if __name__ == "__main__":
    main()
