class QuyenTruyCap:
    """Sử dụng Bitmask để quản lý các cờ phân quyền (Permission Flags)"""

    READ = 1 << 0  # 0001 (Giá trị = 1)
    WRITE = 1 << 1  # 0010 (Giá trị = 2)
    EXECUTE = 1 << 2  # 0100 (Giá trị = 4)
    DELETE = 1 << 3  # 1000 (Giá trị = 8)


def main():
    print("--- DEMO THAO TÁC BIT (BITWISE & BITMASKING) ---")

    # 1. Bật/Cấp quyền sử dụng phép OR (|)
    # Cấp quyền READ và WRITE cho User
    quyen_user = QuyenTruyCap.READ | QuyenTruyCap.WRITE
    print(f"Biểu diễn nhị phân của quyền User: {bin(quyen_user)}")

    # 2. Kiểm tra quyền sử dụng phép AND (&)
    has_read = bool(quyen_user & QuyenTruyCap.READ)
    has_execute = bool(quyen_user & QuyenTruyCap.EXECUTE)

    print(f"\nKiểm tra quyền:")
    print(f" - Có quyền ĐỌC (READ)?      : {has_read}")
    print(f" - Có quyền THỰC THI (EXECUTE)?: {has_execute}")

    # 3. Thêm quyền EXECUTE cho User
    quyen_user |= QuyenTruyCap.EXECUTE
    print(f"\nSau khi cấp thêm quyền EXECUTE:")
    print(f" - Có quyền THỰC THI (EXECUTE)?: {bool(quyen_user & QuyenTruyCap.EXECUTE)}")


if __name__ == "__main__":
    main()
