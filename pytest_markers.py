"""
Module contains custom pytest markers decorators
"""
import pytest
from _pytest.mark import MarkDecorator


def link_to_test(url: str) -> MarkDecorator:
    """
    Specifies link to test in test management tool
    :param url:
    :return:
    """
    return pytest.mark.link_to_test(url)
