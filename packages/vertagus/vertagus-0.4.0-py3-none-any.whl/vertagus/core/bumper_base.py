from abc import ABC, abstractmethod


class BumperABC(ABC):
    name = "base"
    inject_scm: bool = False

    @abstractmethod
    def bump(self, version: str, *args, **kwargs) -> str:
        pass


class BumperBase(BumperABC):
    def __init__(self, *args):
        pass


class BumperException(ValueError):
    """
    Base exception for all bumper-related errors.
    """

    pass
