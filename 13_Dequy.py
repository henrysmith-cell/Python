def tinh_giai_thua(n):
    """
    Tính n! = 1 * 2 * 3 * ... * n
    Đăng ký điều kiện dừng: 0! = 1! = 1
    """
    if n < 0:
        return None  # Không định nghĩa cho số âm
    if n == 0 or n == 1:
        return 1
    # Bước đệ quy
    return n * tinh_giai_thua(n - 1)


def fibonacci(n):
    """
    Trả về số Fibonacci thứ n
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("--- DEMO THUẬT TOÁN ĐỆ QUY ---")

    # 1. Tính giai thừa
    so_n = 6
    ket_qua_gt = tinh_giai_thua(so_n)
    print(f"[Giai thừa] {so_n}! = {ket_qua_gt}")

    # 2. In dãy số Fibonacci
    so_luong_fibo = 10
    print(f"\n[Fibonacci] Dãy {so_luong_fibo} số Fibonacci đầu tiên:")
    day_fibo = [str(fibonacci(i)) for i in range(so_luong_fibo)]
    print(" -> ".join(day_fibo))


if __name__ == "__main__":
    main()
