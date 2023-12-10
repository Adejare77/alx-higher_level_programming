#!/usr/bin/python3

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):

    def test_rect_base(self):  # check if Rect is an instance of Base
        self.assertIsInstance(Rectangle(7, 1), Base)

    def test_rect_no_arg(self):  # check if rect no arg is given
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_one_arg(self):  # check if rect one arg is given
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_three_arg(self):  # check for rect three args
        Rectangle(1, 7, 7)

    def test_four_arg(self):  # check for rect four args
        Rectangle(1, 7, 7, 8)

    def test_five_arg(self):  # check for rect five args
        Rectangle(1, 7, 7, 8, 6)

    def test_more_than_five_arg(self):  # check for rect more than 5 args
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 7, 8, 41, None, 3.4, -2)

    def test_rect_none_arg(self):  # check for rect None arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, None)

    def test_rect_list_arg(self):  # check for rect list arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2], 1)

    def test_rect_str_arg(self):  # check for str arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "a")

    def test_rect_float_arg(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, 4.8)

    def test_rect_type_arg(self):  # check for rect type arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(int, int)

    def test_rect_negative_arg(self):  # check for rect -ve arg
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, -7)

    def test_rect_zerotype_arg(self):  # check for rect zero arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, 0)

    def test_rect_set_arg(self):  # check for rect set arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2})

    def test_rect_tuple_arg(self):  # check for rect tuple arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 4), 3)

    def test_rect_bool_arg(self):  # check for rect boolean arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, False)

    def test_rect_dict_arg(self):  # check for rect dictionary arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'x': 1}, 9)

    def test_rect_x_arg(self):  # check for rect dictionary x arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, 'a', 'k')

    def test_rect_y_arg(self):  # check for rect dictionary arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 7, 2.58)

    def test_rect_y_val_arg(self):  # check for rect y_val arg
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 7, 4, -4)

    def test_rect_y_arg(self):  # check for rect complex arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 7, 7, 'k')

    def test_rect_x_arg(self):  # check for rect frozenset arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 7, frozenset({7}), 'k')

    def test_rect_x_val_arg(self):  # check for rect x_val arg
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 7, -1)

    def test_rect_x_val_arg(self):  # check for rect inf arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'), -1)

    def test_2_diff_ids_arg(self):
        rect_1 = Rectangle(5, 5, 8, 2).id
        rect_2 = Rectangle(5, 5, 8, 2).id
        self.assertNotEqual(rect_1, rect_2)

    def test_2_same_ids_arg(self):
        rect_1 = Rectangle(5, 5, 8, 2, 1).id
        rect_2 = Rectangle(5, 5, 8, 2, 1).id
        self.assertEqual(rect_1, rect_2)

    def test_2_same_x_arg(self):
        rect_1 = Rectangle(5, 5).x
        rect_2 = Rectangle(5, 5).x
        self.assertEqual(rect_1, rect_2)

    def test_2_diff_x_arg(self):
        rect_1 = Rectangle(5, 5, 8, 2).x
        rect_2 = Rectangle(5, 5, 10).x
        self.assertNotEqual(rect_1, rect_2)

    def test_2_same_y_arg(self):
        rect_1 = Rectangle(5, 5).y
        rect_2 = Rectangle(5, 5).y
        self.assertEqual(rect_1, rect_2)

    def test_2_diff_y_args(self):
        rect_1 = Rectangle(5, 5, 8, 2).y
        rect_2 = Rectangle(5, 5, 8, 3).y
        self.assertNotEqual(rect_1, rect_2)


