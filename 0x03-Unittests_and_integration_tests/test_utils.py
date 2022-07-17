#!/usr/bin/env python3

"""
text file to Parameterize a unit test to return accurate result
"""
from typing import Mapping, Sequence, Union
import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """class to test AccessNestedMap method 
        with unittest
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, output) -> Union[Mapping, int]:
        """method to test if accessnestedmap
            returns expected result.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), output)
      