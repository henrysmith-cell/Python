import heapq


class HangDoiUuTien:
    """Hàng đợi ưu tiên dựa trên Min-Heap"""

    def __init__(self):
        self._heap = []

    def them_cong_viec(self, ten_cv: str, do_uu_tien: int):
        # Do heapq sắp xếp theo giá trị tăng dần, do_uu_tien càng nhỏ -> Càng cấp bách
        heapq.heappush(self._heap, (do_uu_tien, ten_cv))

    def lay_cong_viec(self):
        if not self._heap:
            return None
        do_uu_tien, ten_cv = heapq.heappop(self._heap)
        return ten_cv, do_uu_tien


def main():
    print("--- DEMO HÀNG ĐỜI ƯU TIÊN (PRIORITY QUEUE) ---")
    pq = HangDoiUuTien()

    # Thêm các công việc với độ ưu tiên khác nhau (1: Rất gấp, 5: Bình thường)
    pq.them_cong_viec("Cập nhật giao diện Web", do_uu_tien=3)
    pq.them_cong_viec("Sửa lỗi Bảo mật khẩn cấp (Hotfix)", do_uu_tien=1)
    pq.them_cong_viec("Viết Báo cáo cuối tháng", do_uu_tien=5)
    pq.them_cong_viec("Tối ưu Database", do_uu_tien=2)

    print("Thứ tự xử lý công việc dựa trên mức độ ưu tiên:\n")
    buoc = 1
    while True:
        res = pq.lay_cong_viec()
        if not res:
            break
        ten_cv, uu_tien = res
        print(f"Bước {buoc}: [Mức {uu_tien}] -> Xử lý: '{ten_cv}'")
        buoc += 1


if __name__ == "__main__":
    main()
