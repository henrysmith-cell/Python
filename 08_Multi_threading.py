import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor
import time

# Danh sách các URL chạy thử nghiệm
DANH_SACH_URL = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.google.com",
]


def tai_trang_web(url):
    """Hàm thực hiện tải nội dung của một URL cụ thể"""
    print(f"[Bắt đầu] Đang kết nối tới: {url}...")
    start_time = time.time()

    # Giả lập User-Agent để tránh bị một số website chặn request tự động
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read()
            thoi_gian_tai = time.time() - start_time
            print(
                f"[Thành công] {url} tải xong trong {thoi_gian_tai:.2f} giây. Kích thước: {len(html)} bytes."
            )
            return url, len(html), None
    except urllib.error.URLError as e:
        print(f"[Thất bại] Lỗi khi tải {url}: {e.reason}")
        return url, 0, str(e.reason)
    except Exception as e:
        print(f"[Thất bại] Lỗi hệ thống với {url}: {str(e)}")
        return url, 0, str(e)


def main():
    print("--- THỬ NGHIỆM TẢI ĐA LUỒNG (MULTI-THREADING) ---")
    thoi_gian_bat_dau = time.time()

    # Sử dụng ThreadPoolExecutor để quản lý và chạy đồng thời tối đa 4 luồng (workers)
    # Cơ chế này giúp tận dụng thời gian chờ phản hồi mạng (I/O Bound)
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Hàm map sẽ tự động phân bổ danh sách URL vào các luồng xử lý độc lập
        ket_qua = executor.map(tai_trang_web, DANH_SACH_URL)

    print("\n--- BÁO CÁO TỔNG HỢP ---")
    for url, kich_thuoc, loi in ket_qua:
        trang_thai = "LỖI" if loi else "OK"
        print(
            f"URL: {url:<30} | Trạng thái: {trang_thai:<5} | Kích thước dữ liệu: {kich_thuoc:,} bytes"
        )

    tong_thoi_gian = time.time() - thoi_gian_bat_dau
    print(
        f"\n[Hoàn tất] Tổng thời gian thực thi của hệ thống: {tong_thoi_gian:.2f} giây."
    )


if __name__ == "__main__":
    main()
