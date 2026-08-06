INF = float("inf")


def floyd_warshall(graph):
    """
    graph: Ma trận kề V x V biểu diễn trọng số giữa các đỉnh.
    """
    v_count = len(graph)
    # Khởi tạo bảng khoảng cách dist bằng bảng trọng số ban đầu
    dist = [list(row) for row in graph]

    # Vòng lặp k: Xét từng đỉnh k làm đỉnh trung gian
    for k in range(v_count):
        # Vòng lặp i: Đỉnh xuất phát
        for i in range(v_count):
            # Vòng lặp j: Đỉnh đích
            for j in range(v_count):
                # Nếu đi qua k ngắn hơn đi trực tiếp từ i -> j
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def main():
    print("--- DEMO THUẬT TOÁN FLOYD-WARSHALL ---")

    # Ma trận kề biểu diễn đồ thị 4 đỉnh (0, 1, 2, 3)
    # INF đại diện cho không có đường đi trực tiếp
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]

    dist = floyd_warshall(graph)

    print("Ma trận khoảng cách ngắn nhất giữa mọi cặp đỉnh (i -> j):\n")
    print("      Đỉnh 0  Đỉnh 1  Đỉnh 2  Đỉnh 3")
    for i in range(len(dist)):
        row_str = f"Đỉnh {i}: "
        for j in range(len(dist)):
            val = "INF" if dist[i][j] == INF else f"{dist[i][j]:<4}"
            row_str += f"{val:^8}"
        print(row_str)


if __name__ == "__main__":
    main()
