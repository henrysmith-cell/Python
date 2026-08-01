import ctypes
import time


def main():
    print("--- DEMO TỐI ƯU TỐC ĐỘ: TÍCH HỢP HÀM NATIVE VỚI CTYPES ---")

    # 1. Gọi thư viện C chuẩn có sẵn trên hệ điều hành (msvcrt trên Windows hoặc libc trên Linux/Mac)
    try:
        # Thử nạp thư viện C chuẩn của hệ thống
        try:
            libc = ctypes.CDLL("msvcrt.dll")  # Trên Windows
        except OSError:
            libc = ctypes.CDLL("libc.so.6")  # Trên Linux

        print("✅ Đã kết nối thành công tới thư viện C native (C-Shared Library).")

        # 2. Định nghĩa kiểu dữ liệu đầu vào và đầu ra cho hàm C (Ví dụ: hàm abs / puts)
        # Khai báo hàm `puts` từ C: int puts(const char *str);
        libc.puts.argtypes = [ctypes.c_char_p]
        libc.puts.restype = ctypes.c_int

        # 3. Thực thi hàm C trực tiếp từ Python
        print("\nGọi hàm puts() trực tiếp từ C Native:")
        thong_diep = "Xin chao! Day la chuoi duoc in ra tu C Native qua ctypes.".encode(
            "utf-8"
        )
        libc.puts(thong_diep)

    except Exception as e:
        print(f"❌ Không thể nạp thư viện C hệ thống: {e}")


if __name__ == "__main__":
    main()
