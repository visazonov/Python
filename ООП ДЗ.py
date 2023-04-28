class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade >= 1 and grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return print('Ошибка введите оценку от 1 до 10')
                # a = f'Ошибка введите оценку от 1 до 10'
                # return a
        else:
            return print('Ошибка')

    def _average_rating(self):
        hw_grades = []
        for grade in self.grades.values():
            hw_grades += grade
            average = sum(hw_grades) / len(hw_grades)
            return average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('not Student')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self._average_rating()} \n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)} \n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self):
        hw_grades = []
        for grade in self.grades.values():
            hw_grades += grade
            average = sum(hw_grades) / len(hw_grades)
            return average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('not Lecturer')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self._average_rating()}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


anton_martunov = Student('Anton', 'Martunov', 'm')
anton_martunov.courses_in_progress.append('python')
anton_martunov.courses_in_progress.append('git')
anton_martunov.finished_courses.append('Введение в программирование')
# print(anton_martunov.name)
# print(anton_martunov.surname)
# print(anton_martunov.courses_in_progress)

masha_belova = Student('Marya', 'Belova', 'f')
masha_belova.courses_in_progress.append('python')
masha_belova.courses_in_progress.append('git')
# print(masha_belova.name)
# print(masha_belova.surname)
# print(masha_belova.courses_in_progress)

dmitry_mendeleev = Lecturer('Dmitry', 'Mendeleev')
# print(dmitry_mendeleev.name)
# print(dmitry_mendeleev.surname)
dmitry_mendeleev.courses_attached.append('python')
dmitry_mendeleev.courses_attached.append('git')
# print(dmitry_mendeleev.courses_attached)

michail_lomonosov = Lecturer('Michail', 'Lomonosov')
# print(michail_lomonosov.name)
# print(michail_lomonosov.surname)
michail_lomonosov.courses_attached.append('python')
michail_lomonosov.courses_attached.append('git')
# print(michail_lomonosov.courses_attached)

igor_kurchatov = Reviewer('Igor', 'Kurchatov')
# print(igor_kurchatov.name)
# print(igor_kurchatov.surname)
igor_kurchatov.courses_attached.append('python')
igor_kurchatov.courses_attached.append('git')
# print(igor_kurchatov.courses_attached)

sergey_korolev = Reviewer('Sergey', 'Korolev')
# print(sergey_korolev.name)
# print(sergey_korolev.surname)
sergey_korolev.courses_attached.append('python')
sergey_korolev.courses_attached.append('git')
# print(sergey_korolev.courses_attached)


# оценки ревьюэров студентам
# anton_martunov.grades = {}
igor_kurchatov.rate_hw(anton_martunov, "git", 5)
igor_kurchatov.rate_hw(masha_belova, "git", 3)
igor_kurchatov.rate_hw(anton_martunov, "python", 5)
igor_kurchatov.rate_hw(masha_belova, "python", 4)
sergey_korolev.rate_hw(anton_martunov, "git", 5)
sergey_korolev.rate_hw(masha_belova, "git", 5)
sergey_korolev.rate_hw(anton_martunov, "python", 5)
sergey_korolev.rate_hw(masha_belova, "python", 5)
print(anton_martunov.grades)
print(masha_belova.grades)


# оценки студентов лекторам
# dmitry_mendeleev.grades = {}
anton_martunov.rate_hw(dmitry_mendeleev, "python", 7)
anton_martunov.rate_hw(michail_lomonosov, "python", 10)
masha_belova.rate_hw(dmitry_mendeleev, "python", 9)
masha_belova.rate_hw(michail_lomonosov, "python", 10)
anton_martunov.rate_hw(dmitry_mendeleev, "git", 7)
anton_martunov.rate_hw(michail_lomonosov, "git", 10)
masha_belova.rate_hw(dmitry_mendeleev, "git", 9)
masha_belova.rate_hw(michail_lomonosov, "git", 10)
print(dmitry_mendeleev.grades)
print(michail_lomonosov.grades)


# Задание 3
print(igor_kurchatov)
print(dmitry_mendeleev)

print(anton_martunov)

# сравнение студентов по средней оценке
print(anton_martunov < masha_belova)
print(anton_martunov.__lt__(masha_belova))

# сравнение лекторов по средней оценке
print(dmitry_mendeleev < michail_lomonosov)
print(dmitry_mendeleev.__lt__(michail_lomonosov))


# Задание 4 средняя оценка по всем студентам
students = [anton_martunov, masha_belova]
# course = ['python', 'git']
def av_rat_student(list_students, name_course):
    list_rating = []
    for student in list_students:
        print(student.grades)
        for key, value in student.grades.items():
            if name_course in key:
                list_rating += value
                print(list_rating)
        average_rating_student = round(sum(list_rating) / len(list_rating), 2)
    return average_rating_student


# av_rat_student(students, 'git')
# av_rat_student(students, 'python')
print(av_rat_student(students, 'git'))
print(av_rat_student(students, 'python'))



# Задание 4 средняя оценка по всем лекторам
lecturers = [dmitry_mendeleev, michail_lomonosov]
# course = ['python', 'git']
def av_rat_lecturer(list_lecturers, name_course):
    list_rating = []
    for lecturer in list_lecturers:
        print(lecturer.grades)
        for key, value in lecturer.grades.items():
            if name_course in key:
                list_rating += value
                print(list_rating)
        average_rating_lecturer = round(sum(list_rating) / len(list_rating), 2)
    return average_rating_lecturer


av_rat_lecturer(lecturers, 'git')
# av_rat_lecturer(lecturers, 'python')

# Средняя оценка по всем студентам универсальная с любым списком курсов
students = [anton_martunov, masha_belova]
course = ['python', 'git']
def av_rat_student(list_students, name_course):
  a_r_s = {}
  for course in name_course:
    list_rating = []
    for student in list_students:
      for key, value in student.grades.items():
        if course in key:
          list_rating += value
    average_rating_student = round(sum(list_rating) / len(list_rating), 2)
    a_r_s[course] = average_rating_student
    print(average_rating_student)
  return a_r_s

av_rat_student(students, course)