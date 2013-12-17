import unittest
from collections import namedtuple

from data_generator import create_options_tuple, create_cleaned_data

"""
GOAL:
    class / init / process/ opts / opts_tuple

class RunCreator(object):

    def __init__(self, datastore):
        self._datastore = datastore

    def process(self, cleaned_data, created_by):

        opts = ExtractionRunCreateOptions(
            created_by,
            self.cleaned_data["machine"],
            self.cleaned_data["run_name"],
            self.cleaned_data["run_description"],
            self.cleaned_data["barcodes"],)
    return create_extraction_run(self._datastore, opts)

        self.valid_data = {
            'name': 'Hamlet',
            'description': 'This above all: to thine own self be true',
            'type': 'CLIA',
            'status': 'Pass QC',
            'data_files': SimpleUploadedFile(upload_file.name, upload_file.read()),
            'timestamp': datetime.datetime.now()
            }
"""


class TestDataGenerator(unittest.TestCase):

    def setUp(self):
        self.form = 'ExtractionRunCreate'
        self.more_params = ['user_email']
        self.fields = ['name', 'description', 'machine', 'barcodes']
        self.tab_depth = 2
        self.opts = "ExtractionRunCreateOptions = namedtuple('ExtractionRunCreateOptions', ['user_email', 'name', 'description', 'machine', 'barcodes'])"
        self.opts_with_cleaned_data = "\t\topts = ExtractionRunCreateOptions(\n\t\t\tuser_email,\n\t\t\t" + "\n\t\t\t".join(["self.cleaned_data['{}'],".format(field) for field in self.fields]) + ")"

    def test_create_options_tuple(self):
        self.assertEqual(self.opts, create_options_tuple(self.form, self.more_params, self.fields))

    def test_create_cleaned_data(self):
        self.assertEqual(self.opts_with_cleaned_data, create_cleaned_data(self.form, self.more_params, self.fields, self.tab_depth))

    def test_create_valid_data(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
