class NodeTrie:
    def __init__(self):
        self.cac_con = {}  # Map lưu các ký tự con
        self.la_ket_thuc_tu = False  # Đánh dấu có phải kết thúc một từ hợp lệ không


class CayTrie:
    """Cấu trúc dữ liệu Cây tiền tố (Prefix Tree)"""

    def __init__(self):
        self.root = NodeTrie()

    def them_tu(self, tu: str):
        """Thêm một từ vào cây Trie"""
        node = self.root
        for ky_tu in tu.lower():
            if ky_tu not in node.cac_con:
                node.cac_con[ky_tu] = NodeTrie()
            node = node.cac_con[ky_tu]
        node.la_ket_thuc_tu = True

    def kiem_tra_tien_to(self, tien_to: str) -> bool:
        """Kiểm tra xem có từ nào bắt đầu bằng 'tien_to' hay không"""
        node = self.root
        for ky_tu in tien_to.lower():
            if ky_tu not in node.cac_con:
                return False
            node = node.cac_con[ky_tu]
        return True


def main():
    print("--- CẤU TRÚC DỮ LIỆU TRIE (PREFIX TREE) ---")
    trie = CayTrie()

    # Thêm danh sách từ vựng vào cây
    danh_sach_tu = ["python", "pyramid", "pytorch", "java", "javascript"]
    for tu in danh_sach_tu:
        trie.them_tu(tu)

    print(f"Danh sách từ vựng đã nạp: {danh_sach_tu}\n")

    # Kiểm tra tiền tố
    cac_tien_to_test = ["py", "jav", "c++"]
    for tt in cac_tien_to_test:
        co_found = trie.kiem_tra_tien_to(tt)
        ket_qua = "✅ CÓ từ khớp tiền tố" if co_found else "❌ KHÔNG có"
        print(f"Tiền tố '{tt:<4}': {ket_qua}")


if __name__ == "__main__":
    main()
