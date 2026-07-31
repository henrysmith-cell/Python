from abc import ABC, abstractmethod


# 1. Component chung
class NodeHeThong(ABC):
    @abstractmethod
    def lay_dung_luong() -> int:
        pass

    @abstractmethod
    def hien_thi(self, indent: str = ""):
        pass


# 2. Leaf (Lá - Đối tượng đơn lẻ)
class TậpTin(NodeHeThong):
    def __init__(self, ten: str, dung_luong_kb: int):
        self.ten = ten
        self.dung_luong_kb = dung_luong_kb

    def lay_dung_luong(self) -> int:
        return self.dung_luong_kb

    def hien_thi(self, indent: str = ""):
        print(f"{indent}📄 File: {self.ten} ({self.dung_luong_kb} KB)")


# 3. Composite (Cành/Gốc - Chứa các Node con)
class ThuMuc(NodeHeThong):
    def __init__(self, ten: str):
        self.ten = ten
        self.danh_sach_con = []

    def them_node(self, node: NodeHeThong):
        self.danh_sach_con.append(node)

    def lay_dung_luong(self) -> int:
        # Tính tổng dung lượng bằng cách đệ quy xuống tất cả con
        return sum(child.lay_dung_luong() for child in self.danh_sach_con)

    def hien_thi(self, indent: str = ""):
        print(f"{indent}📁 Folder: {self.ten}/ (Tổng: {self.lay_dung_luong()} KB)")
        for child in self.danh_sach_con:
            child.hien_thi(indent + "   ")


def main():
    print("--- DEMO COMPOSITE DESIGN PATTERN ---")

    # Tạo cây thư mục
    root = ThuMuc("C_Drive")
    folder_code = ThuMuc("Projects")

    file1 = TậpTin("main.py", 15)
    file2 = TậpTin("script.sh", 5)
    file3 = TậpTin("database.sqlite", 1024)

    folder_code.them_node(file1)
    folder_code.them_node(file2)

    root.them_node(folder_code)
    root.them_node(file3)

    # Hiển thị cấu trúc cây và tự động tính tổng dung lượng đệ quy
    root.hien_thi()


if __name__ == "__main__":
    main()
