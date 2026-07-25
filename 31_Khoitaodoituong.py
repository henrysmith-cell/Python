from abc import ABC, abstractmethod


# 1. Interface chung cho tất cả các cổng thanh toán
class CongThanhToan(ABC):
    @abstractmethod
    def thanh_toan(self, so_tien: float) -> bool:
        pass


# 2. Các lớp triển khai thực tế
class ThanhToanMomo(CongThanhToan):
    def thanh_toan(self, so_tien: float) -> bool:
        print(f"[MoMo] Xử lý quét mã QR thanh toán {so_tien:,.0f} VND...")
        return True


class ThanhToanVNPay(CongThanhToan):
    def thanh_toan(self, so_tien: float) -> bool:
        print(
            f"[VNPay] Chuyển hướng tới cổng thẻ ATM/Thẻ tín dụng {so_tien:,.0f} VND..."
        )
        return True


class ThanhToanCOD(CongThanhToan):
    def thanh_toan(self, so_tien: float) -> bool:
        print(
            f"[COD] Tạo đơn hàng thanh toán tiền mặt khi nhận hàng {so_tien:,.0f} VND..."
        )
        return True


# 3. Factory Class đóng vai trò tạo đối tượng
class ThanhToanFactory:
    @staticmethod
    def tao_cong_thanh_toan(loai_thanh_toan: str) -> CongThanhToan:
        loai = loai_thanh_toan.lower().strip()
        if loai == "momo":
            return ThanhToanMomo()
        elif loai == "vnpay":
            return ThanhToanVNPay()
        elif loai == "cod":
            return ThanhToanCOD()
        else:
            raise ValueError(
                f"Loại hình thanh toán '{loai_thanh_toan}' không được hỗ trợ!"
            )


def main():
    print("--- DEMO FACTORY DESIGN PATTERN ---")
    so_tien_don_hang = 750000

    # Người dùng chọn phương thức trên giao diện (ví dụ: "momo")
    phuong_thuc_chon = "momo"

    # Code ứng dụng không cần quan tâm lớp Momo khởi tạo ra sao, chỉ cần gọi Factory
    cong_tt = ThanhToanFactory.tao_cong_thanh_toan(phuong_thuc_chon)
    cong_tt.thanh_toan(so_tien_don_hang)


if __name__ == "__main__":
    main()
