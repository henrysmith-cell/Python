def tao_bang_dich_chuyen(pattern: str) -> dict:
    """Tạo bảng Bad Character Table cho thuật toán Horspool"""
    m = len(pattern)
    # Mặc định ký tự không xuất hiện trong pattern sẽ nhảy vọt m bước
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    return bad_char


def boyer_moore_horspool(text: str, pattern: str) -> list:
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    bad_char = tao_bang_dich_chuyen(pattern)
    vi_tri_tim_thay = []
    i = 0  # Chỉ số bắt đầu cửa sổ so sánh trên text

    while i <= n - m:
        j = m - 1  # So sánh từ phải sang trái

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            # Tìm thấy pattern trùng khớp hoàn toàn
            vi_tri_tim_thay.append(i)
            # Nhảy cửa sổ dựa theo ký tự cuối cùng của cửa sổ hiện tại
            i += bad_char.get(text[i + m - 1], m)
        else:
            # Nhảy cửa sổ dựa trên ký tự không khớp ở cuối cửa sổ
            ky_tu_cuoi = text[i + m - 1]
            i += bad_char.get(ky_tu_cuoi, m)

    return vi_tri_tim_thay


def main():
    print("--- DEMO THUẬT TOÁN TÌM KIẾM CHUỖI BOYER-MOORE-HORSPOOL ---")
    van_ban = "LAP TRINH PYTHON NANG CAO HOAC LAP TRINH C++"
    mau_tim = "LAP TRINH"

    ket_qua = boyer_moore_horspool(van_ban, mau_tim)
    print(f"Văn bản: '{van_ban}'")
    print(f"Mẫu cần tìm: '{mau_tim}'")
    print(f"👉 Tìm thấy mẫu tại các vị trí chỉ số (index): {ket_qua}")


if __name__ == "__main__":
    main()
