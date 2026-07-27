def tim_kiem_nhi_phan(danh_sach, gia_tri_can_tim):
    """
    Thuật toán Binary Search trên danh sách ĐÃ SẮP XẾP.
    Trả về chỉ số (index) nếu thấy, hoặc -1 nếu không có.
    """
    trai = 0
    phai = len(danh_sach) - 1

    while trai <= phai:
        giua = (trai + phai) // 2  # Lấy chỉ số ở giữa

        # Nếu tìm thấy ngay ở giữa
        if danh_sach[giua] == gia_tri_can_tim:
            return giua
        # Nếu giá trị cần tìm lớn hơn phần tử giữa -> Bỏ nửa bên trái
        elif danh_sach[giua] < gia_tri_can_tim:
            trai = giua + 1
        # Nếu giá trị cần tìm nhỏ hơn phần tử giữa -> Bỏ nửa bên phải
        else:
            phai = giua - 1

    return -1


def main():
    # Danh sách bắt buộc phải được sắp xếp trước
    danh_sach_so = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    can_tim = 23

    print("--- THUẬT TOÁN TÌM KIẾM NHỊ PHÂN (BINARY SEARCH) ---")
    print(f"Danh sách: {danh_sach_so}")
    print(f"Số cần tìm: {can_tim}")

    index = tim_kiem_nhi_phan(danh_sach_so, can_tim)

    if index != -1:
        print(f" -> Tìm thấy {can_tim} tại vị trí (index): {index}")
    else:
        print(f" -> Không tìm thấy {can_tim} trong danh sách.")


if __name__ == "__main__":
    main()
