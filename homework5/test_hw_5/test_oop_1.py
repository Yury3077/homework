import pytest

from homework5.oop_1 import Student, Teacher


def test_add_teacher_and_student():
    """Testing that class Teacher and Student add attributes"""
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    assert teacher.last_name == "Shadrin"
    assert student.first_name == "Roman"


def test_check_did_student_complete_the_task_on_time():
    """Tasting that created classes determine is it complete the task in time"""
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    expired_homework = teacher.create_homework("Learn functions", 0)
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert student.do_homework(oop_homework) == oop_homework
    assert student.do_homework(expired_homework) == "You are late"
