from grader.checkers import AbstractChecker, Fail
from grader.student import Student


class CheatingChecker(AbstractChecker):
    def __init__(self, thresh: int = 2):
        super().__init__()
        self.thresh = thresh

    def check(self, student: Student):
        if self.is_honest(student):
            return super().check(student)
        else:
            return Fail(self)

    def is_honest(self, student: Student) -> bool:
        cheating = []

        for task in student.tp:
            cheating.append(task.cheating)

        for task in student.td:
            cheating.append(task.cheating)

        cheating.append(student.final_exam.cheating)
        cheating.append(student.final_project.cheating)

        return True if sum(cheating) < self.thresh else False
