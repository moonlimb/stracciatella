import re
import sys

from data_generator import create_options_tuple, create_options_data

# Refer to notes.txt for details

# TODO: may need to replace all instances of \t with TAB
TAB = '\s\s\s\s'

IMPORTS = {
    'unittest': 'from unittest import TestCase',
    'hamcrest': 'from hamcrest import assert_that, is_, has_length',
    'mock': 'from mock import Mock',
    'newline': '\n',
    'form': 'from weblims.apps.{}.forms import {}'
    }

#make indentation configurable?
VALID_DATA = {
    'opening_dict': '\s'*8 + 'self.valid_data = {\n' + '\s'*12,
    'line': '\s'*12 + "'{}': '{}',",
    'closing_dict':  '\s'*12 + '}'
    }


# Theoretically, not suppose to provide mutable datatype as default; ask others
field_to_empty_str = lambda field: VALID_DATA['line'].format(field)

def map_field_to_empty_str(field, data=""):
    return VALID_DATA['line'].format(field, data)

#TODO: WRITE A TEST FOR this fcn
def file_parser(file):
    """
    Returns a list containing all form field names in the given file; Assumes that the given file object is a DJ form
    """
    # ** use regex validator to grab field name in between <tab>field_name<space><equal sign> **
    field_names = []
    re_field = re.compile(r'^\s{4}(\w+)\s\=.+$')
    re_class = re.compile(r'^class\s(\w+)Form\(.+$')
    # can make space before '=' optinal
    # tab or s*$

    #MAKE THIS BETTER
    newline = file.next()
    form_class = None

    while not form_class:
        newline = file.next()
        form_class = re.match(re_class, newline)

    class_name = form_class.group(1)
    while True:
        try:
            newline = file.next()
            # CREATE AN ABSTRACTION LAYER OR figure out better to way to avoid repetition below

            field_validity = re.match(re_field, newline)
            if field_validity:
                field_names.append(field_validity.group(1))  #grab field name
        except StopIteration:
            break
    return {'field_names': field_names, 'form_class': class_name}


def form_test_generator(form_file_path):
    """
    Receives as an input form filename in str, opens the file, and writes string that will be written to test_script

    Calls field_list_generator with file content 

    For now:
     * ignore all lines that do not match re_field
    """
    data_content = []

    with open(form_file_path, 'r') as f:
        parsed_file_info = file_parser(f)
        form_class = parsed_file_info['form_class']
        field_names = parsed_file_info['field_names']
        data_content.append(create_options_data(form_class, [], field_names, 2))
        data_content.append(create_options_tuple(form_class, [], field_names))

    import ipdb; ipdb.set_trace()

    return data_content


if __name__ == '__main__':

    if len(sys.argv) > 2:
        test_form_script = 'test_{}.py'.format(sys.argv[1]) # give test file name as the first CML arg
        list_of_form_files = sys.argv[2:]

        with open(test_form_script, 'w') as f:
            for file_name in list_of_form_files:
                results = form_test_generator(file_name)
                f.write(form_test_generator(file_name)) #creates & wrties form test in test_form_script

        print("\nNew test script created -> {}\n".format(test_form_script))

    elif len(sys.argv) == 2:
        print("\nProvide file name for test_{name}.py as the first argument and form script names as subsequent"
              " arguments.\n")

    else:
        print("\nNo test file name and form script(s) given.\n")
