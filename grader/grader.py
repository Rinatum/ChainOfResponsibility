from typing import List

from grader.student import Student
from grader.checkers import AbstractChecker


class Grader:
    def __init__(self, checkers: List[AbstractChecker]):
        self.checking_pipeline = checkers[0]
        for i in range(len(checkers) - 1):
            checkers[i].set_next(checkers[i + 1])

    def check(self, student: Student):
        return self.checking_pipeline.check(student)
