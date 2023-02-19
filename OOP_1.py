class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Метод, который выставляет оценки лекторам за лекции"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_score = self.av_score()
        courses_progres = ', '.join(self.courses_in_progress)
        courses_end = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {average_score}\nКурсы в процессе изучения: {courses_progres}\nЗавершенные курсы: {courses_end}'
        return res

    def av_score(self):
        '''метод подсчета среднего балла за предмет'''
        summa = 0
        count = 0
        for i in self.grades.keys():
            for j in self.grades[i]:
                summa += j
                count += 1
        return round(summa / count, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.av_score() < other.av_score()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.av_score() > other.av_score()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.av_score() == other.av_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def av_score(self):
        '''метод подсчета среднего балла за лекции'''
        summa = 0
        count = 0
        for i in self.grades.keys():
            for j in self.grades[i]:
                summa += j
                count += 1
        return round(summa / count, 1)

    def __str__(self):
        average_score = self.av_score()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_score}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.av_score() < other.av_score()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.av_score() > other.av_score()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.av_score() == other.av_score()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_score_hw(stud_list, course):
    '''
    Функция возвращает F-строку со средним баллом за курс,
    на входе функция принимает 2 параметра: список студентов и название курса.
    '''
    aver_score = 0
    count = 0
    for i in stud_list:
        if course in i.grades.keys() and isinstance(i, Student): # защита от ошибок, и проверка на соответствиее класса
            for j in i.grades[course]:
                aver_score += j
                count += 1
        else:
            continue
    if aver_score > 0:
        res = round(aver_score / count, 1)
        res_score = f'Средний балл за домашние задания на курсе {course}: {res}'
        return res_score
    else:
        res_not_score = f'Оценки за домашнее задание на курсе {course} не проставлены!'
        return res_not_score

def average_score_lect(lect_list, course):
    '''
        Функция возвращает F-строку со средним баллом за курс,
        на входе функция принимает 2 параметра: список лекторов и название курса.
        '''
    aver_score = 0
    count = 0
    for i in lect_list:
        if course in i.grades.keys() and isinstance(i, Lecturer):  # защита от ошибок, и проверка на соответствиее класса
            for j in i.grades[course]:
                aver_score += j
                count += 1
        else:
            continue
    if aver_score > 0:
        res = round(aver_score / count, 1)
        res_score = f'Средняя оценка за лекции на курсе {course}: {res}'
        return res_score
    else:
        res_not_score = f'Оценки за лекции на курсе {course} не проставлены!'
        return res_not_score


cool_lecturer_Python = Lecturer('Иван', 'Иванов')
cool_lecturer_Python.courses_attached += ['Python']
cool_lecturer_Python.courses_attached += ['GIT']

bad_lecturer_Python = Lecturer('Петя', 'Петров')
bad_lecturer_Python.courses_attached += ['Python']
bad_lecturer_Python.courses_attached += ['GIT']

best_student = Student('Ruoy', 'Eman')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['JS']

bad_student = Student('Коля', 'Николаев')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['GIT']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['GIT']

cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student, 'GIT', 7)
cool_mentor.rate_hw(best_student, 'GIT', 7)

cool_mentor.rate_hw(bad_student, 'Python', 4)
cool_mentor.rate_hw(bad_student, 'Python', 4)
cool_mentor.rate_hw(bad_student, 'Python', 4)
cool_mentor.rate_hw(bad_student, 'Python', 4)

cool_mentor.rate_hw(bad_student, 'GIT', 10)
cool_mentor.rate_hw(bad_student, 'GIT', 10)

best_student.rate_lecture(cool_lecturer_Python, 'Python', 9)
best_student.rate_lecture(cool_lecturer_Python, 'Python', 10)
best_student.rate_lecture(cool_lecturer_Python, 'Python', 9)

best_student.rate_lecture(bad_lecturer_Python, 'Python', 5)
best_student.rate_lecture(bad_lecturer_Python, 'Python', 5)
best_student.rate_lecture(bad_lecturer_Python, 'Python', 5)

student_list = [bad_student, best_student]
lectures_list = [cool_lecturer_Python, bad_lecturer_Python]

print(cool_mentor)
print()
print(bad_lecturer_Python)
print()
print(bad_student)
print()
print(bad_student < best_student)
print()
print(cool_lecturer_Python > bad_lecturer_Python)
print()
print(average_score_lect(lectures_list, 'Python'))
print()
print(average_score_hw(student_list, 'GIT'))