class Student:
    def __init__(self, name, student_id, score_math, score_it):
        self.name = name
        self.student_id = student_id
        self.score_math = score_math
        self.score_it = score_it

    def calculate_gpa(self):
        # Tính điểm trung bình hệ 10 thông thường
        return (self.score_math + self.score_it) / 2

    def get_rank(self):
        gpa = self.calculate_gpa()
        if gpa >= 8.5:
            return "Xuất sắc/Giỏi"
        elif gpa >= 7.0:
            return "Khá"
        elif gpa >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

    def display_info(self):
        gpa = self.calculate_gpa()
        rank = self.get_rank()
        print(f"[{self.student_id}] - {self.name}")
        print(f"  > Toán: {self.score_math} | Tin học: {self.score_it}")
        print(f"  > ĐTB: {gpa:.2f} -> Xếp loại: {rank}")
        print("-" * 30)


# --- Chạy thử nghiệm ---
# Tạo danh sách các sinh viên
student_list = [
    Student("Nguyễn Văn A", "DTHU01", 8.5, 9.0),
    Student("Trần Thị B", "DTHU02", 6.0, 7.5),
    Student("Lê Hoàng C", "DTHU03", 4.0, 5.0),
]

print("--- DANH SÁCH KẾT QUẢ HỌC TẬP SV ---")
for student in student_list:
    student.display_info()
