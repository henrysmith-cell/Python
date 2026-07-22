import random


def tao_anh_caro_rgb(ten_file, chieu_rong, chieu_cao):
    """
    Tạo một file ảnh định dạng PPM (Portable Pixmap Format - Netpbm)
    Chạy trực tiếp không cần cài thư viện ngoài!
    """
    # Header chuẩn của file PPM định dạng ASCII (P3)
    header = f"P3\n{chieu_rong} {chieu_cao}\n255\n"

    pixels = []
    for y in range(chieu_cao):
        for x in range(chieu_rong):
            # Tạo hiệu ứng dải màu (Gradient) bằng công thức toán học tọa độ
            r = int((x / chieu_rong) * 255)
            g = int((y / chieu_cao) * 255)
            b = 128
            pixels.append(f"{r} {g} {b}")

    # Ghi toàn bộ thông số màu xuống file
    with open(ten_file, "w") as f:
        f.write(header)
        f.write("\n".join(pixels))

    print(f"[Thành công] Đã xuất file ảnh PPM tại: {ten_file}")
    print(
        "Em có thể mở file này bằng các phần mềm xem ảnh (GIMP, Photoshop, hoặc VSCode Image Viewer)."
    )


def main():
    print("--- TẠO FILE ẢNH BẰNG PYTHON THUẦN (NO LIBRARIES) ---")
    tao_anh_caro_rgb("mau_gradient.ppm", 300, 200)


if __name__ == "__main__":
    main()
