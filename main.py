from platform import android_ver


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        # Проверяем: лектор ли это, закреплен ли он за курсом и изучает ли студент этот курс
        if (isinstance(lecturer, Lecturer) and
            course in lecturer.courses_attached and
            course in self.courses_in_progress):

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс лекторов наследуется от Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) # Наследуем имя и фамилию
        self.grades = {} # Добавляем словарь для оценок лектору

# Класс экспертов наследуется от Mentor
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
# --- Тестирование ---
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None (успешно)
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка (лектор не ведет Java)
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка (студент не учит C++)
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка (ревьюера нельзя оценивать)

print(lecturer.grades)  # {'Python': [7]}