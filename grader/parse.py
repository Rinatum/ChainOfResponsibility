from typing import List

import yaml

from grader import checkers
from grader.student import Student, Task
from grader.checkers import AbstractChecker
from grader.grader import Grader

CHECKERS: dict = {
    k: v
    for k, v in checkers.__dict__.items()
    if isinstance(v, type) and issubclass(v, AbstractChecker)
}


def parse_students(yaml_path) -> List[Student]:
    with open(yaml_path) as f:
        students = yaml.safe_load(f)

    for student in students:
        student["tp"] = [Task(**tp) for tp in student["tp"]]
        student["td"] = [Task(**tp) for tp in student["td"]]
        student["final_project"] = Task(**student["final_project"])
        student["final_exam"] = Task(**student["final_exam"])

    return [Student(**student) for student in students]


def parse_grader(yaml_path) -> Grader:
    with open(yaml_path) as f:
        grader = yaml.safe_load(f)

    checkers_: List[AbstractChecker] = [CHECKERS[checker["class"]](**checker["params"]) for checker in grader]

    return Grader(checkers_)
