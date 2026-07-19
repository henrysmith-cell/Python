import string
from collections import Counter


def lam_sach_van_ban(van_ban):
    """Chuyển về chữ thường và loại bỏ tất cả các dấu câu (. , ! ?...)"""
    van_ban = van_ban.lower()
    # Tạo bảng dịch để loại bỏ ký tự đặc biệt nhanh chóng bằng C-level speed của Python
    bang_xoa_dau = str.maketrans("", "", string.punctuation)
    return van_ban.translate(bang_xoa_dau)


def phan_tich_tu(doan_van):
    van_ban_sach = lam_sach_van_ban(doan_van)
    # Tách từ dựa trên khoảng trắng
    cac_tu = van_ban_sach.split()

    # Sử dụng Counter - cấu trúc dữ liệu tối ưu nhất của Python để đếm phần tử lặp
    bo_dem = Counter(cac_tu)
    return bo_dem


def main():
    # Đoạn văn bản mẫu (hoặc em có thể đọc từ một file .txt)
    doan_van_mau = """
    Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và rất phổ biến. 
    Lập trình Python giúp chúng ta xử lý dữ liệu, làm AI, hay viết web một cách nhanh chóng.
    Học Python, học lập trình, mở rộng tương lai!
    """

    print("--- ĐOẠN VĂN BẢN PHÂN TÍCH ---")
    print(doan_van_mau.strip())

    bo_dem_tu = phan_tich_tu(doan_van_mau)

    print("\n--- KẾT QUẢ THỐNG KÊ ---")
    print(f"Tổng số từ (sau khi làm sạch): {sum(bo_dem_tu.values())} từ")
    print(f"Số lượng từ duy nhất (unique words): {len(bo_dem_tu)}")

    # Lấy ra top 3 từ xuất hiện nhiều nhất
    print("\nTop 3 từ xuất hiện nhiều nhất:")
    for tu, so_lan in bo_dem_tu.most_common(3):
        print(f" - Từ '{tu}': xuất hiện {so_lan} lần")


if __name__ == "__main__":
    main()
