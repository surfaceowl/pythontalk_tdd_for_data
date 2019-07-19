# file encoding: utf-8
"""
configuration info for name and address logic
"""

# data and test data paths and common files
datapath_tests = "./data/test_cais/"

# all cais excel files from pdf directories are organized by section, with specific cell content
# first three members of this list must be in the order: MEMBER SCHOOLS, HEADS, DIRECTORS
list_section_names = ["MEMBER SCHOOLS",
                      "PROVISIONAL SCHOOLS",
                      "HEADS OF SCHOOL",
                      "Officers",
                      "CAIS BOARD OF DIRECTORS"]

list_school_synonyms = ["school", "schools", "schoolhouse",
                        "academy", "hall", "education", "center",
                        "ecole", "lycée", "Escuela Bilingüe Internacional",
                        "Heschel West", "Marymount of Santa Barbara"]

list_non_name_stopwords = ["Head", "Grades", "Enrollment",
                           "Military Boarding/Day School for Boys",
                           "Preschool",
                           "Elementary School",
                           "Elementary School Campus",
                           "Lower and Middle School",
                           "Middle and Upper School Campus",
                           "Lower Campus",
                           "Upper Campus",
                           "Elementary and Middle Schools",
                           "Lower School",
                           "Middle School",
                           "Upper School",
                           "26800 South Academy Drive Palos Verdes Peninsula, CA 90274",
                           "4400 Day School Place Santa Rosa, CA 95403",
                           "President", "Stuart Hall High School",
                           "Early Learning Center",
                           "Vivian Webb School Boarding/Day School for Girls Webb School of "
                           "California Boarding/Day School for Boys",
                           "1 Carey School Lane"]

# these words are only stopwords if they are on a line by themselves
# but when in a name string they are ok
list_non_name_standalone_stopwords = [
    "Preparatory School", "1678 School Street",
    "High School"]

# list of schools with known formatting problems
# program should be able to find these, but does not - so using list of known schools
# to minimize dev and test time
list_school_format_safe_list = ["Blue Oak School",
                                "The Girls’ Middle School",
                                "Head-Royce School",
                                "Lycée Français de San Francisco",
                                "Marin Primary & Middle School",
                                "Peninsula Heritage School",
                                "Prospect Sierra School",
                                "Santa Barbara Middle School",
                                "Seven Arrows Elementary School",
                                "Wildwood School",
                                "Turning Point School",
                                "Peninsula Heritage School",
                                "Oakwood School "]

