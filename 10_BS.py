def tim_kiem_nhi_phan(danh_sach, muc_tieu):
    """
    Tìm kiếm vị trí của muc_tieu trong danh_sach đã được sắp xếp.
    Trả về vị trí (index) nếu tìm thấy, ngược lại trả về -1.
    """
    trai = 0
    phai = len(danh_sach) - 1
    buoc_dem = 0

    while trai <= phai:
        buoc_dem += 1
        giua = (trai + phai) // 2
        gia_tri_giua = danh_sach[giua]

        print(
            f" Bước {buoc_dem}: Xét đoạn từ chỉ số {trai} đến {phai} -> Phần tử giữa là tại chỉ số {giua} ({gia_tri_giua})"
        )

        if gia_tri_giua == muc_tieu:
            return giua, buoc_dem
        elif gia_tri_giua < muc_tieu:
            trai = giua + 1  # Bỏ nửa bên trái
        else:
            phai = giua - 1  # Bỏ nửa bên phải

    return -1, buoc_dem


def main():
    # Mảng bắt buộc phải được sắp xếp trước khi tìm kiếm nhị phân
    mang_so_nguyen = [3, 7, 12, 19, 24, 33, 45, 57, 70, 83, 91, 100]
    muc_tieu = 70

    print("--- THỬ NGHIỆM THUẬT TOÁN TÌM KIẾM NHỊ PHÂN ---")
    print(f"Mảng đầu vào (đã sắp xếp): {mang_so_nguyen}")
    print(f"Số cần tìm: {muc_tieu}\n")

    vi_tri, so_buoc = tim_kiem_nhi_phan(mang_so_nguyen, muc_tieu)

    print("\n--- KẾT QUẢ ---")
    if vi_tri != -1:
        print(
            f"Tìm thấy số {muc_tieu} tại vị trí index {vi_tri} sau {so_buoc} bước duyệt."
        )
    else:
        print(f"Không tìm thấy số {muc_tieu} trong mảng sau {so_buoc} bước duyệt.")


if __name__ == "__main__":
    main()
