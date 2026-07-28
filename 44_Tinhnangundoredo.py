from abc import ABC, abstractmethod


# 1. Interface Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# 2. Receiver - Đối tượng thực hiện hành động thực sự
class VanBanDocument:
    def __init__(self):
        self.noi_dung = ""

    def chèn_chu(self, chu: str):
        self.noi_dung += chu

    def xoa_chu(self, do_dai: int):
        self.noi_dung = self.noi_dung[:-do_dai]


# 3. Concrete Command - Lệnh chèn văn bản
class ChenTextCommand(Command):
    def __init__(self, doc: VanBanDocument, text: str):
        self.doc = doc
        self.text = text

    def execute(self):
        self.doc.chèn_chu(self.text)

    def undo(self):
        self.doc.xoa_chu(len(self.text))


# 4. Invoker - Trình quản lý Lịch sử lệnh (Undo/Redo Manager)
class LuongThaoTacManager:
    def __init__(self):
        self._lich_su = []

    def thuc_hien_lenh(self, cmd: Command):
        cmd.execute()
        self._lich_su.append(cmd)

    def hoàn_tác(self):
        if not self._lich_su:
            print("[!] Không có thao tác nào để Undo.")
            return
        cmd = self._lich_su.pop()
        cmd.undo()


def main():
    print("--- DEMO COMMAND PATTERN (CƠ CHẾ UNDO) ---")
    doc = VanBanDocument()
    manager = LuongThaoTacManager()

    # Thao tác 1: Gõ "Xin chào "
    cmd1 = ChenTextCommand(doc, "Xin chào ")
    manager.thuc_hien_lenh(cmd1)
    print(f"Nội dung hiện tại: '{doc.noi_dung}'")

    # Thao tác 2: Gõ thêm "Python!"
    cmd2 = ChenTextCommand(doc, "Python!")
    manager.thuc_hien_lenh(cmd2)
    print(f"Nội dung hiện tại: '{doc.noi_dung}'")

    # Bấm Ctrl + Z (Undo lần 1)
    print("\n[Action] Thực hiện Undo (Ctrl + Z)...")
    manager.hoàn_tác()
    print(f"Nội dung sau Undo : '{doc.noi_dung}'")

    # Bấm Ctrl + Z (Undo lần 2)
    print("[Action] Thực hiện Undo (Ctrl + Z)...")
    manager.hoàn_tác()
    print(f"Nội dung sau Undo : '{doc.noi_dung}'")


if __name__ == "__main__":
    main()
