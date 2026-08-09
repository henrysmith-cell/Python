import heapq


def manhattan_distance(p1, p2):
    """Hàm Heuristic h(n): Khoảng cách Manhattan trên lưới 2D"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def a_star_search(luoi, start, goal):
    hangs = len(luoi)
    cots = len(luoi[0])

    # Priority Queue lưu tuple: (f_score, g_score, (r, c))
    pq = [(manhattan_distance(start, goal), 0, start)]
    g_score = {start: 0}
    huong_di = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, Xuống, Trái, Phải

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal:
            return g  # Trả về chi phí đường đi ngắn nhất

        for dr, dc in huong_di:
            neighbor = (current[0] + dr, current[1] + dc)
            r, c = neighbor

            # Kiểm tra vị trí hợp lệ trong lưới và không phải tường (1)
            if 0 <= r < hangs and 0 <= c < cots and luoi[r][c] == 0:
                tentative_g = g + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + manhattan_distance(neighbor, goal)
                    heapq.heappush(pq, (f_score, tentative_g, neighbor))

    return -1  # Không tìm thấy đường đi


def main():
    print("--- DEMO THUẬT TOÁN A* SEARCH ---")
    # Lưới 2D: 0 là đường đi, 1 là chướng ngại vật
    luoi_map = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (4, 4)

    chi_phi = a_star_search(luoi_map, start, goal)
    print(f"Chi phí đường đi ngắn nhất từ {start} tới {goal} bằng A*: {chi_phi} bước.")


if __name__ == "__main__":
    main()
