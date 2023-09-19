class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3)

    def test_list_all_integer(self):
        integer = IntegerList(4, 5, 6)
        self.assertEquals(3, len(integer.get_data()))
        self.assertEquals(3, len(integer._IntegerList__data))

    def test_get_data(self):
        integer = IntegerList(4, 5, 6)
        self.assertEqual([4, 5, 6], integer.get_data())

    def test_int_not_integer(self):
        integer = IntegerList(4, 5, 6.5)
        self.assertEqual(2, len(integer.get_data()))

    def test_int_not_integer_exact_el(self):
        integer = IntegerList(4, 5, 6.5)
        self.assertEqual([4, 5], integer.get_data())

    def test_add_mention_not_int(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        test_data_values = [3.5, 'asd', {}, [], False]
        for v in test_data_values:
            with self.assertRaises(ValueError) as ex:
                self.int_list.add(v)

        self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(3, len(self.int_list.get_data()))

    def test_add_mention_add_int_adds_the_element(self):
        self.assertEqual(3, len(self.int_list.get_data()))

        result = self.int_list.add(5)
        self.assertEqual(4, len(self.int_list.get_data()))
        self.assertIn(5, self.int_list.get_data())
        self.assertEqual([1, 2, 3, 5], result)

    def test_remove_index_invalid_index_raises_exception(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(5)

            self.assertEqual('Index is out of range', str(ex.exception))
            self.assertEqual(3, len(self.int_list.get_data()))

    def test_remove_index_remove_element(self):
        self.assertEqual(3, len(self.int_list.get_data()))
        self.assertEquals(1, self.int_list.get_data()[0])

        result = self.int_list.remove_index(0)

        self.assertEquals(1, result)
        self.assertEqual(2, len(self.int_list.get_data()))
        self.assertEquals(2, self.int_list.get_data()[0])

    def test_get_invalid_index(self):
        self.assertEquals(3, len(self.int_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.int_list.get(4)
        self.assertEquals("Index is out of range", str(ex.exception))

    def test_get_by_index(self):
        self.assertEqual(3, len(self.int_list.get_data()))
        el = self.int_list.get(1)
        self.assertEqual(2, el)

    def test_insert_invalid_index_raises(self):
        self.assertEquals(3, len(self.int_list.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(4, 5)
        self.assertEquals("Index is out of range", str(ex.exception))
        self.assertEquals(3, len(self.int_list.get_data()))

    def test_insert_element_not_int_raises(self):
        self.assertEquals(3, len(self.int_list.get_data()))

        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(0, 5.3)
        self.assertEquals("Element is not Integer", str(ex.exception))
        self.assertEquals(3, len(self.int_list.get_data()))

    def test_insert(self):
        self.assertEquals(3, len(self.int_list.get_data()))
        self.assertEqual([1, 2, 3], self.int_list.get_data())
        self.assertEquals([1, 2, 3], self.int_list._IntegerList__data)

        self.int_list.insert(0, 100)

        self.assertEquals(4, len(self.int_list.get_data()))
        self.assertEqual([100, 1, 2, 3], self.int_list.get_data())
        self.assertEquals([100, 1, 2, 3], self.int_list._IntegerList__data)

    def test_get_biggest(self):
        my_list = IntegerList(0, 12, - 3)
        result = my_list.get_biggest()
        self.assertEqual(12, result)

    def test_get_index(self):
        self.assertEqual(self.int_list.get_data()[0], 1)

        result = self.int_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
