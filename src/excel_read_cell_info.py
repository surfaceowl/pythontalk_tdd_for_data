# file encoding: utf-8
"""
functions analyzing cell content from excel worksheet
"""
import logging
import re

from src.configuration_info_cais import list_non_name_standalone_stopwords
from src.configuration_info_cais import list_non_name_stopwords
from src.configuration_info_cais import list_school_format_safe_list
from src.configuration_info_cais import list_school_synonyms
from src.configuration_info_cais import list_section_names

logging.basicConfig(level=logging.WARN)


# noinspection Annotator
def find_url(content, result):
    """
    finds url of school if it exists in cell
    :param content: cell content from spreadsheet
    :type content: string
    :param result: dict of details on current school
    :type result: dict
    :return: url
    :rtype: basestring
    """
    if check_if_already_found("url", result):
        return result['url']

    # different regex to use during python talk
    # https://regex101.com
    # regex0 = re.compile(r"w{3}.*", re.IGNORECASE)
    # regex1 = re.compile(r"(http|https):\/\/*", re.IGNORECASE)  # EDIT THIS LIVE

    regex2 = re.compile(
        r"((http|https)://)?[a-zA-Z0-9./?::-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9../&/\-_=#])*",
        re.IGNORECASE)

    try:
        match = re.search(regex2,
                          str(content))
    except TypeError:
        raise TypeError

    if match:
        url = str(match.group()).strip()
        return url
    else:
        return None


def check_is_section_name(content):
    """
    checks if cell content is in list of known lines to skip
    :param content:  cell content
    :type content: basestring
    :return: boolean (True;False)
    """
    if str(content).lower() in str(list_section_names).lower():
        return True
    else:
        return False


def split_name_from_address(content):
    """
    many entries have name + address combined in one cell; this function pulls out the name string
    by finding the house number as the first set of digits in the cell, and taking all text before
    :param content: cell content from spreadsheet
    :type content: object
    :return: cais_name_split
    :rtype basestring
    """
    regex_address_num = r"\s[0-9]+"  # first instance of two digits or more
    find_address_num = re.search(regex_address_num, content.value)
    current_house_number = str(find_address_num.group(0))
    find_school_name = re.search(r"(.*)" + current_house_number,
                                 content.value).group(0)
    cais_name = find_school_name.split(current_house_number, 3)[0]
    cais_name = cais_name.replace(":", "")

    return cais_name


def check_for_exception_name_in(cell_content_to_check):
    """
    if special case names appear in the cell, that's the school name
    accepts both objects and strings
    :param cell_content_to_check: object or string (depending on where called from
    :return: school
    """

    for school in list_school_format_safe_list:
        if type(cell_content_to_check) == object:
            if school in cell_content_to_check.value:
                return school
        elif type(cell_content_to_check) == str:
            if school in cell_content_to_check:
                return school


def check_for_school_synonym_in(cell_content_to_check):
    # if special case names appear in the cell, that's the school name
    # if this happens, just return the cell content as the school name - mostly correct
    found = 0
    for school_synonym in list_school_synonyms:
        x = str(school_synonym).lower()
        y = str(cell_content_to_check).lower()
        if x in y:
            found += 1
    if found:
        return cell_content_to_check
    else:
        return None


def find_school_synonym_stopword(cell_content_to_check):
    """
    finds the first stopword that is a school synonym
    :param cell_content_to_check:
    :type cell_content_to_check: basestring
    :return: stopword
    :rtype: basestring
    """
    stopword = None
    for school_synonym in list_school_synonyms:
        x = str(school_synonym).lower()
        y = str(cell_content_to_check).lower()
        if x in y:
            stopword = x
            break
        else:
            stopword = None
    return stopword


