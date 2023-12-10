#!/usr/bin/python3

import math
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """Test the Base Model 'instantiation' method"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_instances_no_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_Id(self):
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b2.id, b3.id - 1)

    def test_unique_Id(self):
        b1 = Base(7)
        self.assertEqual(b1.id, 7)

    def test_unique_Id(self):
        b1 = Base(8)
        b2 = Base(12)
        b3 = Base(21)
        self.assertEqual(b1.id + b2.id, b3.id - 1)

    def test_private_nb_instance(self):
        with self.assertRaises(AttributeError):
            print(Base(6).__nb_objects)

    def test_str_id(self):
        b1 = Base("Hello World")
        self.assertEqual("Hello World", b1.id)

    def test_empty_str_id(self):
        b1 = Base(12)
        b1 = Base("")
        self.assertEqual(30, b1.id)

    def test_float_id(self):
        b1 = Base(24)
        b2 = Base(2.54)
        self.assertEqual(b2.id, 2.54)

    def test_dict_id(self):
        b1 = Base({'a': 1, 'b': 2})
        self.assertEqual(b1.id, {'a': 1, 'b': 2})

    def test_empty_dict_id(self):
        b1 = Base()
        b2 = Base({})
        self.assertEqual(26, b2.id)

    def test_list_id(self):
        b1 = Base([1, 2, "3"])
        self.assertEqual(b1.id, [1, 2, "3"])

    def test_empty_list_id(self):
        b1 = Base()
        b2 = Base([])
        self.assertEqual(28, b2.id)

    def test_complex_id(self):
        self.assertEqual(Base(complex(5)).id, complex(5))

    def test_one_complex_id(self):
        self.assertEqual(Base(complex(1)).id, complex(1))

    def test_bool_id(self):
        b1 = Base(True)
        b2 = Base()
        b3 = Base(False)
        self.assertEqual(b3.id - b1.id, b2.id)

    def test_bool_true_id(self):
        self.assertEqual(Base(True).id, True)

    def test_bool_false_id(self):
        self.assertEqual(Base(False).id, 22)

    def test_set_id(self):
        self.assertEqual(Base({'a', 'b', 4}).id, {'a', 'b', 4})

    def test_empty_set(self):
        b1 = Base(6.4)
        b2 = Base(set())
        self.assertEqual(b2.id, 29)

    def test_tuple_id(self):
        self.assertEqual(Base(('a', 'b', 4)).id, ('a', 'b', 4))

    def test_empty_tuple(self):
        b1 = Base(6.4)
        b2 = Base(())
        self.assertEqual(b2.id, 31)

    def test_frozenset_id(self):  # immutable set
        b1 = Base(frozenset({34, 66, 255}))
        self.assertEqual(b1.id, frozenset({34, 66, 255}))

    def test_bytesarray_id(self):  # mutable sequence of bytes
        b1 = Base(bytearray(b'aceg'))  # == bytearray([97, 99, 101, 103])
        self.assertEqual(b1.id, bytearray(b'aceg'))

    def test_memoryview_id(self):
        self.assertEqual(Base(memoryview(b'abdul')).id, memoryview(b'abdul'))

    def test_inf_Id(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_nan_Id(self):
        # self.assertEqual(Base(float('nan')).id, float('nan')) (Does not work)
        self.assertTrue(math.isnan(Base(float('nan')).id))

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base(3, 4, 5)


class TestBase_to_json_string(unittest.TestCase):
    """Test the Base Model 'to_json_string' method"""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(4, 5)
        self.assertEqual(type(Base.to_json_string((r.to_dictionary()))), str)

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(7, 8)
        self.assertTrue(len(Base.to_json_string(r.to_dictionary())), 51)

    def test_to_json_string_rectangle_two_dict(self):
        r1 = Rectangle(7, 8).to_dictionary()
        r2 = Rectangle(1, 12).to_dictionary()
        length = len(Base.to_json_string([r1, r2]))
        self.assertTrue(length, len(r1) + len(r2) + 4)  # 4 is a result of '[, ]'

    def test_to_json_string_square_type(self):
        s = Square(4)
        self.assertEqual(type(Base.to_json_string((s.to_dictionary()))), str)

    def test_to_json_string_square_one_dict(self):
        s = Square(17)
        self.assertTrue(len(Base.to_json_string(s.to_dictionary())), 39)

    def test_to_json_string_square_two_dict(self):
        s1 = Square(711).to_dictionary()  # len of 38
        s2 = Square(14).to_dictionary()  # len of 39
        length = len(Base.to_json_string([s1, s2]))
        self.assertTrue(length, (len(s1) + len(s2) + 79))  # 4 is a result of '[, ]'

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_str_arg(self):
        self.assertEqual(Base.to_json_string("Hello"), '"Hello"')

    def test_to_json_string_empty_str_arg(self):
        self.assertEqual(Base.to_json_string(""), "[]")

    def test_to_json_string_tuple_arg(self):
        self.assertEqual(Base.to_json_string([1, "a"]), '[1, "a"]')

    def test_to_json_string_empty_tuple_arg(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_set_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string({"a"})

    def test_to_json_string_empty_set_arg(self):
        self.assertEqual(Base.to_json_string(set()), "[]")

    def test_to_json_string_dict_arg(self):
        self.assertEqual(Base.to_json_string
                         ({"name": "Rashisky"}), '{"name": "Rashisky"}')

    def test_to_json_string_empty_dict_arg(self):
        self.assertEqual(Base.to_json_string({}), "[]")

    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([1, "a"], {"name": "paper"})


class TestBase_save_to_file(unittest.TestCase):
    """Test the Base Model 'save_to_file' method"""

    @classmethod
    def tearDownClass(cls) -> None:
        """Delete any Created Files"""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_rectangle(self):
        r = Rectangle(7, 14, 52, 3, 77)
        Rectangle.save_to_file([r])
        exp_len = len(Rectangle.to_json_string([r.to_dictionary()]))
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == exp_len)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(83, 89, 0, 2, 87)
        r2 = Rectangle(87, 22, 93, 9)
        Rectangle.save_to_file([r1, r2])
        exp_len = len(Rectangle.to_json_string([r1.to_dictionary(),
                                                r2.to_dictionary()]))
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == exp_len)

    def test_save_to_file_square(self):
        s = Square(7, 14, 52, 3)
        Square.save_to_file([s])
        exp_len = len(Square.to_json_string([s.to_dictionary()]))
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == exp_len)

    def test_save_to_file_two_squares(self):
        s1 = Square(83, 89, 0, 87)
        s2 = Square(87, 22, 93, 9)
        Square.save_to_file([s1, s2])
        exp_len = len(Square.to_json_string([s1.to_dictionary(),
                                             s2.to_dictionary()]))
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == exp_len)

    def test_save_to_file_Rectangle_none_arg(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_Square_none_arg(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_Rectangle_empty_arg(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_Square_none_arg(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file(None, [])

    def test_save_to_file_not_an_instance(self):
        with self.assertRaises(AttributeError):
            Base.save_to_file(["a"])  # Where a is NOT an instance

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)


class TestBase_from_json_string(unittest.TestCase):
    """Test the Base Model 'from_json_string' method"""
    @classmethod
    def setUpClass(self) -> None:
        r1 = Rectangle(7, 9, 0, 3, 14)
        r2 = Rectangle(6, 83)
        Rectangle.save_to_file([r1, r2])

        s1 = Square(9)
        s2 = Square(14, 0, 4)
        s3 = Square(3, 2, 10, 7)
        Square.save_to_file([s1, s2, s3])

    @classmethod
    def tearDownClass(cls) -> None:
        """Delete any Created Files"""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_from_json_string_return_rectangle_type(self):
        with open("Rectangle.json", "r") as file:
            self.assertEqual(type(Base.from_json_string(file.read())), list)

    def test_from_json_string_return_square_type(self):
        with open("Square.json", "r") as file:
            self.assertEqual(type(Base.from_json_string(file.read())), list)

    def test_from_json_string_two_rectangle_args(self):
        list_input = [
            {"width": 39, "height": 21, "x": 3, "y": 4, "id": 12},
            {"width": 78, "height": 18, "x": 4, "y": 0, "id": 23}
        ]
        json_list_output = Rectangle.to_json_string(list_input)
        py_list_output = Rectangle.from_json_string(json_list_output)
        self.assertEqual(list_input, py_list_output)

    def test_from_json_string_two_square_args(self):
        list_input = [
            {"size": 21, "x": 3, "y": 4, "id": 12},
            {"size": 18, "x": 4, "y": 0, "id": 23}
        ]
        json_list_output = Rectangle.to_json_string(list_input)
        py_list_output = Rectangle.from_json_string(json_list_output)
        self.assertEqual(list_input, py_list_output)

    def test_from_json_string_one_rectangle(self):
        list_input = [
            {"width": 30, "height": 45, "x": 2, "y": 6}
        ]
        json_list_output = Rectangle.to_json_string(list_input)
        py_list_output = Rectangle.from_json_string(json_list_output)
        self.assertEqual(list_input, py_list_output)

    def test_from_json_string_one_square(self):
        list_input = [
            {"size": 30, "x": 3, "y": 7}
        ]
        json_list_output = Square.to_json_string(list_input)
        py_list_output = Square.from_json_string(json_list_output)
        self.assertEqual(list_input, py_list_output)

    def test_from_json_string_int_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(7)

    def test_from_json_string_float_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(7.5)

    def test_from_json_string_dict_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string({"model": "Base"})

    def test_from_json_string_list_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(["a", "b"])

    def test_from_json_string_single_str_arg(self):
        self.assertEqual(Base.from_json_string('["a", "b", 1]'), ['a', 'b', 1])

    def test_from_json_string_single_str_arg2(self):
        self.assertEqual(Base.from_json_string(
            '{"model": "Base", "version": 2.0}'),
                         {'model': 'Base', 'version': 2.0}
                )

    def test_from_json_string_double_str_arg(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string("['a', 'b', 1]")

    def test_from_json_string_double_str_arg2(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string("{'model': 'Base', 'version': 2.0}")

    def test_from_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_from_json_string_more_than_one_arg(self):
        with open("Rectangle.json", "r") as f1:
            with open("Square.json", "r") as f2:
                with self.assertRaises(TypeError):
                    Base.from_json_string(f1, f2)

    def test_from_json_string_empty_arg(self):
        self.assertEqual(Base.from_json_string('[]'), [])


class TestBase_create(unittest.TestCase):
    """Test the Base Model 'create' method"""

    def test_create_rectangle_no_arg(self):
        self.assertEqual(str(Rectangle.create()), "[Rectangle] (5) 0/0 - 8/7")

    def test_create_square_no_arg(self):
        self.assertEqual(str(Square.create()), "[Square] (15) 0/0 - 12")

    def test_create_rectangle_none_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.create(None)

    def test_create_square_none_arg(self):
        with self.assertRaises(TypeError):
            Square.create(None)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5)
        r2 = {
            "width": 23, "height": 15, "x": 3, "y": 4
        }
        self.assertEqual(Rectangle.create(**r2).id, 2)

    def test_create_square(self):
        s1 = Square(5)
        s2 = Square(7)
        s3 = Square.create()
        s4 = Square(51).to_dictionary()
        self.assertEqual(Square.create(**s4).id, 9)

    def test_create_rectangle_is(self):
        r1 = Rectangle(4, 5, 2, 1, 7).to_dictionary()
        r2 = Rectangle.create(**r1)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equal(self):
        r1 = Rectangle(4, 15, 12, 2, 35).to_dictionary()
        r2 = Rectangle.create(**r1)
        self.assertNotEqual(r1, r2)

    def test_create_square_is(self):
        r1 = Square(98).to_dictionary()
        r2 = Square.create(**r1)
        self.assertIsNot(r1, r2)

    def test_create_square_equal(self):
        r1 = Square(42, 5).to_dictionary()
        r2 = Square.create(**r1)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle_is(self):
        r1 = Rectangle(4, 5, 2, 1, 7).to_dictionary()
        r2 = Rectangle.create(**r1)
        self.assertIsNot(str(r1), str(r2))

    def test_create_rectangle_equal(self):
        r1 = Rectangle(4, 15, 12, 2, 35)
        r2 = Rectangle.create(**(r1.to_dictionary()))
        self.assertEqual(r1.__str__(), str(r2))

    def test_create_square_is(self):
        s1 = Square(98).to_dictionary()
        s2 = Square.create(**s1)
        self.assertIsNot(str(s1), str(s2))

    def test_create_square_equal(self):
        s1 = Square(42, 5)
        s2 = Square.create(**(s1.to_dictionary()))
        self.assertEqual(s1.__str__(), str(s2))


class TestBase_load_from_file(unittest.TestCase):
    """Test Base Model 'load_from_file' method"""

    def setUp(self) -> None:
        r1 = Rectangle(8, 3, 9, 2, 5)
        r2 = Rectangle(92, 2, 4)
        Rectangle.save_to_file([r1, r2])

        s1 = Square(4)
        s2 = Square(83, 23)
        s3 = Square(23, 13, 8, 3)
        Square.save_to_file([s1, s2, s3])

    def tearDown(cls) -> None:
        """Delete any Created Files"""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_rectangle_type(self):
        self.assertEqual(type(Rectangle.load_from_file()), list)

    def test_load_from_file_rectangle_types(self):
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_rectangle_without_str_first_obj(self):
        r = Rectangle(8, 3, 9, 2, 5)
        self.assertNotEqual(Rectangle.load_from_file()[0], r.__str__())

    def test_load_from_file_rectangle_with_str_first_obj(self):
        r = Rectangle(8, 3, 9, 2, 5)
        self.assertEqual(str(r.__str__()), str(Rectangle.load_from_file()[0]))

    def test_load_from_file_rectangle_without_str_second_obj(self):
        r = Rectangle(92, 2, 4)
        self.assertNotEqual(Rectangle.load_from_file()[1], r.__str__())

    def test_load_from_file_rectangle_with_str_second_obj(self):
        r = Rectangle(92, 2, 4, 0, 67)
        self.assertEqual(str(r.__str__()), str(Rectangle.load_from_file()[1]))

    def test_load_from_file_rectangle_memory_location(self):
        r1 = Rectangle(8, 3, 9, 2, 5)
        r2 = Rectangle(92, 2, 4)
        Rectangle.save_to_file([r1, r2])
        memory_loc = [repr(r1), repr(r2)]  # gives list of their memory loc
        self.assertIsNot(memory_loc, Rectangle.load_from_file())

    def test_load_from_file_rectangle_empty_file(self):
        with open("Rectangle.json", "w") as file:
            file.write('[]')
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle_no_file(self):
        try:
            os.remove("Rectangle.json")
            self.assertEqual(Rectangle.load_from_file(), [])
        except IOError:
            pass

    def test_load_from_file_rectangle_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])

    def test_load_from_file_square_type(self):
        self.assertEqual(type(Square.load_from_file()), list)

    def test_load_from_file_square_types(self):
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_square_without_str_first_obj(self):
        s = Square(4)
        self.assertNotEqual(Square.load_from_file()[0], s.__str__())

    def test_load_from_file_square_with_str_first_obj(self):
        load = Square.load_from_file()[0].to_dictionary()
        s = Square.create(**load)
        self.assertEqual(str(s), str(Square.load_from_file()[0]))

    def test_load_from_file_square_without_str_third_obj(self):
        s = Square(23, 13, 8, 3)
        self.assertNotEqual(Square.load_from_file()[2], s.__str__())

    def test_load_from_file_square_with_str_second_obj(self):
        load = Square.load_from_file()[1].to_dictionary()
        s = Square.create(**load)
        self.assertEqual(str(s), str(Square.load_from_file()[1]))

    def test_load_from_file_square_memory_location(self):
        s1 = Square(4)
        s2 = Square(83, 23)
        s3 = Square(23, 13, 8, 3)
        Square.save_to_file([s1, s2, s3])
        memory_loc = [repr(s1), repr(s2), repr(s3)]
        self.assertIsNot(memory_loc, Square.load_from_file())

    def test_load_from_file_square_no_file(self):
        try:
            os.remove("Square.json")
            self.assertEqual(Square.load_from_file(), [])
        except IOError:
            pass

    def test_load_from_file_square_empty_file(self):
        with open("Square.json", "w") as file:
            file.write('[]')
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_square_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])


if __name__ == "__main__":
    unittest.main()
