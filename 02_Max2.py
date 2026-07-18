def find_second_largest(numbers):
    # Lọc bỏ các số trùng nhau bằng set, sau đó chuyển lại thành list
    unique_numbers = list(set(numbers))

    # Nếu danh sách có ít hơn 2 phần tử khác nhau thì không có số lớn thứ hai
    if len(unique_numbers) < 2:
        return None

    # Cách đơn giản: Sắp xếp giảm dần và lấy phần tử ở vị trí index 1
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


# --- Chạy thử nghiệm ---
my_list = [10, 5, 20, 20, 8, 15, 15]
result = find_second_largest(my_list)

print(f"Danh sách gốc: {my_list}")
if result is not None:
    print(f"Số lớn thứ hai trong danh sách là: {result}")
else:
    print("Danh sách không có số lớn thứ hai (quá ít phần tử hoặc các số bằng nhau).")
