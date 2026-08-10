from abc import ABC, abstractmethod


# 1. Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# 2. Receiver (Đối tượng nhận tác vụ)
class VanBanEditor:
    def __init__(self):
        self.text = ""

    def chèn_chuoi(self, chuoi: str):
        self.text += chuoi

    def xoa_chuoi(self, do_dai: int):
        self.text = self.text[:-do_dai]


# 3. Concrete Command
class ChenVanBanCommand(Command):
    def __init__(self, editor: VanBanEditor, doan_van: str):
        self.editor = editor
        self.doan_van = doan_van

    def execute(self):
        self.editor.chèn_chuoi(self.doan_van)

    def undo(self):
        self.editor.xoa_chuoi(len(self.doan_van))


# 4. Invoker (Quản lý việc gọi lệnh và lưu lịch sử Undo)
class QuanLyLenh:
    def __init__(self):
        self._history = []

    def thuc_thi(self, cmd: Command):
        cmd.execute()
        self._history.append(cmd)

    def hoàn_tac(self):
        if self._history:
            last_cmd = self._history.pop()
            last_cmd.undo()


def main():
    print("--- DEMO COMMAND DESIGN PATTERN (CÓ UNDO) ---")
    editor = VanBanEditor()
    remote = QuanLyLenh()

    # Lệnh 1: Thêm văn bản
    cmd1 = ChenVanBanCommand(editor, "Xin chào Thoại! ")
    remote.thuc_thi(cmd1)
    print(f"Trạng thái 1: '{editor.text}'")

    # Lệnh 2: Thêm tiếp văn bản
    cmd2 = ChenVanBanCommand(editor, "Chúc bạn học tốt Python.")
    remote.thuc_thi(cmd2)
    print(f"Trạng thái 2: '{editor.text}'")

    # Thực hiện Undo
    print("\n🔄 Thực hiện Undo (Hoàn tác)...")
    remote.hoàn_tac()
    print(f"Trạng thái sau Undo: '{editor.text}'")


if __name__ == "__main__":
    main()
