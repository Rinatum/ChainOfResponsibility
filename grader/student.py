from dataclasses import dataclass
from typing import List


class Task:
    def __init__(self, grade: int, cheating: bool = False):
        self.grade = grade
        self.cheating = cheating


@dataclass
class Student:
    name: str
    mail: str

    tp: List[Task]
    td: List[Task]

    final_project: Task
    final_exam: Task

    attendance: List[bool]
