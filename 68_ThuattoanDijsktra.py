import heapq


def dijkstra(do_thi: dict, bat_dau: str):
    """
    Thuật toán Dijkstra tìm đường đi ngắn nhất
    do_thi: Dict biểu diễn danh sách kề {u: [(v1, w1), (v2, w2)]}
    """
    khoang_cach = {dinh: float("inf") for dinh in do_thi}
    khoang_cach[bat_dau] = 0

    # Hàng đợi ưu tiên lưu tuple: (khoảng_cách_hiện_tại, đỉnh)
    pq = [(0, bat_dau)]

    while pq:
        kc_hien_tai, u = heapq.heappop(pq)

        # Bỏ qua nếu tìm thấy đường đi tốt hơn trước đó
        if kc_hien_tai > khoang_cach[u]:
            continue

        for v, trong_so in do_thi[u]:
            kc_moi = kc_hien_tai + trong_so
            # Nếu tìm thấy khoảng cách ngắn hơn tới v
            if kc_moi < khoang_cach[v]:
                khoang_cach[v] = kc_moi
                heapq.heappush(pq, (kc_moi, v))

    return khoang_cach


def main():
    print("--- DEMO THUẬT TOÁN DIJKSTRA ---")
    # Biểu diễn bản đồ các thành phố và khoảng cách (km)
    ban_do = {
        "Hà Nội": [("Hải Phòng", 120), ("Đà Nẵng", 750)],
        "Hải Phòng": [("Hà Nội", 120), ("Đà Nẵng", 680)],
        "Đà Nẵng": [("Hà Nội", 750), ("Hải Phòng", 680), ("TP.HCM", 960)],
        "TP.HCM": [("Đà Nẵng", 960)],
    }

    goc = "Hà Nội"
    ket_qua = dijkstra(ban_do, goc)

    print(f"Khoảng cách ngắn nhất xuất phát từ '{goc}':\n")
    for diem_den, km in ket_qua.items():
        print(f" -> Tới {diem_den:<10}: {km} km")


if __name__ == "__main__":
    main()
