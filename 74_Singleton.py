class SingletonMeta(type):
    """
    Metaclass quản lý việc khởi tạo Instance độc bản (Singleton)
    bằng cách can thiệp vào phương thức __call__ của Class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Nếu Class chưa có instance nào trong dictionary -> Tạo mới
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Sử dụng Metaclass để biến DatabaseConnection thành Singleton
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, db_name: str):
        self.db_name = db_name
        print(
            f"🔌 [Khởi tạo] Đã mở kết nối mới tới Database: '{db_name}' (Tốn thời gian)..."
        )


def main():
    print("--- DEMO SINGLETON BẰNG PYTHON METACLASS ---")

    print("1. Lần gọi khởi tạo thứ nhất:")
    db1 = DatabaseConnection("MySQL_Production")
    print(f"   ID memory của db1: {id(db1)}")

    print("\n2. Lần gọi khởi tạo thứ hai (truyền tham số khác):")
    db2 = DatabaseConnection("PostgreSQL_Test")
    print(f"   ID memory của db2: {id(db2)}")

    print(f"\n🔍 db1 và db2 có trỏ cùng vào 1 vùng nhớ? -> {db1 is db2}")
    print(
        f"👉 Tên Database hiện tại của db2: '{db2.db_name}' (Vẫn giữ nguyên instance ban đầu)"
    )


if __name__ == "__main__":
    main()
