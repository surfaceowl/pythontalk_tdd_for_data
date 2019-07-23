"""
test functions to find url in cell content from an excel worksheet

functions below have "do_this_later_" prefix to prevent tests from running during early part of talk
remove prefix as we walk through examples, and re-run tests
"""
from src.excel_find_url import find_url


def test_find_multi_url():
    """
    unit test multiple strings for urls in bulk - rather than separate test functions for each
    one way to rapidly iterate on your code, nicely encapsulates similar cases

    requires editing REGEX in excel_read_cell_info.find_url to make this test pass
    """
    result = {}

    # inputs we expect to pass
    input01 = "Coed Boarding/Day School Grades 6-12; Enrollment 350 http://www.prioryca.org"
    input02 = "https://windwardschool.org"
    input03 = "  Enrollment 225 york.org"
    input04 = "Surface Owl Inc., https://surfaceowl.com"

    # inputs we expect to return `None`
    input05 = "Woodside Priory School"
    input06 = "8221  Fax (650)"
    input07 = "Head of School Coeducational Boarding/Day School Grades 6-12; Enrollment 350"
    input08 = "surfaceowl"
    input09 = "www.york.org"

    assert find_url(input01, result) == "http://www.prioryca.org"
    assert find_url(input02, result) == "https://windwardschool.org"
    assert find_url(input03, result) == "york.org"
    assert find_url(input04, result) == "https://surfaceowl.com"
    assert find_url(input05, result) is None
    assert find_url(input06, result) is None
    assert find_url(input07, result) is None
    assert find_url(input08, result) is None
    assert find_url(input09, result) == "www.york.org"
