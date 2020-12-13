import pytest

from grader.parse import parse_students, parse_grader


@pytest.mark.parametrize(
    "grader_yaml_path, students_yaml_path, results",
    [
        ("tests/templates/avg_tp_grader.yml", "tests//templates/students.yml", ["Passed", "Failed by TpChecker"]),
        ("tests/templates/max_tp_grader.yml", 'tests//templates/students.yml', ["Passed", "Passed"]),
        ("tests/templates/cheating_grader.yml", "tests//templates/students.yml",["Passed", "Failed by CheatingChecker"]),
    ],
)
def test_grader(grader_yaml_path, students_yaml_path, results):
    students = parse_students(students_yaml_path)

    grader = parse_grader(grader_yaml_path)

    grades = []
    for student in students:
        fail = grader.check(student)
        grades.append(fail.cause())

    assert grades == results
