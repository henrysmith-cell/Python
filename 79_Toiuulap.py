import itertools


def main():
    print("--- DEMO MODULE ITERTOOLS TRONG PYTHON ---")

    # 1. itertools.chain: Nối nhiều Iterable thành một chuỗi duy nhất mà không tốn RAM tạo list mới
    danh_sach_1 = [1, 2, 3]
    danh_sach_2 = ["a", "b", "c"]
    chuoi_gop = itertools.chain(danh_sach_1, danh_sach_2)
    print(f"1. Nối chuỗi bằng chain(): {list(chuoi_gop)}")

    # 2. itertools.combinations: Sinh tất cả các tổ hợp chập K của tập hợp
    tap_hop = ["A", "B", "C", "D"]
    to_hop = list(itertools.combinations(tap_hop, 2))
    print(f"\n2. Tổ hợp chập 2 của {tap_hop}:")
    print(f"   {to_hop}")

    # 3. itertools.groupby: Gom nhóm các phần tử liên tiếp theo tiêu chí (cần sort trước)
    du_lieu = [("HN", "Nam"), ("HN", "Linh"), ("SG", "An"), ("SG", "Bình")]
    print("\n3. Gom nhóm dữ liệu theo Thành phố (groupby):")
    for thanh_pho, nhom in itertools.groupby(du_lieu, key=lambda x: x[0]):
        ten_cac_ban = [item[1] for item in nhom]
        print(f"   - {thanh_pho}: {ten_cac_ban}")


if __name__ == "__main__":
    main()
