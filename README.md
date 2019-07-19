# Project Title

TDD (Test Driven Development) is great for software engineering, but did you know TDD can add a lot of speed and quality to Data Science projects too? We'll learn how we can use TDD to save you time - and quickly improve functions which extract and process data.  Written for *[Pyninsula Meetup #19](https://www.meetup.com/Pyninsula-Python-Peninsula-Meetup/events/262633295/)* in July 2019.

## Getting Started

Clone this repo to get a copy of the project up and running.  All data is already public, and included in files under /data.

### Prerequisites

Python v3.7 or greater
a python-friendly IDE

### Installing

Clone the repo from either the terminal or your IDE.

```
git clone https://github.com/surfaceowl/pythontalk_tdd_for_data.git
```

From project root (pythontalk.tdd_for_data), create a virtual environment called `venv`

```
virtualenv venv
```

Activate the virtual environment

```
(for linux/unix):  source venv/bin/activate
(for windows);  venv/Scripts/activate
```

Install the python packages in requirements.txt
```
pip install -r requirements.txt
```

Launch jupyter notebook, open `TDD_for_data_cleaning_with_pytest.ipynb` and review the presentation slides
```
jupyter notebook
```

## Running the tests

There are five test files to explore:

test_00_simple_pytest_example.py

test_01_datatest_example.py

test_02_cais_find_url_examples.py -- requires editing /src/read_excel_info.find_url to make tests pass

test_03_cais_name_count_2013.py -- illustrates using supplemental input files for testing

PARK_test_04_cais_name_count_2018.py


## Built With

* [pytest](https://docs.pytest.org/en/latest/ ) - framework for writing and running tests
* [datatest](https://datatest.readthedocs.io/en/stable/) - data-wrangling and data validation in a testing framework
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - library to read/write Microsoft Excel files (2010 and later)


## Authors

* **Chris Brousseau** - *Initial work* - [surfaceowl](https://github.com/surfaceowl?tab=repositories)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc