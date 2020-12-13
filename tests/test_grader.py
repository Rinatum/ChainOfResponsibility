import os
import pathlib

import pytest

from grader.parse import parse_students, parse_grader


@pytest.mark.parametrize(
    "grader_yaml_path, students_yaml_path, results",
    [
        ("templates/avg_tp_grader.yml", "templates/students.yml",
         ["Passed", "Failed by TpChecker"]),
        ("templates/max_tp_grader.yml", 'templates/students.yml',
         ["Passed", "Passed"]),
        ("templates/cheating_grader.yml", "templates/students.yml",
         ["Passed", "Failed by CheatingChecker"]),
    ],
)
def test_grader(grader_yaml_path, students_yaml_path, results):
    current_dir = pathlib.Path(__file__).parent.absolute()

    students = parse_students(os.path.join(current_dir, students_yaml_path))

    grader = parse_grader(os.path.join(current_dir, grader_yaml_path))

    grades = []
    for student in students:
        fail = grader.check(student)
        grades.append(fail.cause())

    assert grades == results
