from collections import defaultdict
from typing import Optional

import pytest

from homework6.oop_2 import Student, Teacher


def test_add_class_teacher():
    """Testing that class Teacher add attributes"""
    teacher = Teacher("Shadrin", "Daniil")
    assert teacher.last_name == "Shadrin"


def test_add_student():
    """Testing that class Teacher and Student add attributes"""
    student = Student("Petrov", "Roman")
    assert student.first_name == "Roman"


def test_checking_homework_not_add_to_homework_done():
    web_teacher = Teacher("Lobov", "Kurafeeva")
    lazy_student_1 = Student("Den", "Kavyar")
    oop_hw_1 = web_teacher.create_homework("dics", 3)
    result_3 = lazy_student_1.do_homework(oop_hw_1, "Done")
    web_teacher.check_homework(result_3)
    assert web_teacher.homework_done == defaultdict(set)


def test_checking_the_same_hw_two_times():
    advanced_python_teacher = Teacher("Roman", "Beltikov")
    good_student = Student("Yury", "Balykov")
    oop_hw_2 = advanced_python_teacher.create_homework("Learn OOP", 1)
    result_1 = good_student.do_homework(oop_hw_2, "I have done this hw")
    result_2 = good_student.do_homework(oop_hw_2, "I have done this hw too")
    advanced_python_teacher.check_homework(result_1)
    advanced_python_teacher.check_homework(result_2)
    defult_d = defaultdict(set)
    defult_d[result_2.homework] = result_2.solution
    assert advanced_python_teacher.homework_done == defult_d


def test_clean_oop2_hw_2_from_howework_done():
    advanced_python_teacher = Teacher("Roman", "Beltikov")
    advanced_python_teacher.reset_result()
    assert advanced_python_teacher.homework_done == defaultdict(set)


def test_add_two_value_into_homework_done_dict():
    teacher_1 = Teacher("Somename", "Somesey0")
    student_1 = Student("nan", "fun")
    some_task = teacher_1.create_homework("Do something important", 10)
    res_1 = student_1.do_homework(some_task, "hei, i did it fast")
    teacher_1.check_homework(res_1)
    defoult_dict_ = defaultdict(set)
    defoult_dict_[res_1.homework] = res_1.solution
    assert teacher_1.homework_done == defoult_dict_
