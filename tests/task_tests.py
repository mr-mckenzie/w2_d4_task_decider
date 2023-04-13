import unittest
from src.Task import Task
from src.task_decider import *

class TestTasks(unittest.TestCase):

    def setUp(self):
        self.dishes = Task("wash dishes", 10)
        self.cook = Task("cook dinner", 10)
        self.windows = Task("clean windows", 10)
        self.ironing = Task("do ironing", 10)
        self.clothes = Task("wash clothes", 10)

    def test_has_description(self):
        self.assertEqual("cook dinner", self.cook.description)

    def test_has_duration(self):
        self.assertEqual(10, self.dishes.duration)

    def test_wash_cook__ordinary(self):
        self.assertEqual(self.dishes, get_preferred_option(self.dishes, self.cook))

    def test_wash_cook__reverse(self):
        self.assertEqual(self.dishes, get_preferred_option(self.cook, self.dishes))

    def test_same_imput_task(self):
        self.assertEqual(self.windows, get_preferred_option(self.windows, self.windows))

    def test_unknown_task__ordinary(self):
        new_task = Task("walk the dog", 50)
        self.assertEqual(None, get_preferred_option(self.cook, new_task))

    def test_unknown_task__reverse(self):
        new_task = Task("walk the dog", 50)
        self.assertEqual(None, get_preferred_option(new_task, self.cook))

    