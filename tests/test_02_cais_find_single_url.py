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
