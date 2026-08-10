import sys
from array import array


def main():
    print("--- DEMO TỐI ƯU BỘ NHỚ BẰNG MODULE ARRAY ---")

    so_luong = 1_000_000

    # 1. Tạo danh sách List thông thường (Mã kiểu Object)
    list_so = list(range(so_luong))
    ram_list = sys.getsizeof(list_so) / (1024 * 1024)

    # 2. Tạo mảng Array kiểu số nguyên 4-bytes ('i')
    array_so = array("i", range(so_luong))
    ram_array = sys.getsizeof(array_so) / (1024 * 1024)

    print(f"Dung lượng RAM cho {so_luong:,} số nguyên:")
    print(f" - Dùng List tiêu chuẩn: {ram_list:.2f} MB")
    print(f" - Dùng Module Array : {ram_array:.2f} MB")

    tiet_kiem = ((ram_list - ram_array) / ram_list) * 100
    print(f"👉 Tiết kiệm được ~{tiet_kiem:.1f}% bộ nhớ RAM!")


if __name__ == "__main__":
    main()
