def bai_toan_bao_lo_01(suc_chua, trong_luong, gia_tri, n):
    """
    Giải bài toán Balo 0/1 bằng Bảng Quy hoạch động (DP Table)
    - suc_chua: Trọng lượng tối đa balo có thể chứa
    - trong_luong: Danh sách trọng lượng các vật phẩm
    - gia_tri: Danh sách giá trị tương ứng của các vật phẩm
    - n: Số lượng vật phẩm
    """
    # Khởi tạo bảng K kích thước (n+1) x (suc_chua+1) với các giá trị 0
    K = [[0 for _ in range(suc_chua + 1)] for _ in range(n + 1)]

    # Xây dựng bảng Quy hoạch động theo từ dưới lên (Bottom-up)
    for i in range(n + 1):
        for w in range(suc_chua + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif trong_luong[i - 1] <= w:
                # Chọn giá trị lớn nhất giữa: (Chọn vật phẩm i) hoặc (Không chọn vật phẩm i)
                K[i][w] = max(
                    gia_tri[i - 1] + K[i - 1][w - trong_luong[i - 1]], K[i - 1][w]
                )
            else:
                K[i][w] = K[i - 1][w]

    return K[n][suc_chua]


def main():
    gia_tri = [60, 100, 120]
    trong_luong = [10, 20, 30]
    suc_chua_balo = 50
    n = len(gia_tri)

    print("--- QUY HOẠCH ĐỘNG: BÀI TOÁN BALO 0/1 ---")
    print(f"Trọng lượng các vật phẩm : {trong_luong}")
    print(f"Giá trị tương ứng        : {gia_tri}")
    print(f"Sức chứa tối đa của Balo : {suc_chua_balo} kg")

    gt_toi_da = bai_toan_bao_lo_01(suc_chua_balo, trong_luong, gia_tri, n)
    print(f"\n -> Tổng giá trị lớn nhất có thể lấy được: {gt_toi_da}")


if __name__ == "__main__":
    main()
