class CuaHangConfig:
    """
    Singleton Class dùng để quản lý Cấu hình hệ thống.
    Dù em có khởi tạo bao nhiêu lần thì nó vẫn chỉ trả về duy nhất 1 Instance trong memory!
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        # Nếu chưa có instance nào được tạo, tạo mới và lưu lại
        if cls._instance is None:
            print("[CuaHangConfig] Đang khởi tạo bộ cấu hình hệ thống lần đầu...")
            cls._instance = super().__new__(cls)
            # Khởi tạo các thuộc tính cấu hình mặc định
            cls._instance.ten_ung_dung = "Hệ thống Quản lý Bán hàng"
            cls._instance.phien_ban = "v1.0.2"
        return cls._instance


def main():
    print("--- DEMO SINGLETON DESIGN PATTERN ---")

    # Khởi tạo lần 1
    config1 = CuaHangConfig()
    print(f"Config 1: {config1.ten_ung_dung} | Memory Address: {id(config1)}")

    # Khởi tạo lần 2 (thử tạo một object mới)
    config2 = CuaHangConfig()
    print(f"Config 2: {config2.ten_ung_dung} | Memory Address: {id(config2)}")

    # Kiểm tra xem config1 và config2 có thực sự trỏ cùng vào 1 ô nhớ hay không
    print(f"\n -> config1 và config2 có phải là MỘT không? {config1 is config2}")

    # Thay đổi giá trị ở config1 thì config2 cũng đổi theo!
    config1.phien_ban = "v2.0.0"
    print(f" -> Phiên bản đọc từ config2 sau khi config1 sửa: {config2.phien_ban}")


if __name__ == "__main__":
    main()
