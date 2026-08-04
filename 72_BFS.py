from collections import deque


def tim_duong_me_cung(me_cung: list, bat_dau: tuple, dich: tuple):
    """
    me_cung: Ma trận 0 (đường đi) và 1 (vật cản/tường)
    bat_dau: (hàng, cột)
    dich: (hàng, cột)
    """
    hangs = len(me_cung)
    cots = len(me_cung[0])

    # 4 hướng di chuyển: Lên, Xuống, Trái, Phải
    huong_di = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(bat_dau[0], bat_dau[1], 0)])  # (hàng, cột, khoảng_cách)
    da_tham = {bat_dau}

    while queue:
        r, c, buoc = queue.popleft()

        # Nếu đã chạm đích
        if (r, c) == dich:
            return buoc

        # Thử đi qua 4 hướng kề bên
        for dr, dc in huong_di:
            nr, nc = r + dr, c + dc

            # Kiểm tra vị trí mới hợp lệ: trong ma trận, không phải tường (1) và chưa tham
            if 0 <= nr < hangs and 0 <= nc < cots:
                if me_cung[nr][nc] == 0 and (nr, nc) not in da_tham:
                    da_tham.add((nr, nc))
                    queue.append((nr, nc, buoc + 1))

    return -1  # Không tìm thấy đường đi


def main():
    print("--- DEMO THUẬT TOÁN BFS TÌM ĐƯỜNG MÊ CUNG ---")
    # 0 là đường đi, 1 là tường cản
    me_cung = [[0, 0, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0]]
    diem_start = (0, 0)
    diem_end = (3, 3)

    so_buoc = tim_duong_me_cung(me_cung, diem_start, diem_end)
    print(f"Mê cung kích thước {len(me_cung)}x{len(me_cung[0])}")
    if so_buoc != -1:
        print(
            f"✅ Đường đi ngắn nhất từ {diem_start} tới {diem_end} mất: {so_buoc} bước!"
        )
    else:
        print(f"❌ KHÔNG thể di chuyển tới đích!")


if __name__ == "__main__":
    main()
