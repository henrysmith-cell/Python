def hien_thi_menu():
    print("\n=== ỨNG DỤNG QUẢN LÝ CÔNG VIỆC ===")
    print("1. Xem danh sách công việc")
    print("2. Thêm công việc mới")
    print("3. Đánh dấu hoàn thành")
    print("4. Xóa công việc")
    print("5. Thoát")


def xem_danh_sach(danh_sach):
    if not danh_sach:
        print("\n[Thông báo] Danh sách trống. Hãy thêm công việc nhé!")
        return
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for i, cv in enumerate(danh_sach, 1):
        trang_thai = "✓ Đã xong" if cv["hoan_thanh"] else "✗ Chưa làm"
        print(f"{i}. {cv['ten']} [{trang_thai}]")


def them_cong_viec(danh_sach):
    ten_cv = input("Nhập tên công việc cần thêm: ").strip()
    if ten_cv:
        danh_sach.append({"ten": ten_cv, "hoan_thanh": False})
        print(f"[Thành công] Đã thêm: '{ten_cv}'")
    else:
        print("[Lỗi] Tên công việc không được để trống!")


def hoan_thanh_cong_viec(danh_sach):
    xem_danh_sach(danh_sach)
    if not danh_sach:
        return
    try:
        vi_tri = int(input("Nhập số thứ tự công việc đã hoàn thành: ")) - 1
        if 0 <= vi_tri < len(danh_sach):
            danh_sach[vi_tri]["hoan_thanh"] = True
            print(f"[Thành công] Đã hoàn thành công việc: '{danh_sach[vi_tri]['ten']}'")
        else:
            print("[Lỗi] Số thứ tự không tồn tại!")
    except ValueError:
        print("[Lỗi] Vui lòng nhập một số nguyên hợp lệ!")


def xoa_cong_viec(danh_sach):
    xem_danh_sach(danh_sach)
    if not danh_sach:
        return
    try:
        vi_tri = int(input("Nhập số thứ tự công việc muốn xóa: ")) - 1
        if 0 <= vi_tri < len(danh_sach):
            xoa = danh_sach.pop(vi_tri)
            print(f"[Thành công] Đã xóa công việc: '{xoa['ten']}'")
        else:
            print("[Lỗi] Số thứ tự không tồn tại!")
    except ValueError:
        print("[Lỗi] Vui lòng nhập một số nguyên hợp lệ!")


def main():
    # Sử dụng list chứa các dict để lưu trữ dữ liệu linh hoạt
    danh_sach_cv = [
        {"ten": "Học Python cơ bản", "hoan_thanh": True},
        {"ten": "Luyện tập giải thuật", "hoan_thanh": False},
    ]

    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng (1-5): ").strip()

        if lua_chon == "1":
            xem_danh_sach(danh_sach_cv)
        elif lua_chon == "2":
            them_cong_viec(danh_sach_cv)
        elif lua_chon == "3":
            hoan_thanh_cong_viec(danh_sach_cv)
        elif lua_chon == "4":
            xoa_cong_viec(danh_sach_cv)
        elif lua_chon == "5":
            print("Cảm ơn em đã sử dụng ứng dụng. Chúc một ngày làm việc hiệu quả!")
            break
        else:
            print("[Lỗi] Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 đến 5.")


if __name__ == "__main__":
    main()
