import math


def is_prime(n):
    # Số nhỏ hơn hoặc bằng 1 không phải là số nguyên tố
    if n <= 1:
        return False

    # Kiểm tra từ 2 đến căn bậc hai của n
    # Dùng math.isqrt(n) giúp tăng tốc độ xử lý cho số lớn
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False  # Chia hết cho số khác thì không phải số nguyên tố

    return True  # Nếu không chia hết cho số nào thì là số nguyên tố


# --- Chạy thử nghiệm ---
num = int(input("Nhập một số nguyên để kiểm tra: "))
if is_prime(num):
    print(f"{num} là số nguyên tố! 🎉")
else:
    print(f"{num} không phải là số nguyên tố.")