class TestRectangle_area(unittest.TestCase):

    def test_small_area_args(self):  # area of a circle
        self.assertEqual(Rectangle(3, 4, 7).area(), 12)

    def test_large_area_args(self):  # check for area2 set arge
        self.assertEqual(Rectangle(4587512466, 74125478963, 7).area(),
                         340051558790983252758)

    def test_area_no_arg(self):  # check if area no arg is given
        with self.assertRaises(TypeError):
            Rectangle().area()

    def test_area_one_arg(self):  # check if area one arg is given
        with self.assertRaises(TypeError):
            Rectangle(1).area()

    def test_area_zero_arg(self):  # check for area set arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 6).area()

    def test_area_set_arg(self):  # check for area set arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2}).area()

    def test_area_tuple_arg(self):  # check for area tuple arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 4), 3).area()

    def test_area_bool_arg(self):  # check for area boolean arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, False).area()

    def test_area_dict_arg(self):  # check for area dictionary arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'x': 1}, 9).area()

    def test_area_x_arg(self):  # check for area dictionary x arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, 'a', 'k').area()

    def test_area_y_arg(self):  # check for area dictionary arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 7, 2.58).area()

    def test_area_y_val_arg(self):  # check for area y_val arg
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 7, 4, -4).area()

    def test_area_y_arg(self):  # check for area complex arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 7, 7, 'k').area()

    def test_area_x_arg(self):  # check for area frozenset arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 7, frozenset({7}), 'k').area()

    def test_area_x_val_arg(self):  # check for area x_val arg
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 7, -1).area()

    def test_area_negative_arg(self):  # check for area -ve arg
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, -7).area()


class TestRectangle_width(unittest.TestCase):

    def test_width_args(self):  # width of a circle
        self.assertEqual(Rectangle(3, 4, 7).width, 2)

    def test_width_args(self):  # check for width2 set arge
        self.assertNotEqual(Rectangle(3, 11, 7).width, 11)

    def test_width_no_arg(self):  # check if width no arg is given
        with self.assertRaises(TypeError):
            Rectangle().width

    def test_width_one_arg(self):  # check if width one arg is given
        with self.assertRaises(TypeError):
            Rectangle(1).width

    def test_width_zero_arg(self):  # check for width set arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 6).width

    def test_width_set_arg(self):  # check for width set arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2}).width

    def test_width_tuple_arg(self):  # check for width tuple arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 4), 3).width

    def test_width_bool_arg(self):  # check for width boolean arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, False).width

    def test_width_dict_arg(self):  # check for width dictionary arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'x': 1}, 9).width

    def test_width_x_arg(self):  # check for width dictionary x arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, 'a', 'k').width

    def test_width_y_arg(self):  # check for width dictionary arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 7, 2.58).width

    def test_width_y_val_arg(self):  # check for width y_val arg
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 7, 4, -4).width

    def test_width_y_arg(self):  # check for width complex arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 7, 7, 'k').width

    def test_width_x_arg(self):  # check for width frozenset arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 7, frozenset({7}), 'k').width

    def test_width_x_val_arg(self):  # check for width x_val arg
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 7, -1).width

    def test_width_negative_arg(self):  # check for width -ve arg
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, -7).width


class TestRectangle_height(unittest.TestCase):

    def test_height_args(self):  # width of a circle
        self.assertNotEqual(Rectangle(3, 4, 7).height, 3)

    def test_height_args(self):  # check for width2 set arge
        self.assertEqual(Rectangle(3, 11, 7).height, 11)

    def test_height_no_arg(self):  # check if width no arg is given
        with self.assertRaises(TypeError):
            Rectangle().height

    def test_height_one_arg(self):  # check if width one arg is given
        with self.assertRaises(TypeError):
            Rectangle(1).height

    def test_height_zero_arg(self):  # check for width set arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 6).height

    def test_height_set_arg(self):  # check for width set arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2}).height

    def test_height_tuple_arg(self):  # check for width tuple arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (4, 4)).height

    def test_height_bool_arg(self):  # check for width boolean arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, False).height

    def test_height_dict_arg(self):  # check for width dictionary arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'x': 1}, 9).height

    def test_height_x_arg(self):  # check for width dictionary x arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, {'name': "Holberton"}, 'k').height

    def test_height_y_arg(self):  # check for width dictionary arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 7, {'size': 2.58}).height

    def test_height_y_val_arg(self):  # check for width y_val arg
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 7, 4, -4).height

    def test_height_y_arg(self):  # check for width complex arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 87, complex(1), 7).height

    def test_height_x_arg(self):  # check for width frozenset arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 7, frozenset({7}), 'k').height

    def test_height_x_val_arg(self):  # check for width x_val arg
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 7, -1).height

    def test_height_negative_arg(self):  # check for width -ve arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -7).height

    def test_height_y_arg(self):  # check for width arg length
        with self.assertRaises(TypeError):
            Rectangle(1, 87, complex(1), 7, 7, 'k').height


