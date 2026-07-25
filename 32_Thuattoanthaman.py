from dataclasses import dataclass


@dataclass
class CuocHop:
    ten: str
    bat_dau: float  # Thời gian bắt đầu (ví dụ: 8.5 là 8h30)
    ket_thuc: float  # Thời gian kết thúc


def tim_lich_hop_toi_uu(danh_sach_cuoc_hop):
    """
    Giải thuật Tham ăn (Greedy) xếp lịch họp không trùng nhau:
    Bước 1: Sắp xếp danh sách cuộc họp theo thời gian KẾT THÚC tăng dần.
    Bước 2: Chọn cuộc họp đầu tiên, sau đó chọn cuộc họp tiếp theo có thời gian bắt đầu >= cuộc họp vừa chọn.
    """
    if not danh_sach_cuoc_hop:
        return []

    # Sắp xếp theo mốc thời gian ket_thuc
    danh_sach_sap_xep = sorted(danh_sach_cuoc_hop, key=lambda x: x.ket_thuc)

    lich_duoc_chon = []
    cuoc_hop_cuoi = None

    for ch in danh_sach_sap_xep:
        if cuoc_hop_cuoi is None or ch.bat_dau >= cuoc_hop_cuoi.ket_thuc:
            lich_duoc_chon.append(ch)
            cuoc_hop_cuoi = ch

    return lich_duoc_chon


def main():
    danh_sach_hop = [
        CuocHop("Họp Phòng IT", 8.0, 10.0),
        CuocHop("Họp Dự án A", 9.0, 11.5),
        CuocHop("Đào tạo Nhân sự", 10.0, 11.0),
        CuocHop("Gặp Khách hàng", 11.0, 13.0),
        CuocHop("Review Code", 12.0, 14.0),
    ]

    print("--- THUẬT TOÁN THAM ĂN: LẬP LỊCH CÔNG VIỆC TỐI ƯU ---")
    print("Danh sách tất cả các cuộc họp đăng ký:")
    for ch in danh_sach_hop:
        print(f" - {ch.ten:<20}: {ch.bat_dau}h -> {ch.ket_thuc}h")

    lich_toi_uu = tim_lich_hop_toi_uu(danh_sach_hop)

    print(f"\n -> Số lượng cuộc họp tối đa tổ chức được: {len(lich_toi_uu)}")
    print("Lịch trình chi tiết:")
    for ch in lich_toi_uu:
        print(f" [✓] {ch.ten:<20}: {ch.bat_dau}h -> {ch.ket_thuc}h")


if __name__ == "__main__":
    main()
