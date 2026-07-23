import sys


def tao_danh_sach_thuong(n):
    """Tạo List thông thường - Nạp toàn bộ dữ liệu vào RAM"""
    ket_qua = []
    for i in range(n):
        ket_qua.append(i**2)
    return ket_qua


def tao_generator_binh_phuong(n):
    """
    Sử dụng Generator với từ khóa 'yield'.
    Mỗi lần gọi chỉ tính đúng 1 số và trả về, không tốn RAM lưu trữ toàn bộ!
    """
    for i in range(n):
        yield i**2


def main():
    SO_LUONG = 1_000_000
    print(f"--- SO SÁNH BỘ NHỚ RAM ({SO_LUONG:,} phần tử) ---")

    # 1. Đo dung lượng List
    danh_sach_list = tao_danh_sach_thuong(SO_LUONG)
    dung_luong_list = sys.getsizeof(danh_sach_list)
    print(
        f"1. Dung lượng RAM của List      : {dung_luong_list:,} bytes (~{dung_luong_list / (1024*1024):.2f} MB)"
    )

    # 2. Đo dung lượng Generator
    gen_object = tao_generator_binh_phuong(SO_LUONG)
    dung_luong_gen = sys.getsizeof(gen_object)
    print(f"2. Dung lượng RAM của Generator : {dung_luong_gen:,} bytes")

    print(
        f"\n => Generator tiết kiệm gấp ~{dung_luong_list // dung_luong_gen:,} lần bộ nhớ!"
    )

    # Duyệt qua Generator như một danh sách bình thường
    print("\nDuyệt 5 phần tử đầu tiên từ Generator:")
    for idx, val in enumerate(gen_object):
        if idx >= 5:
            break
        print(f" - Phần tử {idx}: {val}")


if __name__ == "__main__":
    main()
