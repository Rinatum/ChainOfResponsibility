from typing import List

from grader.checkers import AbstractChecker, Fail
from grader.student import Student


class AttendanceChecker(AbstractChecker):
    def __init__(self, thresh: int = 5):
        super().__init__()
        self.thresh = thresh

    def check(self, student: Student):
        if self.is_attendance_enough(student.attendance):
            return super().check(student)
        else:
            return Fail(self)

    def is_attendance_enough(self, attendance: List[bool]) -> bool:
        return True if sum(attendance) > self.thresh else False