def find_cais_name(cell_obj, result_local):
    """
    # consider adding:  workbook_tab, row,, result
    finds name of school if it exists in cell
    :param result_local:
    :param cell_obj: object cell content from spreadsheet
    :type cell_obj: object
    :return: cais_name:  name of school
    :rtype: basestring
    """
    cell_content = cell_obj.value
    stopwords = list_section_names + list_non_name_stopwords  # list of lists

    if cell_content is not None:
        # if cell value is a section name, we don't want it
        if any(cell_content.lower() == name.lower() for name in list_section_names):
            return None

        # if the cell value is a stopword, we don't want it
        if any(cell_content.lower() == stopword.lower() for stopword in list_non_name_stopwords):
            return None

        # trap for cases where a common segmentation term like `preparatory school`
        # is found alone in a cell - often part of legit name, but not when by itself
        for stopword in list_non_name_standalone_stopwords:
            if cell_content.lower() == stopword.lower() and len(cell_content) == len(stopword):
                return None
            else:
                continue

        if any(word.lower() in cell_content.lower() for word in stopwords):
            if check_for_exception_name_in(cell_content):
                return cell_content  # found a known troublesome name/format
            else:
                found_stopword = True  # we found a stopword, but don't know enough to skip yet
        else:
            found_stopword = False

        # return existing name if we've already found it (from nested dict)
        if result_local.keys():
            outer_dict = list(result_local.keys())
            unique_id = outer_dict[0]
            inner_dict = result_local[unique_id]
            if 'name' in inner_dict.keys():
                existing_name = result_local[unique_id]['name']
                return existing_name

        # skip empty cells
        # noinspection PyTypeChecker
        if cell_obj.value is None:
            return None

        # skip known header rows
        elif cell_obj.value in list_section_names \
                or "provisional" in str(cell_content).lower():
            return None  # no name found

        # skip rows that contain head or enrollment info, or other stopword
        elif found_stopword:
            return None

        # handle known exceptions
        elif check_for_exception_name_in(cell_obj):
            if cell_obj.font.charset == 204 and cell_obj.value is not None:
                # charset 204 exists when name formatting different than other cell text
                cais_name = split_name_from_address(cell_obj)
                return cais_name

        # this catches most schools
        elif check_for_school_synonym_in(cell_content):
            if cell_obj.alignment.indent != 0:  # names found only on non-indented cells
                return None  # cell not indented
            else:
                # check if content contains address
                # MUST be inside check for synonym
                if check_contains_address(cell_obj):
                    cais_name = split_name_from_address(cell_obj)
                    return cais_name
                else:
                    return cell_content


def check_contains_address(content):
    """
    determines if cell content contains potential physical address
    :param content: workbook cell object
    :type content: object
    :return: True or False
    :rtype boolean
    """
    # all schools are in state of CA w/zip; allow 5-digit zip, with *optional* -zip+4
    regex_address = r"CA\s[0-9]{5}(?:-[0-9]{4})?$"
    match = re.search(regex_address, content.value)

    if match:
        return True
    else:
        return False


