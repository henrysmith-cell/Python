import time


class TokenBucketRateLimiter:
    """
    Cơ chế giới hạn truy cập bằng thuật toán Token Bucket:
    - Xô chứa tối đa `dung_luong` token.
    - Token tự động được nạp lại theo tốc độ `toc_do_nap` (token/giây).
    """

    def __init__(self, dung_luong: int, toc_do_nap: float):
        self.dung_luong = dung_luong
        self.toc_do_nap = toc_do_nap
        self.tokens = float(dung_luong)
        self.last_update = time.monotonic()

    def _nap_token(self):
        now = time.monotonic()
        thoi_gian_troi_qua = now - self.last_update
        # Số token được cộng thêm dựa trên thời gian trôi qua
        tokens_moi = thoi_gian_troi_qua * self.toc_do_nap
        self.tokens = min(self.dung_luong, self.tokens + tokens_moi)
        self.last_update = now

    def thuc_hien_request(self) -> bool:
        self._nap_token()
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True  # Cho phép request đi qua
        return False  # Chặn request vì hết token (Rate Limit Exceeded)


def main():
    print("--- DEMO RATE LIMITER (TOKEN BUCKET) ---")
    # Cho phép tối đa 3 token trong xô, mỗi giây nạp lại 1 token
    limiter = TokenBucketRateLimiter(dung_luong=3, toc_do_nap=1.0)

    print("Gửi liên tiếp 5 request...")
    for i in range(1, 6):
        duoc_phep = limiter.thuc_hien_request()
        trang_thai = (
            "✅ THÀNH CÔNG" if duoc_phep else "❌ BỊ CHẶN (429 Too Many Requests)"
        )
        print(f"Request {i}: {trang_thai}")

    print("\nChờ 2 giây để token tự động nạp lại...")
    time.sleep(2)

    print("Gửi lại request 6...")
    if limiter.thuc_hien_request():
        print("Request 6: ✅ THÀNH CÔNG (Đã có token mới!)")
    else:
        print("Request 6: ❌ BỊ CHẶN")


if __name__ == "__main__":
    main()
