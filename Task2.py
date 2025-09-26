class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Студент {student.name} добавлен к преподавателю {self.name}")
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удален у преподавателя {self.name}")
        else:
            print("Студент не найден")
    
    def list_students(self):
        print(f"Студенты преподавателя {self.name} ({self.subject}):")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")