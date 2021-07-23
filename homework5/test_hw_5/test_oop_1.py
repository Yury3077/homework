import pytest

from homework5.oop_1 import Student, Teacher


def test_add_class_teacher():
    """Testing that class Teacher add attributes"""
    teacher = Teacher("Shadrin", "Daniil")
    assert teacher.last_name == "Shadrin"


def test_add_student():
    """Testing that class Teacher and Student add attributes"""
    student = Student("Petrov", "Roman")
    assert student.first_name == "Roman"


def test_check_did_student_complete_the_task_on_time():
    """Tasting that created classes determine is it complete the task in time"""
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    oop_homework = teacher.create_homework("create 2 simple classes", 5)
    assert student.do_homework(oop_homework) == oop_homework


def test_check_did_student_late_to_do_homework():
    """Tasting that created classes determine is it complete the task in time"""
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert student.do_homework(expired_homework) == "You are late"
