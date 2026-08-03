from abc import ABC, abstractmethod


# Class cha định nghĩa quy trình chuẩn
class QuyTrinhDataMiner(ABC):
    def khai_thac_du_lieu(self):
        """Template Method: Định nghĩa cố định thứ tự các bước"""
        self.mo_file()
        self.trich_xuat_du_lieu()
        self.dong_file()
        print("✅ Khai thác dữ liệu hoàn tất!\n")

    def mo_file(self):
        print("1. Đã mở File thành công.")

    @abstractmethod
    def trich_xuat_du_lieu(self):
        """Bước này bắt buộc class con phải tự thực thi tùy theo định dạng file"""
        pass

    def dong_file(self):
        print("3. Đã đóng File an toàn.")


# Class con xử lý File CSV
class PDFDataMiner(QuyTrinhDataMiner):
    def trich_xuat_du_lieu(self):
        print(
            "2. [PDF] Đang phân tích cú pháp các trang và bảng biểu trong file PDF..."
        )


# Class con xử lý File JSON
class JSONDataMiner(QuyTrinhDataMiner):
    def trich_xuat_du_lieu(self):
        print("2. [JSON] Đang parse chuỗi JSON thành các Key-Value Object...")


def main():
    print("--- DEMO TEMPLATE METHOD DESIGN PATTERN ---")

    print("Đọc File PDF:")
    pdf_worker = PDFDataMiner()
    pdf_worker.khai_thac_du_lieu()

    print("Đọc File JSON:")
    json_worker = JSONDataMiner()
    json_worker.khai_thac_du_lieu()


if __name__ == "__main__":
    main()
