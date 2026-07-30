class KiemTraQuyChuanMeta(type):
    """
    Metaclass bắt buộc tất cả tên phương thức (method) trong class con
    phải bắt đầu bằng chữ thường (snake_case).
    """

    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            # Chỉ kiểm tra các phương thức tự định nghĩa (không phải magic method)
            if callable(attr_value) and not attr_name.startswith("__"):
                if not attr_name[0].islower():
                    raise TypeError(
                        f"[Lỗi Quy Chuẩn] Phương thức '{attr_name}' trong Class '{name}' "
                        f"phải bắt đầu bằng chữ cái thường! (Tuân thủ snake_case)"
                    )
        return super().__new__(cls, name, bases, dct)


# Áp dụng Metaclass cho class cơ sở
class ServiceBase(metaclass=KiemTraQuyChuanMeta):
    pass


def main():
    print("--- DEMO PYTHON METACLASS (ĐỒNG BỘ QUY CHUẨN CODE) ---")

    try:
        # Class này tuân thủ đúng quy chuẩn -> Khởi tạo thành công
        class NguoiDungService(ServiceBase):
            def xu_ly_dang_nhap(self):
                pass

        print("✅ Class 'NguoiDungService' được tạo thành công vì đúng quy chuẩn!")

        # Class này vi phạm quy chuẩn (Viết hoa chữ cái đầu 'Xu_ly') -> Metaclass quăng lỗi ngay!
        class SanPhamService(ServiceBase):
            def Xu_ly_don_hang(self):
                pass

    except TypeError as e:
        print(f"\n❌ Phát hiện lỗi bởi Metaclass:\n {e}")


if __name__ == "__main__":
    main()
