"""
basic usage example of pytest
"""
import pytest
from src.pytest_simple_example import add_two_ints


@pytest.mark.filterwarnings("ignore: :DeprecationWarning")
def test_simple_example():
    assert add_two_ints(1, 1) == 2
