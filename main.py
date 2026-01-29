def _get_avg_grade(grades):
    """Вспомогательная функция для расчета оценки"""
    if not grades:
        return 0
    all_grades = []
    for course_grades in grades.values():
        all_grades.extend(course_grades)
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

# Класс лекторов наследуется от Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) # Наследуем имя и фамилию
        self.grades = {} # Добавляем словарь для оценок лектору

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
    def __str__(self):
        return  f"Имя: {self.name}\nФамилия: {self.surname}"

# --- Тестирование ---
lecturer1 = Lecturer('Ivan', 'Ivanov')
lecturer2 = Lecturer('Petr', 'Petrov')
student1 = Student('Olya', 'Alekhina', 'F')

student1.courses_in_progress += ['Python']
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer2, 'Python', 8)

print(student1, "\n")
print(lecturer1, "\n")
print(f"Лектор 1 лучше Лектора 2? {lecturer1 > lecturer2}")