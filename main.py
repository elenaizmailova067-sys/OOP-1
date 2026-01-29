def _get_avg_grade(grades):
    if not grades:
        return 0
    all_grades = [grade for sublist in grades.values() for grade in sublist]
    return round(sum(all_grades) / len(all_grades), 1)

# 1. Функция подсчета средних оценок
def avg_grade_students(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)

def avg_grade_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg = _get_avg_grade(self.grades)
        in_progress = ", ".join(self.courses_in_progress)
        finished = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    # Сравнение студентов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение возможно только между студентами"
        return _get_avg_grade(self.grades) < _get_avg_grade(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg = _get_avg_grade(self.grades)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg}")

    # Сравнение лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравнение возможно только между лекторами"
        return _get_avg_grade(self.grades) < _get_avg_grade(other.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# 2. Создаем по 2 экземпляра каждого класса
student_1 = Student('Ruoy', 'Eman', 'm')
student_2 = Student('Olya', 'Alekhina', 'f')

lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_2 = Lecturer('Petr', 'Petrov')

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_2 = Reviewer('Expert', 'Pro')

# 3. Настройка связей и вызов методов
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Python', 'Git']

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

# Ревьюеры оценивают студентов (rate_hw)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Git', 9)

# Студенты оценивают лекторов (rate_lecture)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Python', 7)
student_1.rate_lecture(lecturer_2, 'Git', 10)

# 4. Проверка работы функций
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

print(f"Средняя оценка студентов по Python: {avg_grade_students(student_list, 'Python')}")
print(f"Средняя оценка лекторов по Python: {avg_grade_lecturers(lecturer_list, 'Python')}")

# Проверка __str__
print("\n--- Карточка студента ---")
print(student_1)

# Проверка сравнения
print(f"\nСтудент 1 учится лучше Студента 2? {student_1 > student_2}")