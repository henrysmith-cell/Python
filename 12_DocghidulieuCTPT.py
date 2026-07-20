import json
import os

FILE_DATABASE = "database_nguoi_dung.json"


def khoi_tao_du_lieu_mau():
    """Tạo dữ liệu mặc định ban đầu nếu file chưa tồn tại"""
    du_lieu_mac_dinh = {
        "he_thong": "HeThongQuanLy_v2",
        "danh_sach_user": [
            {
                "id": 1,
                "username": "admin",
                "roles": ["quản trị", "nhân viên"],
                "active": True,
            },
            {"id": 2, "username": "student_01", "roles": ["học viên"], "active": False},
        ],
    }
    # Ghi file JSON với định dạng thụt lề (indent=4) cho dễ đọc bằng mắt
    with open(FILE_DATABASE, "w", encoding="utf-8") as f:
        json.dump(du_lieu_mac_dinh, f, ensure_ascii=False, indent=4)
    print(f"[Hệ thống] Đã khởi tạo dữ liệu mẫu thành công tại file: {FILE_DATABASE}")


def doc_du_lieu_json():
    if not os.path.exists(FILE_DATABASE):
        print("[Cảnh báo] File dữ liệu không tồn tại!")
        khoi_tao_du_lieu_mau()

    try:
        with open(FILE_DATABASE, "r", encoding="utf-8") as f:
            # Chuyển đổi từ chuỗi văn bản JSON thành cấu trúc Dict/List của Python
            du_lieu = json.load(f)
            return du_lieu
    except json.JSONDecodeError:
        print("[Lỗi nặng] Cấu trúc file JSON bị hỏng, không thể parse dữ liệu!")
        return None


def cap_nhat_trang_thai_user(user_id, trang_thai_moi):
    du_lieu = doc_du_lieu_json()
    if not du_lieu:
        return

    tim_thay = False
    for user in du_lieu["danh_sach_user"]:
        if user["id"] == user_id:
            user["active"] = trang_thai_moi
            tim_thay = True
            break

    if tim_thay:
        # Ghi đè lại file sau khi thay đổi dữ liệu trên bộ nhớ RAM
        with open(FILE_DATABASE, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
        print(
            f"[Thành công] Đã cập nhật trạng thái hoạt động của User ID {user_id} thành {trang_thai_moi}."
        )
    else:
        print(f"[-] Không tìm thấy User ID: {user_id} trong hệ thống.")


def main():
    print("--- QUY TRÌNH XỬ LÝ FILE DỮ LIỆU JSON ĐỘC LẬP ---")

    # Bước 1: Đọc dữ liệu hiện tại
    du_lieu_hien_tai = doc_du_lieu_json()
    if du_lieu_hien_tai:
        print("\nDữ liệu hiện có trước khi sửa đổi:")
        print(json.dumps(du_lieu_hien_tai, ensure_ascii=False, indent=2))

    # Bước 2: Thực hiện chỉnh sửa và cập nhật xuống file cứng ổ đĩa
    print("\n--- Thực hiện cập nhật trạng thái tài khoản ---")
    cap_nhat_trang_thai_user(2, True)

    # Bước 3: Đọc lại để kiểm tra
    du_lieu_moi = doc_du_lieu_json()
    print("\nDữ liệu mới nhất đọc từ file sau khi cập nhật:")
    print(json.dumps(du_lieu_moi, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