class TestRectangle_x(unittest.TestCase):

    def test_x_args(self):  # X of a circle
        self.assertNotEqual(Rectangle(3, 4).x, 0)

    def test_x_args(self):  # check for X2 set arge
        self.assertEqual(Rectangle(3, 11, 7).x, 7)

    def test_x_no_arg(self):  # check if X no arg is given
        with self.assertRaises(TypeError):
            Rectangle().x

    def test_x_one_arg(self):  # check if X one arg is given
        with self.assertRaises(TypeError):
            Rectangle(1).x

    def test_x_zero_arg(self):  # check for X set arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 6).x

    def test_x_set_arg(self):  # check for X set arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2}).x

    def test_x_tuple_arg(self):  # check for X tuple arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (4, 4)).x

    def test_x_bool_arg(self):  # check for X boolean arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, False).x

    def test_x_dict_arg(self):  # check for X dictionary arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'x': 1}, 9).x

    def test_x_x_arg(self):  # check for X dictionary x arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, {'name': "Holberton"}, 'k').x

    def test_x_y_arg(self):  # check for X dictionary arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 7, {'size': 2.58}).x

    def test_x_y_val_arg(self):  # check for X y_val arg
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 7, 4, -4).x

    def test_x_y_arg(self):  # check for X complex arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 87, complex(1), 7).x

    def test_x_x_arg(self):  # check for X frozenset arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 7, frozenset({7}), 'k').x

    def test_x_x_val_arg(self):  # check for X x_val arg
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 7, -1).x

    def test_x_negative_arg(self):  # check for X -ve arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -7).x

    def test_x_y_arg(self):  # check for X arg length
        with self.assertRaises(TypeError):
            Rectangle(1, 87, complex(1), 7, 7, 'k').x


class TestRectangle_y(unittest.TestCase):

    def test_y_args(self):  # Y of a circle
        self.assertNotEqual(Rectangle(3, 4).y, 2)

    def test_y_args(self):  # check for Y2 set arge
        self.assertEqual(Rectangle(3, 11, 7).y, 0)

    def test_y_no_arg(self):  # check if Y no arg is given
        with self.assertRaises(TypeError):
            Rectangle().y

    def test_y_one_arg(self):  # check if Y one arg is given
        with self.assertRaises(TypeError):
            Rectangle(1).y

    def test_y_zero_arg(self):  # check for Y set arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 6, -2.5).y

    def test_y_set_arg(self):  # check for Y set arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2}, 4).y

    def test_y_tuple_arg(self):  # check for Y tuple arg
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (4, 4), 0, 5).y

    def test_y_bool_arg(self):  # check for Y boolean arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, False, False, True, None).y

    def test_y_dict_arg(self):  # check for Y dictionary arg
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'y': 1}, 9, "value", set((4, 6))).y

    def test_y_x_arg(self):  # check for Y dictionary x arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 3, 89, {'name': "Holberton"}).y

    def test_y_y_arg(self):  # check for Y dictionary arg
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 7, {'size': 2.58}).y

    def test_y_y_val_arg(self):  # check for Y y_val arg
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 7, 4, -4).y

    def test_y_y_arg(self):  # check for Y complex arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 87, complex(1), 7).x

    def test_y_x_arg(self):  # check for Y frozenset arg
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 7, frozenset({7}), 87).y

    def test_y_x_val_arg(self):  # check for Y x_val arg
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 7, -1, {6}).y

    def test_y_negative_arg(self):  # check for Y -ve arg
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -7, list((1, 3))).y

    def test_y_y_arg(self):  # check for Y arg length
        with self.assertRaises(TypeError):
            Rectangle(1, 87, complex(1), 7, 7, 'k').x


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
