import sys
import time
import json
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digPhoneExtractor.phone_extractor import PhoneExtractor

class TestPhoneExtractorMethods(unittest.TestCase):

    def setUp(self):
        self.groundtruth_data = groundtruth.load_groundtruth()

    def tearDown(self):
        pass

    def test_phone_extractor(self):
        doc = { 'content': 'Sexy new girl in town searching for a great date wiff u Naughty fresh girl here searching 4 a great date wiff you Sweet new girl in town seeking for a good date with u for80 2sixseven one9zerofor 90hr incall or out call', 'url': 'http://liveescortreviews.com/ad/philadelphia/602-228-4192/1/310054','b': 'world'}

        extractor = PhoneExtractor().set_metadata({'extractor': 'phone'})
        extractor_processor = ExtractorProcessor().set_input_fields(['url', 'content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted'][0]['value'], [{'obfuscation': 'False', 'telephone': '6022284192'}, {'obfuscation': 'True', 'telephone': '4802671904'}])

    def test_groundtruth(self):
        extractor = PhoneExtractor().set_metadata({'extractor': 'phone'})
        extractor_processor = ExtractorProcessor().set_input_fields(['url', 'body', 'title']).set_output_field('extracted').set_extractor(extractor)
        for doc in self.groundtruth_data[:60]:
            # print doc
            updated_doc = extractor_processor.extract(doc)
            # a = set([_['telephone'] for _ in updated_doc['extracted'][0]['value']])
            b = set(doc['url_ext_gt'])|set(doc['text_ext_gt'])

            if 'extracted' not in updated_doc:
                self.assertEqual(set(), set(doc['url_ext_gt'])|set(doc['text_ext_gt']))
            else:
                self.assertEqual(set([_['telephone'] for _ in updated_doc['extracted'][0]['value']]), set(doc['url_ext_gt'])|set(doc['text_ext_gt']))
                # print updated_doc['extracted'][0]['value']
    

    def test_groundtruth_sample(self):
        doc = {
              "url": "",
              "title": "deyi linda y sexy llamame papi 7864865044tengo una amiguita servicio a parejas. - Miami escorts - backpage.com",
              "body": "",
              "url_ext_gt": [],
              "text_ext_gt": ["7864865044"]
            }

        extractor = PhoneExtractor().set_metadata({'extractor': 'phone'})
        extractor_processor = ExtractorProcessor().set_input_fields(['url', 'title', 'body']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        a = set([_['telephone'] for _ in updated_doc['extracted'][0]['value']])
        b = set(doc['url_ext_gt'])|set(doc['text_ext_gt'])
        self.assertEqual(a, b)
    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()

        # suite.addTest(TestPhoneExtractorMethods('test_phone_extractor'))
        suite.addTest(TestPhoneExtractorMethods('test_groundtruth'))
        # suite.addTest(TestPhoneExtractorMethods('test_groundtruth_sample'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()




