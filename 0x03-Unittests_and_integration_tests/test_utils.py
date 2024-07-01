#!/usr/bin/env python3
"""
unitest on utilities function
"""
import unittest
from typing import Dict, Mapping, Tuple, Union

from parameterized import parameterized  # type: ignore

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    test the access nested map function
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 1}}, ("a",), {"b": 1}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Tuple, expected: Union[Dict, int]
    ):
        """the test access nested map unit test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Tuple
    ):
        """a test method too test for exception raised"""
        with self.assertRaises(KeyError):
            map_values = access_nested_map(nested_map, path)
