class Node:
    """Node trong Danh sách liên kết đôi"""

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """Bộ nhớ tạm LRU (Least Recently Used) tự cài đặt"""

    def __init__(self, dung_luong: int):
        self.dung_luong = dung_luong
        self.cache = {}  # Map lưu key -> Node

        # Tạo 2 Node giả (Head và Tail) để đơn giản hóa việc thêm/xóa
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _xoa_node(self, node: Node):
        """Xóa một Node khỏi danh sách liên kết đôi"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _them_vao_dau(self, node: Node):
        """Thêm một Node vào ngay sau Head (Vị trí dùng gần nhất)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Đã dùng key này -> Chuyển Node lên đầu danh sách
            self._xoa_node(node)
            self._them_vao_dau(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._xoa_node(self.cache[key])

        node_moi = Node(key, value)
        self.cache[key] = node_moi
        self._them_vao_dau(node_moi)

        # Nếu vượt quá dung lượng -> Xóa phần tử ở Tail (Phần tử lâu không dùng nhất)
        if len(self.cache) > self.dung_luong:
            lru_node = self.tail.prev
            self._xoa_node(lru_node)
            del self.cache[lru_node.key]


def main():
    print("--- DEMO TỰ TẠO LRU CACHE ---")
    cache = LRUCache(dung_luong=2)

    cache.put(1, 100)  # Cache: {1:100}
    cache.put(2, 200)  # Cache: {1:100, 2:200}
    print(f"Lấy key 1: {cache.get(1)}")  # Trả về 100 (1 được đẩy lên mới nhất)

    cache.put(3, 300)  # Dung lượng đầy! Key 2 lâu không dùng sẽ bị XÓA!
    print(f"Lấy key 2: {cache.get(2)}")  # Trả về -1 (Không tìm thấy)
    print(f"Lấy key 3: {cache.get(3)}")  # Trả về 300


if __name__ == "__main__":
    main()
