from abc import ABC, abstractmethod


# 1. Handler Interface
class CoCheKiemTra(ABC):
    def __init__(self):
        self._next_handler = None

    def dat_handler_tiep_theo(self, handler):
        self._next_handler = handler
        return handler  # Trả về để cho phép chaining

    @abstractmethod
    def xu_ly(self, request: dict) -> bool:
        if self._next_handler:
            return self._next_handler.xu_ly(request)
        return True


# 2. Concrete Handlers
class KiemTraXacThuc(CoCheKiemTra):
    def xu_ly(self, request: dict) -> bool:
        if not request.get("is_authenticated"):
            print("❌ [Auth Middleware] Người dùng chưa đăng nhập!")
            return False
        print("✅ [Auth Middleware] Xác thực tài khoản thành công.")
        return super().xu_ly(request)


class KiemTraPhanQuyen(CoCheKiemTra):
    def xu_ly(self, request: dict) -> bool:
        if request.get("role") != "admin":
            print("❌ [Permission Middleware] Bạn không có quyền Admin!")
            return False
        print("✅ [Permission Middleware] Quyền truy cập hợp lệ.")
        return super().xu_ly(request)


class KiemTraGioiHanTienDo(CoCheKiemTra):
    def xu_ly(self, request: dict) -> bool:
        if request.get("request_count", 0) > 5:
            print("❌ [Rate Limit Middleware] Bạn đã gửi quá nhiều request (Spam)!")
            return False
        print("✅ [Rate Limit Middleware] Tần suất request hợp lệ.")
        return super().xu_ly(request)


def main():
    print("--- DEMO CHAIN OF RESPONSIBILITY PATTERN (MIDDLEWARE) ---")

    # Thiết lập chuỗi Middleware Pipeline
    auth = KiemTraXacThuc()
    permission = KiemTraPhanQuyen()
    rate_limit = KiemTraGioiHanTienDo()

    # Nối chuỗi: auth -> permission -> rate_limit
    auth.dat_handler_tiep_theo(permission).dat_handler_tiep_theo(rate_limit)

    # Giả lập Request 1: Hợp lệ hoàn toàn
    print("1. Kiểm tra Request 1 (Hợp lệ):")
    req1 = {"is_authenticated": True, "role": "admin", "request_count": 2}
    if auth.xu_ly(req1):
        print("👉 Request được chấp thuận và xử lý logic chính!\n")

    # Giả lập Request 2: Vi phạm phân quyền
    print("2. Kiểm tra Request 2 (Sai quyền):")
    req2 = {"is_authenticated": True, "role": "user", "request_count": 1}
    if not auth.xu_ly(req2):
        print("👉 Request bị từ chối giữa chừng trong Pipeline!")


if __name__ == "__main__":
    main()
