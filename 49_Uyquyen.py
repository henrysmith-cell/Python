from abc import ABC, abstractmethod


# 1. Interface chung cho Server
class ServerInterface(ABC):
    @abstractmethod
    def truy_cap_du_lieu(self, user_role: str):
        pass


# 2. Real Subject - Server chứa dữ liệu nhạy cảm
class ServerGoc(ServerInterface):
    def __init__(self):
        print(
            "[ServerGoc] Đang kết nối tới Cơ sở dữ liệu lõi (Tốn nhiều tài nguyên)..."
        )

    def truy_cap_du_lieu(self, user_role: str):
        print(f"[ServerGoc] ✅ Đã xuất dữ liệu bảo mật cho quyền '{user_role}'.")


# 3. Proxy - Kiểm soát quyền trước khi cho vào Server gốc
class ProxyServer(ServerInterface):
    def __init__(self):
        self._server_goc = None  # Chưa tạo ngay (Lazy Initialization)

    def truy_cap_du_lieu(self, user_role: str):
        # Kiểm tra quyền truy cập (Access Control)
        if user_role.lower() != "admin":
            print(
                f"[ProxyServer] ❌ Truy cập bị TỪ CHỐI! Quyền '{user_role}' không đủ thẩm quyền."
            )
            return

        # Chỉ khởi tạo ServerGoc khi thực sự cần thiết
        if self._server_goc is None:
            self._server_goc = ServerGoc()

        self._server_goc.truy_cap_du_lieu(user_role)


def main():
    print("--- DEMO PROXY DESIGN PATTERN ---")
    proxy = ProxyServer()

    # User thường cố truy cập -> Bị chặn từ lớp Proxy
    print("\n1. Thử truy cập với quyền 'Guest':")
    proxy.truy_cap_du_lieu("Guest")

    # Admin truy cập -> Cho phép và mới bắt đầu khởi tạo Server gốc
    print("\n2. Thử truy cập với quyền 'Admin':")
    proxy.truy_cap_du_lieu("Admin")


if __name__ == "__main__":
    main()
