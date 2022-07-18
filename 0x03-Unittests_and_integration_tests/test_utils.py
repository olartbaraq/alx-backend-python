#!/usr/bin/env python3

"""
text file to Parameterize a unit test to return accurate result
"""
from typing import Mapping, Sequence, Union
import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """class to test AccessNestedMap method
        with unittest
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, output) -> Union[Mapping, int]:
        """method to test if accessnestedmap
            returns expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """to test that a keyError is raised"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests Class for utils.get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> Mapping:
        """Test for correct results"""
        class payLoad():
            """creates a mock response having a json method"""
            def __init__(self, obj):
                """Instantiation method"""
                self.obj = obj

            def json(self):
                """state the json method and return"""
                return self.obj

        with mock.patch('requests.get', return_value=payLoad(test_payload))\
                as mock_method:
            self.assertEqual(get_json(test_url), test_payload)
            mock_method.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
