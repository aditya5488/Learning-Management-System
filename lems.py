# Learning Management System - Version 1.1
# Features: enroll and complete courses, fee calculation

def enroll_course(course_id, student_id):
    print("Student", student_id, "enrolled in course", course_id)

def complete_course(course_id, student_id):
    print("Student", student_id, "completed course", course_id)

def calculate_fee(course_fee, discount=0):
    fee = course_fee - discount
    print("Course Fee = Rs.", fee)
    return fee

