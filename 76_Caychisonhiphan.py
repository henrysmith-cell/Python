class FenwickTree:
    """Binary Indexed Tree (BIT) hỗ trợ cập nhật và tính tổng tiền tố O(log N)"""

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, val: int):
        """Thêm giá trị 'val' vào vị trí 'index' (chỉ số tính từ 1)"""
        while index <= self.size:
            self.tree[index] += val
            # LSB (Least Significant Bit): index += (index & -index)
            index += index & (-index)

    def query(self, index: int) -> int:
        """Tính tổng tiền tố từ vị trí 1 tới 'index'"""
        tong = 0
        while index > 0:
            tong += self.tree[index]
            index -= index & (-index)
        return tong

    def query_range(self, left: int, right: int) -> int:
        """Tính tổng đoạn từ 'left' tới 'right'"""
        return self.query(right) - self.query(left - 1)


def main():
    print("--- DEMO CẤU TRÚC DỮ LIỆU FENWICK TREE (BIT) ---")
    mang_goc = [3, 2, -1, 6, 5, 4, -3, 3]
    n = len(mang_goc)

    bit = FenwickTree(n)
    # Khởi tạo cây
    for i, val in enumerate(mang_goc, 1):
        bit.update(i, val)

    print(f"Mảng dữ liệu ban đầu: {mang_goc}")

    # 1. Truy vấn tổng đoạn [2..5] (tương ứng vị trí từ 2 tới 5)
    tong_2_5 = bit.query_range(2, 5)
    print(f"Tổng đoạn từ vị trí 2 tới 5: {tong_2_5}")

    # 2. Cập nhật phần tử tại vị trí 3 tăng thêm 6 đơn vị
    print("\nCập nhật phần tử vị trí 3 tăng thêm +6...")
    bit.update(3, 6)

    # 3. Tính lại tổng đoạn [2..5]
    tong_moi = bit.query_range(2, 5)
    print(f"Tổng đoạn từ vị trí 2 tới 5 sau khi cập nhật: {tong_moi}")


if __name__ == "__main__":
    main()
