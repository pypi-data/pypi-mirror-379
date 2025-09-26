import json
import unittest
from collections import Counter

from bunch.bunch import Bunch


class TestBunch(unittest.TestCase):
    def test_getitem(self):
        b = Bunch(name='Alice', age=30)
        self.assertEqual(b['name'], 'Alice')

    def test_setitem(self):
        b = Bunch(name='Alice')
        b['age'] = 30
        self.assertEqual(b.age, 30)

    def test_delitem(self):
        b = Bunch(name='Alice', age=30)
        del b['name']
        self.assertEqual(b.name, None)

    def test_contains(self):
        b = Bunch(name='Alice', age=30)
        self.assertTrue('name' in b)
        self.assertFalse('location' in b)

    def test_str(self):
        b = Bunch(name='Alice', age=30)
        expected_str = json.dumps({'name': 'Alice', 'age': 30})
        self.assertEqual(b.__str__(), expected_str)

    def test_repr(self):
        b = Bunch(name='Alice', age=30)
        expected_repr = json.dumps({'name': 'Alice', 'age': 30})
        self.assertEqual(b.__repr__(), expected_repr)

    def test_getattr(self):
        b = Bunch(name='Alice', age=30)
        self.assertEqual(b.age, 30)

    def test_setattr(self):
        b = Bunch(name='Alice', age=30)
        b.age = 40
        b.location = 'New York'
        self.assertEqual(b.age, 40)
        self.assertEqual(b.location, 'New York')

    def test_delattr(self):
        b = Bunch(name='Alice', age=30)
        del b.age
        self.assertEqual(b.age, None)

    def test_contains_value(self):
        b = Bunch(name='Alice', age=30)
        self.assertTrue(b.contains_value('Alice'))
        self.assertFalse(b.contains_value('Bob'))

    def test_clear(self):
        b = Bunch(name='Alice', age=30)
        b.clear()
        self.assertEqual(len(b.keys()), 0)

    def test_pop(self):
        b = Bunch(name='Alice', age=30)
        popped_value = b.pop('name')
        self.assertEqual(popped_value, 'Alice')
        self.assertEqual(b.name, None)

    def test_popitem(self):
        b = Bunch(name='Alice', age=30)
        popped_value = b.popitem()
        self.assertEqual(popped_value, ('age', 30))
        self.assertEqual(b.age, None)

    def test_update(self):
        b = Bunch(name='Alice', age=30)
        d = {'name': 'Bob', 'age': 35}
        b.update(d)
        self.assertEqual(d['name'], 'Bob')
        self.assertEqual(d['age'], 35)

    def test_setdefault(self):
        b = Bunch(name='Alice', age=30)
        b.setdefault('location')
        self.assertEqual(b.location, None)

    def test_keys(self):
        b = Bunch(name='Alice', age=30)
        self.assertEqual(Counter(b.keys()), Counter(['name', 'age']))

    def test_values(self):
        b = Bunch(name='Alice', age=30)
        self.assertEqual(Counter(b.values()), Counter(['Alice', 30]))

    def test_items(self):
        b = Bunch(name='Alice', age=30)
        self.assertEqual(Counter(b.items()), Counter([('name', 'Alice'), ('age', 30)]))

    def test_from_dict(self):
        data = {'fruit': 'apple', 'color': 'red'}
        b = Bunch.from_dict(data)
        self.assertEqual(b.fruit, 'apple')
        self.assertEqual(b.color, 'red')

    def test_from_dict_recursive_nested(self):
        data = {
            'user': {
                'name': 'Alice',
                'profile': {'age': 30, 'city': 'Paris'}
            }
        }
        b = Bunch.from_dict(data, recursive=True)

        self.assertIsInstance(b.user, Bunch)
        self.assertIsInstance(b.user.profile, Bunch)
        self.assertEqual(b.user.profile.city, 'Paris')

    def test_from_dict_recursive_deeply_nested(self):
        data = {'level1': {'level2': {'level3': {'value': 42}}}}
        b = Bunch.from_dict(data, recursive=True)

        self.assertEqual(b.level1.level2.level3.value, 42)
        self.assertIsInstance(b.level1.level2, Bunch)
        self.assertIsInstance(b.level1.level2.level3, Bunch)

    def test_from_dict_with_list_of_dicts(self):
        data = {
            'users': [
                {'name': 'Alice', 'age': 30},
                {'name': 'Bob', 'age': 25}
            ]
        }
        b = Bunch.from_dict(data, recursive=True)

        self.assertIsInstance(b.users[0], Bunch)
        self.assertEqual(b.users[0].name, 'Alice')
        self.assertEqual(b.users[1].age, 25)

    def test_from_dict_recursive_false(self):
        data = {
            'user': {
                'name': 'Alice',
                'profile': {'age': 30}
            }
        }
        b = Bunch.from_dict(data, recursive=False)

        self.assertIsInstance(b.user, dict)
        self.assertEqual(b.user['profile']['age'], 30)

if __name__ == '__main__':
    unittest.main()
