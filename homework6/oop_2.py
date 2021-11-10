"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from typing import Optional


class Person:
    """
    The class collect information

    Attributes:
        last_name (str): Last name
        first_name (str): First name
    """

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """
    The Homework class collect information about task and
    checking is it complete the task in time

    Attributes:
        text (str): description a task
        deadline (int): amount of days for work
        created (class datetime): current data and time of creation a task
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Checking if task in active, return True/False"""
        dead_line = self.deadline + datetime.datetime.now()
        if dead_line > datetime.datetime.now():
            return True
        else:
            return False


class DeadlineError(Exception):
    """Custom exception class for checking deadlines"""

    def __init__(self, text):
        self.text = text


class Student(Person):
    """
    The class collect information about student

    Attributes:
        last_name (str): Last name of student
        first_name (str): First name of student
    """

    def do_homework(self, homework: object, res: str) -> Optional:
        """Return object "homework" if work overdue"""
        try:
            if homework.is_active():
                return HomeworkResult(self, homework, res)
            else:
                raise DeadlineError("You are late")
        except DeadlineError:
            raise DeadlineError("You are late")


class HomeworkResult:
    """Class for collecting information about solution of homework"""

    def __init__(self, student, homework: object, solution: str):
        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = homework.created


class Teacher(Person):
    """
    The class collect information about teacher
        Class attributes:
            homework_done (defaultdict): collect unique value of checked homeworks
        Attributes:
            last_name (str): Last name of student
            first_name (str): First name of student
    """

    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, days: int) -> object:
        """Create an instance of Homework"""
        return Homework(text, days)

    def check_homework(self, homeworkresult: object) -> Optional:
        """Checking solution of homework, if ok -> add to homework_done else: False"""
        str_solution = homeworkresult.solution
        if len(str_solution) > 5:
            self.homework_done[homeworkresult.homework] = str_solution
        else:
            return False

    def reset_result(self, homework=0) -> None:
        """Delete homework from homework_done if no argument clear all values"""
        if homework == 0:
            self.homework_done.clear()
        else:
            self.homework_done.pop(homework)


# if __name__ == '__main__':
# opp_teacher = Teacher('Daniil', 'Shadrin')
# advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
#
# lazy_student = Student('Roman', 'Petrov')
# good_student = Student('Lev', 'Sokolov')
#
# oop_hw = opp_teacher.create_homework('Learn OOP', 1)
# docs_hw = opp_teacher.create_homework('Read docs', 5)
# #
# result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
# result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
# result_3 = lazy_student.do_homework(docs_hw, 'done,fddfdfdfdfdfdfdfd')
# # try:
# #     result_4 = HomeworkResult(good_student, "fff", "Solution")
# # except Exception:
# #     print('There was an exception here')
# temp_1 = opp_teacher.homework_done
# print(temp_1)
# #
# advanced_python_teacher.check_homework(result_2)
# opp_teacher.check_homework(result_1)
#
# print(temp_1)
# #
# opp_teacher.reset_result(homework=docs_hw)
# print(temp_1)
# # temp_2 = Teacher.homework_done
# # assert temp_1 == temp_2
# #
# # opp_teacher.check_homework(result_2)
# # opp_teacher.check_homework(result_3)
# #
# # print(Teacher.homework_done[oop_hw])
# # Teacher.reset_results()
