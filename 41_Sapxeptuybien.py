from functools import cmp_to_key


class HocSinh:
    def __init__(self, ten: str, diem_toan: float, diem_van: float):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_van = diem_van

    @property
    def diem_trung_binh(self) -> float:
        return (self.diem_toan + self.diem_van) / 2


def so_sanh_hoc_sinh(hs1: HocSinh, hs2: HocSinh) -> int:
    """
    Quy tắc xếp hạng:
    1. Học sinh có Điểm trung bình cao hơn xếp TRƯỚC.
    2. Nếu ĐTB bằng nhau, ai có Điểm Toán cao hơn xếp TRƯỚC.
    3. Nếu Điểm Toán vẫn bằng nhau, xếp theo Tên bảng chữ cái (A-Z).

    Trả về:
      < 0 nếu hs1 đứng trước hs2
      > 0 nếu hs1 đứng sau hs2
      0 nếu bằng nhau
    """
    if hs1.diem_trung_binh != hs2.diem_trung_binh:
        return -1 if hs1.diem_trung_binh > hs2.diem_trung_binh else 1

    if hs1.diem_toan != hs2.diem_toan:
        return -1 if hs1.diem_toan > hs2.diem_toan else 1

    if hs1.ten < hs2.ten:
        return -1
    elif hs1.ten > hs2.ten:
        return 1
    return 0


def main():
    danh_sach = [
        HocSinh("Bình", 8.0, 8.0),  # ĐTB = 8.0, Toán = 8.0
        HocSinh("An", 9.0, 7.0),  # ĐTB = 8.0, Toán = 9.0 (Thắng Bình nhờ Toán)
        HocSinh("Cường", 9.5, 9.5),  # ĐTB = 9.5 (Cao nhất)
        HocSinh(
            "Dũng", 8.0, 8.0
        ),  # ĐTB = 8.0, Toán = 8.0 (Bằng Bình nhưng tên 'D' đứng sau 'B')
    ]

    print("--- SẮP XẾP TÙY BIẾN VỚI CMP_TO_KEY ---")
    danh_sach_xep_hang = sorted(danh_sach, key=cmp_to_key(so_sanh_hoc_sinh))

    for idx, hs in enumerate(danh_sach_xep_hang, 1):
        print(
            f"Hạng {idx}: {hs.ten:<8} | ĐTB: {hs.diem_trung_binh:.1f} | Toán: {hs.diem_toan:.1f} | Văn: {hs.diem_van:.1f}"
        )


if __name__ == "__main__":
    main()
