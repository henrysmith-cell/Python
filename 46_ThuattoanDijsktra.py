import heapq


def dijkstra(do_thi, dinh_bat_dau):
    """
    Tìm quãng đường ngắn nhất từ 'dinh_bat_dau' tới mọi đỉnh trong đồ thị.
    do_thi: Dict dạng { u: [(v, trong_so), ...] }
    """
    # Khởi tạo khoảng cách tới tất cả các đỉnh là vô cùng (infinity)
    khoang_cach = {dinh: float("inf") for dinh in do_thi}
    khoang_cach[dinh_bat_dau] = 0

    # Hàng đợi ưu tiên lưu cặp (khoang_cach_hien_tai, dinh)
    priority_queue = [(0, dinh_bat_dau)]

    while priority_queue:
        kc_hien_tai, dinh_hien_tai = heapq.heappop(priority_queue)

        # Nếu khoảng cách lấy ra lớn hơn khoảng cách đã ghi nhận -> Bỏ qua
        if kc_hien_tai > khoang_cach[dinh_hien_tai]:
            continue

        # Duyệt qua các đỉnh kề
        for dinh_ke, trong_so in do_thi[dinh_hien_tai]:
            kc_moi = kc_hien_tai + trong_so

            # Nếu tìm được đường đi ngắn hơn tới dinh_ke
            if kc_moi < khoang_cach[dinh_ke]:
                khoang_cach[dinh_ke] = kc_moi
                heapq.heappush(priority_queue, (kc_moi, dinh_ke))

    return khoang_cach


def main():
    # Biểu diễn bản đồ các thành phố và khoảng cách (km)
    ban_do = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
    }

    print("--- THUẬT TOÁN DIJKSTRA TÌM ĐƯỜNG ĐI NGẮN NHẤT ---")
    start = "A"
    ket_qua = dijkstra(ban_do, start)

    print(f"Khoảng cách ngắn nhất từ thành phố '{start}':")
    for dinh, kc in ket_qua.items():
        print(f" -> Tới {dinh}: {kc} km")


if __name__ == "__main__":
    main()
