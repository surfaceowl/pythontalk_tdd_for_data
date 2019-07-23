"""
test functions to find url in cell content from an excel worksheet

functions below have "do_this_later_" prefix to prevent tests from running during early part of talk
remove prefix as we walk through examples, and re-run tests
"""
from src.excel_find_url import find_url


def test_find_https_url():
    """
    unit test multiple strings for urls in bulk - rather than separate test functions for each
    one way to rapidly iterate on your code, nicely encapsulates similar cases

    requires editing REGEX in excel_read_cell_info.find_url to make this test pass
    """
    result = {}

    # inputs we expect to pass
    input01 = "Coed Boarding/Day School Grades 6-12; Enrollment 350 http://www.prioryca.org"
    input02 = "https://windwardschool.org"

    assert find_url(input01, result) == "http://www.prioryca.org"
    assert find_url(input02, result) == "https://windwardschool.org"
