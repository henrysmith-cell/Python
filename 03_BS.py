def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Tìm vị trí ở giữa

        # Nếu tìm thấy mục tiêu ngay giữa
        if arr[mid] == target:
            return mid
        # Nếu mục tiêu lớn hơn, bỏ qua nửa bên trái
        elif arr[mid] < target:
            left = mid + 1
        # Nếu mục tiêu nhỏ hơn, bỏ qua nửa bên phải
        else:
            right = mid - 1

    return -1  # Trả về -1 nếu không tìm thấy


# --- Chạy thử nghiệm ---
# Danh sách BẮT BUỘC phải được sắp xếp trước
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 23

result = binary_search(sorted_list, x)
print(f"Mảng đã sắp xếp: {sorted_list}")
if result != -1:
    print(f"Phần tử {x} được tìm thấy tại vị trí index: {result}")
else:
    print(f"Không tìm thấy phần tử {x} trong mảng.")
