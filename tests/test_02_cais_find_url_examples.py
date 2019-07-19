"""
test functions to find url in cell content from an excel worksheet

functions below have "do_this_later_" prefix to prevent tests from running during early part of talk
remove prefix as we walk through examples, and re-run tests
"""
from src.excel_read_file_functions import get_workbook
from src.excel_read_cell_info import find_url
from src.configuration_info_cais import datapath_tests


def test_find_single_url():
    """
    unit test to find url in a single text string
    :return: None
    """
    # the find_url function we are testing takes cell content as a string, and current results dict
    # pass an empty results dict, so no existing value is found
    result = {}

    # inputs we expect to pass
    input01 = "Coeducational Boarding/Day School Grades 6-12; Enrollment 350 www.prioryca.org"

    # declare result we expect to find here
    assert find_url(input01, result) == "www.prioryca.org"


def do_this_later_test_find_multi_url():
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

    assert find_url(input01, result) == "http://www.prioryca.org"
    assert find_url(input02, result) == "https://windwardschool.org"
    assert find_url(input03, result) == "york.org"
    assert find_url(input04, result) == "https://surfaceowl.com"
    assert find_url(input05, result) is None
    assert find_url(input06, result) is None
    assert find_url(input07, result) is None
    assert find_url(input08, result) is None


def do_this_later_test_find_url_from_excelfile():
    """
    integration test to find url from excel file
    :return: None
    """

    filename = datapath_tests + "School_Directory_2013-2014-converted.xlsx"
    workbook = get_workbook(filename)
    tab_name = "Table 15"
    row = 23
    result = {}  # function expects input dict with prior results; equals empty dict now

    # inputs we expect to pass
    test_input = workbook[tab_name].cell(row=row, column=1).value

    assert find_url(test_input, result) == "https://www.hamlin.org"
