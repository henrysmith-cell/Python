def doc_chuoi_so_le(gioi_han: int):
    """Generator con 1: Sinh danh sách số lẻ"""
    for i in range(1, gioi_han + 1, 2):
        yield i


def doc_chuoi_so_chan(gioi_han: int):
    """Generator con 2: Sinh danh sách số chẵn"""
    for i in range(2, gioi_han + 1, 2):
        yield i


def tong_hop_du_lieu(max_val: int):
    """Generator cha: Dùng 'yield from' để gom kết quả từ các generator con"""
    print("--- Bắt đầu đọc Số Lẻ ---")
    yield from doc_chuoi_so_le(max_val)  # Ủy quyền cho doc_chuoi_so_le

    print("\n--- Bắt đầu đọc Số Chẵn ---")
    yield from doc_chuoi_so_chan(max_val)  # Ủy quyền cho doc_chuoi_so_chan


def main():
    print("--- DEMO KỸ THUẬT YIELD FROM TRONG PYTHON GENERATOR ---")

    # Gọi generator tổng hợp
    stream_du_lieu = tong_hop_du_lieu(6)

    # Duyệt qua từng phần tử mà không cần tạo mảng phụ trong bộ nhớ
    for gia_tri in stream_du_lieu:
        print(f" > Nhận giá trị: {gia_tri}")


if __name__ == "__main__":
    main()
