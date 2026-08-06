from abc import ABC, abstractmethod


# 1. Receiver - Đối tượng thực hiện hành động thực sự
class DenThongMinh:
    def bat(self):
        print("💡 [Đèn] Đã BẬT ánh sáng.")

    def tat(self):
        print("🌙 [Đèn] Đã TẮT ánh sáng.")


# 2. Command Interface
class LenhCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# 3. Concrete Commands
class LenhBatDen(LenhCommand):
    def __init__(self, den: DenThongMinh):
        self.den = den

    def execute(self):
        self.den.bat()

    def undo(self):
        self.den.tat()


# 4. Invoker - Remote điều khiển chứa lịch sử lệnh để Undo
class RemoteControl:
    def __init__(self):
        self._lich_su_lenh = []

    def gui_lenh(self, command: LenhCommand):
        command.execute()
        self._lich_su_lenh.append(command)

    def nut_undo(self):
        if not self._lich_su_lenh:
            print("❌ Không có thao tác nào để Undo!")
            return
        lenh_cu = self._lich_su_lenh.pop()
        print("↺ [Undo] Đang hoàn tác thao tác vừa rồi:")
        lenh_cu.undo()


def main():
    print("--- DEMO COMMAND DESIGN PATTERN (CÓ UNDO) ---")
    den = DenThongMinh()
    remote = RemoteControl()

    lenh_bat = LenhBatDen(den)

    # Thực thi lệnh
    print("1. Bấm nút Bật đèn trên Remote:")
    remote.gui_lenh(lenh_bat)

    # Thử nút Undo
    print("\n2. Bấm nút Undo trên Remote:")
    remote.nut_undo()


if __name__ == "__main__":
    main()
