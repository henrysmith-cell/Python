def tim_tat_ca_tap_con(mang_so):
    """
    Thuật toán Backtracking tìm toàn bộ các tập hợp con (Power Set).
    Ví dụ: [1, 2] -> [], [1], [2], [1, 2]
    """
    ket_qua = []

    def backtrack(index_hien_tai, tap_con_hien_tai):
        # Lưu lại một bản sao của tập con hiện tại vào kết quả
        ket_qua.append(list(tap_con_hien_tai))

        # Duyệt qua các phần tử tiếp theo
        for i in range(index_hien_tai, len(mang_so)):
            # 1. Chọn phần tử mang_so[i]
            tap_con_hien_tai.append(mang_so[i])

            # 2. Đệ quy đi tiếp tới các phần tử sau
            backtrack(i + 1, tap_con_hien_tai)

            # 3. Backtrack (Bỏ phần tử vừa chọn để thử phương án khác)
            tap_con_hien_tai.pop()

    backtrack(0, [])
    return ket_qua


def main():
    tap_goc = [1, 2, 3]
    print("--- THUẬT TOÁN BACKTRACKING: TIM TẬP CON ---")
    print(f"Tập hợp gốc: {tap_goc}")

    cac_tap_con = tim_tat_ca_tap_con(tap_goc)
    print(f"\nTổng số tập con tìm được: {len(cac_tap_con)}")
    for idx, tc in enumerate(cac_tap_con, 1):
        print(f" Tập {idx:<2}: {tc}")


if __name__ == "__main__":
    main()
