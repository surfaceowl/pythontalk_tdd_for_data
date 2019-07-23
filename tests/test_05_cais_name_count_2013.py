"""
tests focused on ability to pull all the names from a cais excel file

expected result stats manually gathered for  one file:  cais_name_counts_manual_2018-2019.xlsx

expected results have the following headers:
- filename:  cais_name_counts_manual_2018-2019.xlsx
- accreditation_status:  accredited or provisional
- sheetname:  e.g. "Table 12"  --- note Title Casing
- count_schools_manual:  (int) number of school names found on that tab
- count_schools_double_addresses_subtotal: # of schools on tab with more than one address listed
- count_schools_one_line_name_address: # of schools with name and address combined on one line

"""
import logging

import pytest

from src.excel_read_cell_info import find_cais_name
from src.excel_read_file_functions import get_workbook

logging.basicConfig(level=logging.WARN)

datapath_tests = "../data/test_cais/"


@pytest.mark.filterwarnings("ignore: :DeprecationWarning")
def common_search(test_filename, results_filename, table_num):
    """
    common function to test ability to find the correct number of school names
    uses static file to hold expected results in lookup table
    :return: test_num_found, results_num_expected; number of names found & number of expected names
    """
    test_workbook = get_workbook(datapath_tests + test_filename)
    test_table = f"Table {table_num}"
    test_max_rows = test_workbook[test_table].max_row

    results_workbook = get_workbook(datapath_tests + results_filename)
    results_ws = results_workbook["school_name_counts_by_sheet"]

    # find expected results:
    test_num_expected = 0
    for row in range(1, results_ws.max_row + 1):
        if results_ws.cell(row=row, column=3).value == test_table:
            test_num_expected = results_ws.cell(row=row, column=4).value
            break
        else:
            continue

    # count_name_in_table names & compare with expected value in result_total_table
    result_local = {2013: {}}
    list_discovered_schools = []
    test_num_found = 0

    for row in range(1, test_max_rows + 1):
        temp_result = find_cais_name(
            test_workbook[test_table].cell(row=row, column=1),
            result_local)

        if temp_result is not None:
            list_discovered_schools.append(temp_result)
            test_num_found += 1
        continue

    if test_num_found != test_num_expected:
        logging.warning(f"table: {test_table}")
        logging.warning(f"found: {test_num_found} vs expected: {test_num_expected}")
        for item in list_discovered_schools:
            logging.warning(f"school names discovered {item}")

    print("\n2013 school names discovered:\n")
    for item in list_discovered_schools:
        print(f"{item}")

    return test_num_found, test_num_expected


def test_find_2013_cais_name_table10():
    """
    test finding names in first member schools tab
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2013-2014-converted.xlsx"
    results_file = "cais_name_counts_manual_2013-2014.xlsx"
    table_num = 10

    found_in_table_10, expected_in_table_10 = common_search(test_file, results_file, table_num)

    assert found_in_table_10 == expected_in_table_10
