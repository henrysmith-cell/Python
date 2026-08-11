from abc import ABC, abstractmethod


# 1. Mediator Interface
class TramDieuHanhKhongLuu(ABC):
    @abstractmethod
    def gui_thong_diep(self, thong_diep: str, may_bay_gui):
        pass


# 2. Concrete Mediator
class TramDieuHanhTrungTam(TramDieuHanhKhongLuu):
    def __init__(self):
        self._danh_sach_may_bay = []

    def dang_ky_may_bay(self, may_bay):
        self._danh_sach_may_bay.append(may_bay)
        may_bay.tram_dieu_hanh = self

    def gui_thong_diep(self, thong_diep: str, may_bay_gui):
        for mb in self._danh_sach_may_bay:
            # Không gửi lại thông điệp cho chính máy bay vừa phát ra
            if mb != may_bay_gui:
                mb.nhan_thong_diep(thong_diep)


# 3. Colleague Class
class MayBay:
    def __init__(self, so_hieu: str):
        self.so_hieu = so_hieu
        self.tram_dieu_hanh = None

    def phát_tin(self, thong_diep: str):
        print(f"\n✈️  [{self.so_hieu}] Phát tín hiệu: '{thong_diep}'")
        if self.tram_dieu_hanh:
            self.tram_dieu_hanh.gui_thong_diep(thong_diep, self)

    def nhan_thong_diep(self, thong_diep: str):
        print(f" 📥 [{self.so_hieu}] Đã nhận thông báo: '{thong_diep}'")


def main():
    print("--- DEMO MEDIATOR DESIGN PATTERN ---")
    tram_khong_luu = TramDieuHanhTrungTam()

    flight_01 = MayBay("VN-A321")
    flight_02 = MayBay("VJ-B737")
    flight_03 = MayBay("QH-A350")

    tram_khong_luu.dang_ky_may_bay(flight_01)
    tram_khong_luu.dang_ky_may_bay(flight_02)
    tram_khong_luu.dang_ky_may_bay(flight_03)

    # Máy bay 01 phát tín hiệu, Trạm điều hành sẽ chuyển tiếp cho máy bay 02 và 03
    flight_01.phát_tin("Xin phép chuẩn bị hạ cánh xuống đường băng 1A.")


if __name__ == "__main__":
    main()
