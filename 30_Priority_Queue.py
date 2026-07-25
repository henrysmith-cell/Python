import heapq


class HangDoiUuTienProcess:
    """Quản lý danh sách công việc cần xử lý theo mức độ ưu tiên"""

    def __init__(self):
        self._heap = []
        self._index = 0

    def them_cong_viec(self, ten_cv, độ_ưu_tiên):
        """
        Độ ưu tiên nhỏ hơn sẽ được xử lý TRƯỚC (Min-Heap).
        Ví dụ: Mức 1 (Khẩn cấp) sẽ ra trước Mức 3 (Bình thường).
        """
        # Lưu cặp (độ_ưu_tiên, _index, ten_cv)
        # _index giúp tránh so sánh ten_cv khi 2 công việc có cùng độ ưu tiên
        heapq.heappush(self._heap, (độ_ưu_tiên, self._index, ten_cv))
        self._index += 1
        print(f"[+] Đã thêm: '{ten_cv}' (Độ ưu tiên: {độ_ưu_tiên})")

    def lay_cong_viec_tiep_theo(self):
        if not self._heap:
            return None
        # Lấy ra phần tử có độ ưu tiên nhỏ nhất
        độ_ưu_tiên, _, ten_cv = heapq.heappop(self._heap)
        return ten_cv, độ_ưu_tiên


def main():
    print("--- HỆ THỐNG HÀNG ĐỜI ƯU TIÊN (PRIORITY QUEUE) ---")
    q = HangDoiUuTienProcess()

    # Thêm các công việc với độ ưu tiên ngẫu nhiên
    q.them_cong_viec("Gửi Email thông báo tuần", độ_ưu_tiên=3)
    q.them_cong_viec("Sửa lỗi sập Server (CRITICAL)", độ_ưu_tiên=1)
    q.them_cong_viec("Cập nhật giao diện nút bấm", độ_ưu_tiên=4)
    q.them_cong_viec("Cảnh báo lỗ hổng bảo mật", độ_ưu_tiên=1)

    print("\n--- THỨ TỰ THỰC HIỆN CÔNG VIỆC ---")
    while True:
        res = q.lay_cong_viec_tiep_theo()
        if not res:
            break
        ten_cv, uu_tien = res
        print(f" -> Đang xử lý: '{ten_cv}' [Độ ưu tiên: {uu_tien}]")


if __name__ == "__main__":
    main()
