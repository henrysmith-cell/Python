from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SanPham:
    """Dataclass đại diện cho thông tin một sản phẩm trong kho"""

    ma_sp: str
    ten_sp: str
    don_gia: float
    so_luong_ton: int = 0
    # Dùng field(default_factory=...) để tạo giá trị mặc định động
    ngay_tao: datetime = field(default_factory=datetime.now)

    @property
    def tong_gia_tri_ton_kho(self) -> float:
        """Phương thức tính tổng giá trị hàng tồn kho"""
        return self.don_gia * self.so_luong_ton


def main():
    print("--- DEMO PYTHON DATACLASS ---")

    # Khởi tạo đối tượng cực kỳ ngắn gọn
    sp1 = SanPham(ma_sp="SP01", ten_sp="Bàn phím Cơ", don_gia=1200000, so_luong_ton=15)
    sp2 = SanPham(
        ma_sp="SP02", ten_sp="Chuột Không dây", don_gia=450000, so_luong_ton=30
    )

    # Dataclass tự động sinh hàm __repr__ in ra thông tin siêu đẹp
    print("Thông tin sản phẩm 1:")
    print(sp1)

    print("\nThông tin sản phẩm 2:")
    print(sp2)

    # Gọi property tính toán
    print(
        f"\n -> Tổng giá trị tồn kho của {sp1.ten_sp}: {sp1.tong_gia_tri_ton_kho:,.0f} VND"
    )


if __name__ == "__main__":
    main()
