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


@pytest.mark.filterwarnings("ignore: :DeprecationWarning")
def common_search(test_filename, results_filename, table_num):
    """
    common function to test ability to find the correct number of school names
    uses static file to hold expected results in lookup table
    :return: test_num_found, results_num_expected; number of names found & number of expected names
    """
    datapath_tests = "../data/test_cais/"
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
    result_local = {2018: {}}
    list_discovered_schools = []
    test_num_found = 0

    for row in range(1, test_max_rows + 1):
        temp_result = find_cais_name(
            test_workbook[test_table].cell(row=row, column=1),
            result_local)

        if temp_result is not None:
            list_discovered_schools.append(temp_result)
            test_num_found += 1
        else:
            pass
        continue

    if test_num_found != test_num_expected:
        logging.warning(f"table: {test_table}")
        logging.warning(f"found: {test_num_found} vs expected: {test_num_expected}")
        for item in list_discovered_schools:
            logging.warning(f"school names discovered {item}")

    # print("\n 2018 school names discovered")
    # for item in list_discovered_schools:
    #    print(f"{item}")

    return test_num_found, test_num_expected


def test_find_2018_cais_name_table12():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 12

    found_in_table_12, expected_in_table_12 = common_search(test_file, results_file, table_num)

    assert found_in_table_12 == expected_in_table_12


def test_find_2018_cais_name_table13():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 13

    found_in_table_13, expected_in_table_13 = common_search(test_file, results_file, table_num)

    assert found_in_table_13 == expected_in_table_13


def test_find_2018_cais_name_table14():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 14

    found_in_table_14, expected_in_table_14 = common_search(test_file, results_file, table_num)

    assert found_in_table_14 == expected_in_table_14


def test_find_2018_cais_name_table15():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 15

    found_in_table_15, expected_in_table_15 = common_search(test_file, results_file, table_num)

    assert found_in_table_15 == expected_in_table_15


def test_find_2018_cais_name_table16():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 16

    found_in_table_16, expected_in_table_16 = common_search(test_file, results_file, table_num)

    assert found_in_table_16 == expected_in_table_16


def test_find_2018_cais_name_table17():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 17

    found_in_table_17, expected_in_table_17 = common_search(test_file, results_file, table_num)

    assert found_in_table_17 == expected_in_table_17


def test_find_2018_cais_name_table18():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 18

    found_in_table_18, expected_in_table_18 = common_search(test_file, results_file, table_num)

    assert found_in_table_18 == expected_in_table_18


def test_find_2018_cais_name_table19():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 19

    found_in_table_19, expected_in_table_19 = common_search(test_file, results_file, table_num)

    assert found_in_table_19 == expected_in_table_19


def test_find_2018_cais_name_table20():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 20

    found_in_table_20, expected_in_table_20 = common_search(test_file, results_file, table_num)

    assert found_in_table_20 == expected_in_table_20


def test_find_2018_cais_name_table21():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 21

    found_in_table_21, expected_in_table_21 = common_search(test_file, results_file, table_num)

    assert found_in_table_21 == expected_in_table_21


def test_find_2018_cais_name_table22():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 22

    found_in_table_22, expected_in_table_22 = common_search(test_file, results_file, table_num)

    assert found_in_table_22 == expected_in_table_22


def test_find_2018_cais_name_table23():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 23

    found_in_table_23, expected_in_table_23 = common_search(test_file, results_file, table_num)

    assert found_in_table_23 == expected_in_table_23


def test_find_2018_cais_name_table24():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 24

    found_in_table_24, expected_in_table_24 = common_search(test_file, results_file, table_num)

    assert found_in_table_24 == expected_in_table_24


def test_find_2018_cais_name_table25():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 25

    found_in_table_25, expected_in_table_25 = common_search(test_file, results_file, table_num)

    assert found_in_table_25 == expected_in_table_25


def test_find_2018_cais_name_table26():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 26

    found_in_table_26, expected_in_table_26 = common_search(test_file, results_file, table_num)

    assert found_in_table_26 == expected_in_table_26


def test_find_2018_cais_name_table27():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 27

    found_in_table_27, expected_in_table_27 = common_search(test_file, results_file, table_num)

    assert found_in_table_27 == expected_in_table_27


def test_find_2018_cais_name_table28():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 28

    found_in_table_28, expected_in_table_28 = common_search(test_file, results_file, table_num)

    assert found_in_table_28 == expected_in_table_28


def test_find_2018_cais_name_table29():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 29

    found_in_table_29, expected_in_table_29 = common_search(test_file, results_file, table_num)

    assert found_in_table_29 == expected_in_table_29


def test_find_2018_cais_name_table30():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 30

    found_in_table_30, expected_in_table_30 = common_search(test_file, results_file, table_num)

    assert found_in_table_30 == expected_in_table_30


def test_find_2018_cais_name_table31():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 31

    found_in_table_31, expected_in_table_31 = common_search(test_file, results_file, table_num)

    assert found_in_table_31 == expected_in_table_31


def test_find_2018_cais_name_table32():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 32

    found_in_table_32, expected_in_table_32 = common_search(test_file, results_file, table_num)

    assert found_in_table_32 == expected_in_table_32


def test_find_2018_cais_name_table33():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 33

    found_in_table_33, expected_in_table_33 = common_search(test_file, results_file, table_num)

    assert found_in_table_33 == expected_in_table_33


def test_find_2018_cais_name_table34():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 34

    found_in_table_34, expected_in_table_34 = common_search(test_file, results_file, table_num)

    assert found_in_table_34 == expected_in_table_34


def test_find_2018_cais_name_table35():
    """
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 35

    found_in_table_35, expected_in_table_35 = common_search(test_file, results_file, table_num)

    assert found_in_table_35 == expected_in_table_35


def test_find_2018_cais_name_table36():
    """
    provisional tab
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 36

    found_in_table_36, expected_in_table_36 = common_search(test_file, results_file, table_num)

    assert found_in_table_36 == expected_in_table_36


def test_find_2018_cais_name_table37():
    """
    provisional tab
    test function to dynamically look up names vs. expected result from separate file
    :return: True or False
    """
    test_file = "School_Directory_2018-2019-converted.xlsx"
    results_file = "cais_name_counts_manual_2018-2019.xlsx"
    table_num = 37

    found_in_table_37, expected_in_table_37 = common_search(test_file, results_file, table_num)

    assert found_in_table_37 == expected_in_table_37
