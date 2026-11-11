class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Course:
    def __init__(self, course_id, course_code, credits):
        self.course_id = course_id
        self.course_code = course_code
        self.credits = credits


class Enrollment:
    def __init__(self, enrollment_id, registration_date, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.registration_date = registration_date
        self.student_id = student_id
        self.course_id = course_id