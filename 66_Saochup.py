import datetime


# 1. Memento (Đối tượng lưu Snapshot dữ liệu)
class GameMemento:
    def __init__(self, level: int, hp: int, item: str):
        self._level = level
        self._hp = hp
        self._item = item
        self._timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    def get_saved_info(self):
        return f"Level {self._level} | HP: {self._hp} | Item: {self._item} (Lưu lúc {self._timestamp})"


# 2. Originator (Đối tượng chính cần lưu/khôi phục trạng thái)
class NhanVatGame:
    def __init__(self, ten: str):
        self.ten = ten
        self.level = 1
        self.hp = 100
        self.item = "Kiếm Gỗ"

    def choi_game(self, level: int, hp: int, item: str):
        self.level = level
        self.hp = hp
        self.item = item
        print(
            f"🎮 [{self.ten}] Hiện tại -> Level {self.level} | HP: {self.hp} | Item: {self.item}"
        )

    def save_snapshot(self) -> GameMemento:
        print(f"💾 [Hệ thống] Đã tạo điểm Save Game cho {self.ten}!")
        return GameMemento(self.level, self.hp, self.item)

    def restore_snapshot(self, memento: GameMemento):
        self.level = memento._level
        self.hp = memento._hp
        self.item = memento._item
        print(
            f"🔄 [Hệ thống] Đã khôi phục dữ liệu: Level {self.level} | HP: {self.hp} | Item: {self.item}"
        )


# 3. Caretaker (Quản lý các bản Save Game)
class QuanLySaveGame:
    def __init__(self):
        self._history = []

    def add_save(self, memento: GameMemento):
        self._history.append(memento)

    def get_save(self, index: int) -> GameMemento:
        return self._history[index]


def main():
    print("--- DEMO MEMENTO DESIGN PATTERN ---")
    hero = NhanVatGame("Anh Hùng Thoại")
    keeper = QuanLySaveGame()

    # Bắt đầu chơi
    hero.choi_game(1, 100, "Kiếm Gỗ")
    keeper.add_save(hero.save_snapshot())  # Checkpoint 0

    # Lên cấp & mua đồ
    print()
    hero.choi_game(5, 250, "Kiếm Rồng")
    keeper.add_save(hero.save_snapshot())  # Checkpoint 1

    # Đánh Boss thua (HP về 0)
    print()
    hero.choi_game(5, 0, "Kiếm Rồng (Hỏng)")

    # Khôi phục về Checkpoint 1
    print("\n⚠️  Nhân vật tử trận! Đang tải lại File Save gần nhất...")
    hero.restore_snapshot(keeper.get_save(1))


if __name__ == "__main__":
    main()
