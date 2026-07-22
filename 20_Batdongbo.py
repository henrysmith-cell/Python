import asyncio
import time


async def gia_lap_tai_du_lieu_tu_api(api_id, thoi_gian_cho):
    """Một Task bất đồng bộ (Coroutine) giả lập việc gọi API mất thời gian"""
    print(f"[Bắt đầu Task {api_id}] Đang gửi request, dự kiến mất {thoi_gian_cho}s...")

    # Dùng asyncio.sleep thay vì time.sleep để KHÔNG khóa (block) Event Loop
    await asyncio.sleep(thoi_gian_cho)

    print(f"[Hoàn thành Task {api_id}] Đã nhận xong dữ liệu!")
    return {"api_id": api_id, "data": f"Dữ liệu mẫu từ API {api_id}"}


async def main():
    print("--- CHƯƠNG TRÌNH LẬP TRÌNH BẤT ĐỒNG BỘ (ASYNCIO) ---")
    bat_dau = time.perf_counter()

    # Khởi tạo 3 Task bất đồng bộ chạy song song đồng thời trên Event Loop
    task1 = asyncio.create_task(gia_lap_tai_du_lieu_tu_api(1, 2.0))
    task2 = asyncio.create_task(gia_lap_tai_du_lieu_tu_api(2, 1.0))
    task3 = asyncio.create_task(gia_lap_tai_du_lieu_tu_api(3, 1.5))

    # Gom tất cả các task lại và đợi tất cả chạy xong bằng asyncio.gather
    ket_qua = await asyncio.gather(task1, task2, task3)

    print("\n--- TỔNG HỢP KẾT QUẢ ---")
    for res in ket_qua:
        print(f" -> {res}")

    tong_thoi_gian = time.perf_counter() - bat_dau
    print(f"\n[Hoàn tất] Tổng thời gian thực thi: {tong_thoi_gian:.2f} giây.")
    print(
        "(Lưu ý: Tổng thời gian chỉ bằng thời gian của Task lâu nhất [2.0s] chứ không phải tổng [2.0 + 1.0 + 1.5 = 4.5s])"
    )


if __name__ == "__main__":
    # Kích hoạt Event Loop của asyncio
    asyncio.run(main())
