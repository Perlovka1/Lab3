class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Ошибка: оценка должна быть от 0 до 10")
    
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")
    
    def __str__(self):
        return f"Student(name='{self.name}', id={self.student_id}, grades={self.grades})"
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
    
    def __len__(self):
        return len(self.grades)

# Пример использования
student1 = Student("Иван Иванов", "12345")
student2 = Student("Петр Петров", "12345")
student3 = Student("Анна Сидорова", "67890")

student1.add_grade(8)
student1.add_grade(9)
student1.add_grade(7)

print(student1)
print(f"Количество оценок: {len(student1)}")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 == student3: {student1 == student3}")