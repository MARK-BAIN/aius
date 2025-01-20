import unittest
from aius.beings.being import Being

class TestBeingClass(unittest.TestCase):

    def test_init(self):
        being = Being()
        self.assertIsNotNone(being.id)
        self.assertRegex(being.id, r'^Aius-Being-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    def test_hash(self):
        being1 = Being()
        being2 = Being()
        self.assertNotEqual(hash(being1), hash(being2))

    def test_repr(self):
        being = Being()
        self.assertEqual(repr(being), being.id)

    def test_str(self):
        being = Being()
        self.assertEqual(str(being), being.id)

    def test_get_id(self):
        being = Being()
        with self.assertRaises(TypeError):
            Being.get_id()

if __name__ == '__main__':
    unittest.main()