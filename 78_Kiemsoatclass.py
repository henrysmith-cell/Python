class IntegerField:
    """Descriptor kiểm tra thuộc tính bắt buộc phải là số nguyên nằm trong khoảng quy định"""

    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        # Tự động lấy tên thuộc tính khai báo ở Class sở hữu
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(
                f"Lỗi: Thuộc tính phải là số nguyên (int), nhận được {type(value).__name__}!"
            )
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"Lỗi: Giá trị phải >= {self.min_val}!")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"Lỗi: Giá trị phải <= {self.max_val}!")

        setattr(instance, self.private_name, value)


class TaiKhoanGame:
    # Tái sử dụng Descriptor cho các thuộc tính khác nhau
    cap_do = IntegerField(min_val=1, max_val=100)
    diem_so = IntegerField(min_val=0)

    def __init__(self, cap_do: int, diem_so: int):
        self.cap_do = cap_do
        self.diem_so = diem_so


def main():
    print("--- DEMO DESCRIPTOR PROTOCOL (VALIDATION) ---")

    # Khởi tạo hợp lệ
    acc = TaiKhoanGame(cap_do=10, diem_so=500)
    print(f"✅ Tạo tài khoản thành công! Cấp độ: {acc.cap_do}, Điểm số: {acc.diem_so}")

    # Gán giá trị vi phạm
    try:
        print("\nThử gán Cấp độ = 150 (Vượt quá max_val=100)...")
        acc.cap_do = 150
    except ValueError as e:
        print(f"❌ Chặn bởi Descriptor: {e}")

    try:
        print("\nThử gán Điểm số = 'Năm trăm' (Sai kiểu dữ liệu)...")
        acc.diem_so = "Năm trăm"
    except TypeError as e:
        print(f"❌ Chặn bởi Descriptor: {e}")


if __name__ == "__main__":
    main()
