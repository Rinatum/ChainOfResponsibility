from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union, Optional

from grader.student import Student


class Checker(ABC):
    @abstractmethod
    def set_next(self, checker):
        pass

    @abstractmethod
    def check(self, student: Student):
        pass


@dataclass
class Fail:
    failed_checker: Optional[Checker] = None

    def cause(self) -> str:
        if self.failed_checker:
            return f"Failed by {self.failed_checker.__class__.__name__}"
        else:
            return "Passed"


class AbstractChecker(Checker):
    _next_checker: Checker = None

    def set_next(self, checker: Checker) -> Checker:
        self._next_checker = checker
        return checker

    @abstractmethod
    def check(self, student: Student) -> Union[Student, Fail]:
        if self._next_checker:
            return self._next_checker.check(student)

        return Fail(None)
