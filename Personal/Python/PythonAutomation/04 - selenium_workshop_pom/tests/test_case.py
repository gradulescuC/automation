from abc import ABC


class TestCaseModel(ABC):
    def setup(self):
        raise NotImplemented

    def run(self):
        raise NotImplemented

    def tear_down(self):
        raise NotImplemented