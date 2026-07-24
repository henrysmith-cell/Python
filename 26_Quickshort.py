def quick_sort(danh_sach):
    """
    Thuật toán Quick Sort đệ quy chia để trị:
    1. Chọn một phần tử làm chốt (Pivot)
    2. Phân chia mảng thành 3 phần: nhỏ hơn Pivot, bằng Pivot, lớn hơn Pivot
    3. Đệ quy sắp xếp 2 mảng con
    """
    # Điều kiện dừng đệ quy: mảng có 0 hoặc 1 phần tử thì nghiễm nhiên đã sắp xếp
    if len(danh_sach) <= 1:
        return danh_sach

    # Chọn phần tử ở giữa làm Pivot
    pivot = danh_sach[len(danh_sach) // 2]

    # Tách mảng dựa trên Pivot bằng List Comprehension
    trai = [x for x in danh_sach if x < pivot]
    giua = [x for x in danh_sach if x == pivot]
    phai = [x for x in danh_sach if x > pivot]

    # Đệ quy và ghép kết quả
    return quick_sort(trai) + giua + quick_sort(phai)


def main():
    mang_so = [38, 27, 43, 3, 9, 82, 10, 19, 50, 3]
    print("--- THUẬT TOÁN SẮP XẾP NHANH (QUICK SORT) ---")
    print(f"Mảng ban đầu (chưa sắp xếp) : {mang_so}")

    mang_da_sap_xep = quick_sort(mang_so)
    print(f"Mảng sau khi sắp xếp (tăng dần): {mang_da_sap_xep}")


if __name__ == "__main__":
    main()
