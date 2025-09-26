class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Оценка должна быть от 0 до 10")
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")
        print("-" * 20)

# Демонстрация работы
student1 = Student("Иван Иванов", "12345")
student1.add_grade(8)
student1.add_grade(9)
student1.add_grade(7)
student1.add_grade(15)  # Невалидная оценка
student1.display_info()