def find_address(workbook, sheet_name, row, content, result):
    """
    finds address of school  if it exists in cell
    :param workbook: current worksheet object
    :type: workbook_object: object
    :param sheet_name: name excel worksheet, for indexing into workbook cells
    :type sheet_name: basestring
    :param row: row number we are currently inspecting
    :type row: int
    :param content: cell content as VALUE from spreadsheet
    :type content: basestring
    :param result: dict of member info
    :type result: dict
    :return: address
    :rtype: basestring
    """

    def clean_known_address(address_string):
        """
        there are known tokens we can use to split non-address content from a string
        :param address_string: string that likely contains an address we want
        :type address_string: basestring
        :return: clean_address_string -- result without known bad substrings
        :rtype basestring
        """
        bad_tokens_leading = [": ", "Elementary School:"]
        bad_tokens_trailing = ["MAIL:"]

        clean_address = None
        cleaning_executed = False

        for token in bad_tokens_leading:
            if token in address_string:  # take second part of address_string
                cleaning_executed = True
                clean_address = address_string.split(token, 2)[1].strip()
            else:
                clean_address = address_string

        for token in bad_tokens_trailing:
            if token in clean_address:  # take first part of address_string
                cleaning_executed = True
                clean_address = clean_address.split(token, 2)[0].strip()
            else:
                clean_address = clean_address

        if cleaning_executed:
            return clean_address
        else:
            return address_string

    # address are mostly formatted like Case 2
    # cases organized in order of easiest parsing logic
    # Case 1 name in content - name in line 0; address merged in line 0
    # Case 2 name in line 0; entire address in line 1
    # Case 3 name in line 0; TWO part address; address part 1 with no CA in line 1
    # Case 4 - TODO: addresses with both physical and MAIL addresses
    # Case 5 - TODO: multi-campus addresses
    # all schools are in state of CA w/zip; allow 5-digit zip, with *optional* -zip+4

    regex_address = str(r"CA\s[0-9]{5}(?:-[0-9]{4})?$")
    try:
        match = re.search(regex_address, str(content))
        # use str() to protect against python typing text as int
    except TypeError:
        raise TypeError

    # check if we need to process a potential address
    if check_if_already_found("address", result):  # if already found, skip rest of function
        return result['address']
    elif content is None:  # protect against empty cells
        return None
    elif not match:
        return None

    name_in_content = None
    regex_name = None

    if row >= 2:
        cell_content_prev_row = workbook[sheet_name].cell(row=row - 1, column=1).value
    else:
        cell_content_prev_row = None

    if match and "MAIL" in content:  # found address we don't want; strip and seek address again
        content = str(content).split("MAIL", 2)[1].strip()
        match = re.search(regex_address, content)

    if match and "MAIL" not in content:  # found physical address we want
        # protect in cases where we haven't created the `name` key yet

        # if we've already found school name, use it to help address search
        if 'name' in result.keys():
            name = result['name']
        else:
            name = None

        # check for name string in current cell content
        if name is not None:
            regex_name = re.escape(name)  # search for existing name
            name_in_content = re.search(regex_name, content)
        else:
            # backup search for content likely to be a school name
            if any(word in content for word in list_school_synonyms):
                name_in_content = content

        if cell_content_prev_row is not None and regex_name is not None:
            name_in_previous_content = re.search(regex_name, cell_content_prev_row)
        else:
            name_in_previous_content = None

        # Case 1  - name + State/Zip code in content
        if name_in_content is not None:
            # if both name + address in content
            # split at end of name - rest of cell == correct address!
            match_address = str(content).split(name, 2)[
                1].strip()  # name is always before address
            match_address = clean_known_address(match_address)
            return match_address
        # Case 2 - # address in one line, directly below name
        elif name_in_content is None and name_in_previous_content:
            exception_strings = ["Secondary School:"]
            for string in exception_strings:
                if string in content:
                    address = str(name_in_content).split(name, 2)[1].strip()
                    address = clean_known_address(address)
                    return address
                else:
                    continue
            address = str(content).strip()
            address = clean_known_address(address)
            return address
        # Case 3 - address in two lines, below name in top line
        elif name is not None \
                and name_in_content is None \
                and name_in_previous_content is None \
                and row >= 3:  # we must be on the 3rd row to look back two rows

            content_row_up2 = workbook[sheet_name].cell(row=row - 2, column=1).value
            content_row_up1 = workbook[sheet_name].cell(row=row - 1, column=1).value

            if name in content_row_up2:
                address = f"{content_row_up1} {content}"
                address = str(address).strip()
                address = clean_known_address(address)
                return address
            else:
                return None

        else:
            # we did not find an address
            return None

        # END `find_address` function


def check_if_already_found(key, result):
    """
    checks if data element exists in result dict and if so, if the value is not None
    :param key: key from result dict
    :type key: basestring
    :param result: dictionary of results
    :return: boolean
    """
    if key not in result.keys():
        return False
    elif result[key] is None:
        return False
    else:
        return True


if __name__ == '__main__':
    pass
