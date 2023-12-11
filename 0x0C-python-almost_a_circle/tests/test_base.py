import unittest
import turtle
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for base"""

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Tests custom int id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_create_instance(self):
        b = Base()
        self.assertEqual(b.id, 7)

    def test_create_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 8)
        self.assertEqual(b2.id, 9)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')


    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])
        self.assertEqual(Base.to_json_string([{'id': 1, 'x': 2, 'y': 3}]),
                                               '[{"id": 1, "x": 2, "y": 3}]')

    def test_save_to_file(self):
        Base.save_to_file([])
        with open('Base.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_load_from_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])


if __name__ == '__main__':
    unittest.main()
