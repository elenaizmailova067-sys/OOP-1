class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс лекторов наследуется от Mentor
class Lecturer(Mentor):
    pass
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
# Проверка реализации

# Создаем эксперта (Reviewer)
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

# Создаем лектора (Lecturer)
some_lecturer = Lecturer('Ivan', 'Ivanov')
some_lecturer.courses_attached += ['Python']

# Создаем студента
some_student = Student('Ruoy', 'Eman', 'm')
some_student.courses_in_progress += ['Python']

# Проверяющий выставляет оценку
some_reviewer.rate_hw(some_student, 'Python', 10)

print(f"Имя ревьюера: {some_reviewer.name}")
print(f"Имя лектора: {some_lecturer.name}")
print(f"Оценки студента: {some_student.grades}")