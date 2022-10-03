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
	# def __str__()

student = Student('Ruoy', 'Eman', 'Man')
student.finished_courses += ['Git']
student.courses_in_progress += ['Python']
student.grades['Git'] = [10, 10, 10, 10, 10]
student.grades['Python'] = [10, 10]

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
mentor = Reviewer('Alex', 'Smith')
mentor.courses_attached += ['Python']
student.rate_lecture(cool_mentor, 'Python', 4)
mentor.rate_hw(student, 'Python', 7)
print(cool_mentor.grades)
print(student.grades)
