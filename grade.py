import argparse

from grader.parse import parse_grader, parse_students

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--students", type=str, help="Path to .yml file with students description"
    )
    parser.add_argument(
        "--grader", type=str,  help="Path to .yml file with grader settings"
    )
    args = parser.parse_args()

    students = parse_students(args.students)

    grader = parse_grader(args.grader)

    for student in students:
        fail = grader.check(student)
        print(f"{student.name} - {fail.cause()}")
