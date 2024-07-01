#!/usr/bin/env python3
"""
unitest on utilities function
"""
import unittest

from parameterized import parameterized  # type: ignore

from utils import access_nested_map


class TestAccessNestedMad(unittest.TestCase):
    """
    test the access nested map function
    """

    @parameterized.expand(
        [
            ("test_map_1", {"a": 1}, ("a",), 1),
            ("test_map_2", {"a": {"b": 1}}, ("a",), {'b': 1}),
            ("test_map_3", {"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, name, nested_map, path, expected):
        """ the test access nested map unit test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
