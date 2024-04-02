from unittest import TestCase as TestCaseBase


class TestCase(TestCaseBase):
    def tearDown(self):
        super().tearDown()
