#!/usr/bin/env python3
"""
unitest on utilities function
"""
import unittest
from typing import Mapping, Tuple, Union

from parameterized import parameterized  # type: ignore

from utils import access_nested_map


class TestAccessNestedMad(unittest.TestCase):
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
        self, nested_map: Mapping, path: Tuple, expected: Union[Mapping, int]
    ):
        """the test access nested map unit test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
