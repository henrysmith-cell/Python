import asyncio
import random
import time


async def cawl_trang_web(url: str, id_trang: int):
    """Giả lập việc gửi HTTP Request và cào dữ liệu bất đồng bộ từ 1 URL"""
    print(f"[Start] Đang tải dữ liệu từ Trang #{id_trang} ({url})...")
    # Giả lập thời gian chờ phản hồi mạng từ 1 đến 3 giây
    thoi_gian_cho = random.uniform(1.0, 3.0)
    await asyncio.sleep(thoi_gian_cho)

    dung_luong = random.randint(150, 500)  # KB
    print(
        f"[Done ] Trang #{id_trang} tải xong trong {thoi_gian_cho:.2f}s ({dung_luong} KB)"
    )
    return f"Data_{id_trang}"


async def main():
    danh_sach_url = [f"https://api.example.com/item/{i}" for i in range(1, 6)]

    print("--- CÀO DỮ LIỆU SONG SONG VỚI ASYNCIO ---")
    start_time = time.perf_counter()

    # Tạo danh sách các Task chạy song song cùng lúc
    tasks = [cawl_trang_web(url, idx + 1) for idx, url in enumerate(danh_sach_url)]

    # asyncio.gather sẽ kích hoạt tất cả task chạy đồng thời
    ket_qua = await asyncio.gather(*tasks)

    end_time = time.perf_counter() - start_time
    print(f"\n[Kết quả] Đã tải xong tất cả {len(ket_qua)} trang!")
    print(
        f"Tổng thời gian thực thi: {end_time:.2f} giây (So với chạy tuần tự ~10 giây)"
    )


if __name__ == "__main__":
    asyncio.run(main())
