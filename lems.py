# Learning Management System - Version 2.0
# Features: enroll/complete courses, fee calculation, online course search

catalogue = ["Python", "DBMS", "Operating Systems"]

def enroll_course(course_id, student_id):
    print("Student", student_id, "enrolled in course", course_id)

def complete_course(course_id, student_id):
    print("Student", student_id, "completed course", course_id)

def calculate_fee(course_fee, discount=0):
    fee = course_fee - discount
    print("Course Fee = Rs.", fee)
    return fee

def search_course(title):
    if title in catalogue:
        print(title, "is available")
    else:
        print(title, "not found")

