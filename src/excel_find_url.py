# %load src/excel_find_url.py
# %%writefile src/excel_find_url.py


import re

from src.excel_read_cell_info import check_if_already_found


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
    # https://regex101.com  -- use this to test different regex vs data patterns

    # regex = re.compile(r"w{3}.*", re.IGNORECASE)
    # regex = re.compile(r"(http|https):\/\/.*", re.IGNORECASE)  # EDIT THIS LIVE

    regex = re.compile(
    r"((http|https):\/\/)?[a-zA-Z0-9.\/?::-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9..\/&\/\-_=#])*",
    re.IGNORECASE)

    try:
        match = re.search(regex,
                          str(content))
    except TypeError:
        raise TypeError

    if match:
        url = str(match.group()).strip()
        return url
    else:
        return None
