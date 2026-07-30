import itertools


class RoundRobinLoadBalancer:
    """Bộ cân bằng tải sử dụng thuật toán Round Robin"""

    def __init__(self, danh_sach_servers):
        if not danh_sach_servers:
            raise ValueError("Danh sách server không được để rỗng!")
        self.servers = danh_sach_servers
        # itertools.cycle tạo ra vòng lặp vô hạn qua các phần tử của list
        self._vong_lap_server = itertools.cycle(self.servers)

    def lay_server_tiep_theo(self) -> str:
        """Lấy ra IP/Tên server tiếp theo để xử lý request"""
        return next(self._vong_lap_server)


def main():
    print("--- DEMO LOAD BALANCER (ROUND ROBIN) ---")
    danh_sach_app_servers = [
        "192.168.1.10 (Server A)",
        "192.168.1.11 (Server B)",
        "192.168.1.12 (Server C)",
    ]

    lb = RoundRobinLoadBalancer(danh_sach_app_servers)

    print("Giả lập 7 request người dùng gửi tới hệ thống:\n")
    for req_id in range(1, 8):
        server_duoc_chon = lb.lay_server_tiep_theo()
        print(f"Request #{req_id} -> Được điều hướng tới: {server_duoc_chon}")


if __name__ == "__main__":
    main()
