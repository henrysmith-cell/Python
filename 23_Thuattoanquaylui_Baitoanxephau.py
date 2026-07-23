def an_toan(ban_co, dong, cot, n):
    """Kiểm tra xem đặt quân Hậu tại vị trí (dong, cot) có bị quân nào khác ăn không"""
    # Kiểm tra cột dọc phía trên
    for i in range(dong):
        if ban_co[i][cot] == 1:
            return False

    # Kiểm tra đường chéo trái phía trên
    for i, j in zip(range(dong - 1, -1, -1), range(cot - 1, -1, -1)):
        if ban_co[i][j] == 1:
            return False

    # Kiểm tra đường chéo phải phía trên
    for i, j in zip(range(dong - 1, -1, -1), range(cot + 1, n)):
        if ban_co[i][j] == 1:
            return False

    return True


def gia_i_n_queens(ban_co, dong, n, loi_giai):
    """Hàm đệ quy quay lui để tìm tất cả cách đặt quân Hậu"""
    if dong >= n:
        # Đã đặt thành công N quân Hậu -> Lưu lại lời giải
        loi_giai.append([hang[:] for hang in ban_co])
        return

    for cot in range(n):
        if an_toan(ban_co, dong, cot, n):
            ban_co[dong][cot] = 1  # Thử đặt quân Hậu

            gia_i_n_queens(ban_co, dong + 1, n, loi_giai)  # Đệ quy dòng tiếp theo

            ban_co[dong][
                cot
            ] = 0  # Quay lui (Backtrack) - gỡ quân Hậu ra để thử cột khác


def in_ban_co(ban_co):
    for hang in ban_co:
        print(" ".join(["Q" if x == 1 else "." for x in hang]))
    print()


def main():
    N = 4  # Bàn cờ 4x4
    ban_co = [[0 for _ in range(N)] for _ in range(N)]
    cac_loi_giai = []

    print(f"--- BÀI TOÁN {N} QUÂN HẬU (BACKTRACKING) ---")
    gia_i_n_queens(ban_co, 0, N, cac_loi_giai)

    print(f"Tìm thấy tổng cộng {len(cac_loi_giai)} cách xếp hợp lệ:\n")
    for idx, lg in enumerate(cac_loi_giai, 1):
        print(f"Cách {idx}:")
        in_ban_co(lg)


if __name__ == "__main__":
    main()
