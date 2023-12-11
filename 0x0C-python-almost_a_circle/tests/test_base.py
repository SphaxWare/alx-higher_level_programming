import unittest
import turtle
from models.base import Base


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

    def test_save_to_file(self):
        Base.save_to_file([])
        with open('Base.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_load_from_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])


if __name__ == '__main__':
    unittest.main()
