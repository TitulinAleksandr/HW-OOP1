import sys
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
    def stud_av(self):
        sum_ = 0
        count = []
        for x in self.grades.values():
            sum_ += sum(x) / len(x)
            count.append(x)
        result = round(sum_ / len(count), 1)
        return result
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.stud_av()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого студента нет.')
            return
        return self.stud_av() < other.lec_av()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def add_courses(self, course_name):
        self.courses_attached.append(course_name)     
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) 
        self.grades = {}
    def lec_av(self):
        sum_ = 0
        count = []
        for x in self.grades.values():
            sum_ += sum(x) / len(x)
            count.append(x)
        result = round(sum_ / len(count), 1)
        return result
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lec_av()}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет.')
            return
        return self.lec_av() < other.stud_av()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
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
student = Student('Ruoy', 'Eman', 'Man')
student.finished_courses += ['Git']
student.courses_in_progress += ['Python']
student.courses_in_progress += ['GH']
student.grades['Git'] = [10, 10, 10, 10, 10]
student.grades['Python'] = [10, 10]

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['GH']
mentor = Reviewer('Alex', 'Smith')
mentor.courses_attached += ['Python']
mentor.courses_attached += ['GH']
student.rate_lecture(cool_mentor, 'Python', 4)
student.rate_lecture(cool_mentor, 'GH', 7)
mentor.rate_hw(student, 'Python', 7)
mentor.rate_hw(student, 'Python', 4)
mentor.rate_hw(student, 'Python', 9)
mentor.rate_hw(student, 'Python', 1)
student.rate_lecture(cool_mentor, 'Python', 8)
student.rate_lecture(cool_mentor, 'GH', 9)




