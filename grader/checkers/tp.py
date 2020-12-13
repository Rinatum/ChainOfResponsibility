from typing import List

from grader.checkers import AbstractChecker, Fail
from grader.student import Student, Task


class TpChecker(AbstractChecker):
    def __init__(self, thresh: int = 56):
        super().__init__()
        self.thresh = thresh

    def check(self, student: Student):
        if self.is_tp_pass(student.tp):
            return super().check(student)
        else:
            return Fail(self)

    def is_tp_pass(self, tp: List[Task]) -> bool:
        grades = [task.grade for task in tp]
        mean = sum(grades) / len(grades)
        return True if mean > self.thresh else False


class TpMaxChecher(TpChecker):
    def is_tp_pass(self, tp: List[Task]) -> bool:
        grades = [task.grade for task in tp]
        max_grade = max(grades)
        return True if max_grade > self.thresh else False
