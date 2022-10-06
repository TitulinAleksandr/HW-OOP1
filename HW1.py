class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_fin_courses(self, course_name):
        self.finished_courses.append(course_name)   
    def add_prog_courses(self, course_name):
        self.courses_in_progress.append(course_name)
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
student1 = Student('Ben', 'Smit', 'man')
student1.add_prog_courses('Python')
student1.add_prog_courses('Git')
student1.add_fin_courses('Введение в программирование')
student2 = Student('Gina', 'Adamson', 'woman')
student2.add_prog_courses('JavaScript')
student2.add_prog_courses('html')
student2.add_fin_courses('Английский для программистов')
lecturer1 = Lecturer('Василий', 'Иванов')
lecturer1.add_courses('Python')
lecturer1.add_courses('Git')
lecturer2 = Lecturer('Иван', 'Абрамов')
lecturer2.add_courses('JavaScript')
lecturer2.add_courses('html')
reviewer1 = Reviewer('Анна', 'Петрова')
reviewer1.add_courses('Python')
reviewer1.add_courses('Git')
reviewer2 = Reviewer('Екатерина', 'Кротова')
reviewer2.add_courses('JavaScript')
reviewer2.add_courses('html')
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 4)
reviewer2.rate_hw(student2, 'JavaScript', 6)
reviewer2.rate_hw(student2, 'html', 10)
reviewer2.rate_hw(student2, 'JavaScript', 9)
reviewer2.rate_hw(student2, 'html', 7)
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 7)
student1.rate_lecture(lecturer1, 'Git', 8)
student1.rate_lecture(lecturer1, 'Git', 10)
student2.rate_lecture(lecturer2, 'JavaScript', 9)
student2.rate_lecture(lecturer2, 'JavaScript', 6)
student2.rate_lecture(lecturer2, 'html', 10)
student2.rate_lecture(lecturer2, 'html', 7)
# print(student1.stud_av())
# print(student2.stud_av())
# print(student1)
# print(student2)
# print(lecturer1)
# print(lecturer2)
# print(reviewer1)
# print(reviewer2)
# print(student1 < lecturer1)
# print(student2 > lecturer2)
students_list = [student1, student2]
def grade_av(students_list, course):
    sum = 0
    count = 0
    for x in students_list:
        for y in x.grades[course]:
            sum += y
            count += 1
    return round(sum/count, 1)

lecturers_list = [lecturer1, lecturer2]
def rating_al(lecturers_list, course):
    sum = 0
    count = 0
    for x in lecturers_list:
        for y in x.grades1[course]:
            sum += y
            count += 1
    return round(sum/count, 1)

print(grade_av(students_list, 'Python'))
print(rating_al(lecturers_list, 'Python'))
