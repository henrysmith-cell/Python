import asyncio
import time


async def tai_du_lieu_tu_api(id_server: int, thoi_gian_cho: float):
    """Hàm bất đồng bộ giả lập việc gửi HTTP request"""
    print(f"⏳ [Server {id_server}] Bắt đầu gửi request...")
    # asyncio.sleep không làm 'chặn' (block) cả chương trình như time.sleep
    await asyncio.sleep(thoi_gian_cho)
    print(f"✅ [Server {id_server}] Tải xong dữ liệu sau {thoi_gian_cho}s!")
    return f"Data_{id_server}"


async def main():
    print("--- DEMO LẬP TRÌNH BẤT ĐỒNG BỘ (ASYNCIO) ---")
    start_time = time.perf_counter()

    # Chạy song song 3 tác vụ I/O bất đồng bộ
    danh_sach_tac_vu = [
        tai_du_lieu_tu_api(id_server=1, thoi_gian_cho=2.0),
        tai_du_lieu_tu_api(id_server=2, thoi_gian_cho=1.0),
        tai_du_lieu_tu_api(id_server=3, thoi_gian_cho=1.5),
    ]

    # asyncio.gather cho phép chờ tất cả tác vụ hoàn thành đồng thời
    ket_qua = await asyncio.gather(*danh_sach_tac_vu)

    total_time = time.perf_counter() - start_time
    print(f"\n📦 Kết quả thu được: {ket_qua}")
    print(
        f"⚡ Tổng thời gian chạy: {total_time:.2f} giây (Chạy song song thay vì tốn 2.0+1.0+1.5 = 4.5s)!"
    )


if __name__ == "__main__":
    # Khởi chạy Event Loop của asyncio
    asyncio.run(main())
