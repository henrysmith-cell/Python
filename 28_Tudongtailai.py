import time
import random
import functools


def tu_dong_retry(so_lan_toi_da=3, thoi_gian_cho_ban_dau=1):
    """
    Decorator tự động thử lại hàm khi gặp Exception.
    Khoảng thời gian chờ giữa các lần thử sẽ nhân đôi (Exponential Backoff).
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            thoi_gian_cho = thoi_gian_cho_ban_dau
            for lan_thu in range(1, so_lan_toi_da + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[-] Lần {lan_thu}/{so_lan_toi_da} thất bại! Lỗi: '{e}'")
                    if lan_thu == so_lan_toi_da:
                        print("[!] Đã hết số lần thử lại cho phép. Quăng lỗi ra ngoài.")
                        raise e

                    print(f" -> Đang chờ {thoi_gian_cho} giây trước khi thử lại...")
                    time.sleep(thoi_gian_cho)
                    thoi_gian_cho *= 2  # Nhân đôi thời gian chờ cho lần sau

        return wrapper

    return decorator


# --- THỬ NGHIỆM SỬ DỤNG RETRY DECORATOR ---


@tu_dong_retry(so_lan_toi_da=4, thoi_gian_cho_ban_dau=1)
def ket_noi_server_chua_on_dinh():
    """Giả lập hàm kết nối server bị chập chờn mạng"""
    print("[Kết nối] Đang thử kết nối tới Server...")
    # Tỷ lệ 70% bị lỗi mạng giả lập
    if random.random() < 0.7:
        raise ConnectionResetError("Server bị đứt kết nối tạm thời!")
    return "Thành công: Đã lấy được dữ liệu từ Server!"


def main():
    print("--- DEMO TỰ ĐỘNG RETRY KHI MẠNG BỊ LỖI (EXPONENTIAL BACKOFF) ---")
    try:
        ket_qua = ket_noi_server_chua_on_dinh()
        print(f"\n[Kết quả cuối cùng] {ket_qua}")
    except Exception:
        print("\n[Kết quả cuối cùng] Thất bại hoàn toàn sau nhiều lần thử lại.")


if __name__ == "__main__":
    main()
