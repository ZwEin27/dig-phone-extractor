import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from phone_extractor import PhoneExtractor

class TestPhoneExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_phone_extractor(self):
        doc = { 'content': 'Sexy new girl in town searching for a great date wiff u Naughty fresh girl here searching 4 a great date wiff you Sweet new girl in town seeking for a good date with u for80 2sixseven one9zerofor 90hr incall or out call', 'b': 'world'}

        extractor = PhoneExtractor().set_metadata({'extractor': 'phone'})
        extractor_processor = ExtractorProcessor().set_input_fields('content').set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted']['value'], ['4802671904'])

    

if __name__ == '__main__':
    unittest.main()

    # def run_main_test():
    #     suite = unittest.TestSuite()
    #     suite.addTest(TestCSVMethods("test_read_csv"))
        
    #     runner = unittest.TextTestRunner()
    #     runner.run(suite)

    # run_main_test()



