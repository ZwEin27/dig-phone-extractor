# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-21 12:36:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-28 08:40:47

import copy 
import types
from digExtractor.extractor import Extractor
from pnmatcher import PhoneNumberMatcher

class PhoneExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['url', 'raw_content']  # ? renamed_input_fields

    def extract(self, doc):
        if not 'url' in doc or not 'raw_content' in doc:
            return None

        extractor = PhoneNumberMatcher(_output_format='obfuscation')
        extracts = []
        if 'url' in doc:
            extracts += extractor.match(doc['url'], source_type='url')
        if 'raw_content' in doc:
            extracts += extractor.match(doc['raw_content'], source_type='text')
        return extracts

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields

    def set_renamed_input_fields(self, renamed_input_fields):
        if not (isinstance(renamed_input_fields, basestring) or isinstance(renamed_input_fields, types.ListType)):
            raise ValueError("renamed_input_fields must be a string or a list")
        self.renamed_input_fields = renamed_input_fields
        return self 


if __name__ == '__main__':
    from digExtractor.extractor import Extractor
    from digExtractor.extractor_processor import ExtractorProcessor

    # doc = { 'content': '       Share Record         Full Name Zasha  Naara  Hurst  Birth Date Jun 1977  Age 39      Associated Names        Lasha  Hurst           Possible Relatives    Current & Past Addresses        34650 Marcia Rd #4 ,  Cathedral City, CA 92234     Current Address      4030 Hillview Rd ,  Santa Maria, CA 93455      (Feb 2001 - Mar 2008)      34650 Marcia Rd #4 ,  Cathedral City, CA 92234      (Oct 2004)      1023 Stokes Ave ,  Santa Maria, CA 93454      (Jul 1996 - Apr 1998)            Phone Numbers        (760) 861-3197    341-7790    (805) 928-0120         SOURCE: familytreenow.com.  Living People Records  [online].  Original Data: familytreenow.com.  Compiled from 1000\'s of U.S. Public Records Sources, including property, business, historical and current records .', 'url': 'http://liveescortreviews.com/ad/philadelphia/602-228-4192/1/310054','b': 'world'}

    doc = { 'content': 'Share Record \n \n \n \n \n \n \n \n Full Name Zasha  Naara  Hurst \n Birth Date Jun 1977 \n Age 39 \n \n \n \n \n Associated Names \n \n \n \n \n \n \n \nLasha  Hurst \n \n \n \n \n \n \n \n \n \n Possible Relatives \n \n \n Current & Past Addresses \n \n \n \n \n \n \n \n34650 Marcia Rd #4 ,  Cathedral City, CA 92234     \nCurrent Address  \n \n \n \n \n4030 Hillview Rd ,  Santa Maria, CA 93455     \n \n(Feb 2001 - Mar 2008)\n \n \n \n \n \n \n34650 Marcia Rd #4 ,  Cathedral City, CA 92234     \n \n(Oct 2004)\n \n \n \n \n \n \n1023 Stokes Ave ,  Santa Maria, CA 93454     \n \n(Jul 1996 - Apr 1998)\n \n \n \n \n \n \n \n \n \n \n \n Phone Numbers \n \n \n \n \n \n \n \n(760) 861-3197 341-7790 (805) 928-0120\n \n \n \n \n \n \n \n \n SOURCE: familytreenow.com.  Living People Records  [online].  Original Data: familytreenow.com.  Compiled from 1000\'s of U.S. Public Records Sources, including property, business, historical and current records . \n \n \n', 'url': 'http://liveescortreviews.com/ad/philadelphia/602-228-4192/1/310054','b': 'world'}

    extractor = PhoneExtractor().set_metadata({'extractor': 'phone'})
    extractor_processor = ExtractorProcessor().set_input_fields(['url', 'content']).set_output_field('extracted').set_extractor(extractor)
    updated_doc = extractor_processor.extract(doc)
    print updated_doc['extracted'][0]['value']
    





