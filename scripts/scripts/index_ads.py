# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-08-10 13:53:23
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-11-04 11:56:26

"""
python index_ads.py -t <USERNAME>:<PASSWORD> -i <INPUT_FILE_PATH> -o <OUTPUT_FILE_PATH>

"""

import urllib3
import re
import sys
from elasticsearch import Elasticsearch, helpers
import json
import getopt
import hashlib

urllib3.disable_warnings()


######################################################################
#   Query
######################################################################

query = {
    "query": {
        "constant_score" : {
            "filter" : {
                "terms" : { "mainEntity.seller.telephone.name" : ["8146513184"]}
            }
        }
    },
    "size": 7372220
}
# 7372220
######################################################################
#   Main Class
######################################################################

class Streamer(object):

    def __init__(self, token):
        self.cdr = 'https://' + token + '@esc.memexproxy.com/dig-2'
        self.es = Elasticsearch([self.cdr], timeout=86400) # timeout=3600

    def generate(self, input_path=None, output_path=None):
        phone_numbers = []
        with open(input_path, 'r') as file_handler:
            for line in file_handler:
                phone_numbers.append(line.strip())

        """ scroll
        ans = []
        try:
            query['query']['constant_score']['filter']['terms']['mainEntity.seller.telephone.name'] = phone_numbers

            # ans = helpers.scan(client=self.es, query=query, scroll='90m', index='webpage', timeout='10m')
            # ans = self.es.search(index='webpage', body=query)
            

            page = self.es.search(
                      index='webpage',
                      # doc_type='webpage',
                      scroll='2m',
                      # search_type='scan',
                      size=1000,
                      body=query)
            # page = self.es.search(index='webpage', body=query, doc_type='json',search_type='scan',scroll='1m', size=1000)   # search_type = 'scan'
            # print json.dumps(page, indent=4)
            # ans.extend([_['_source'] for _ in page['hits']['hits']])
            
            sid = page['_scroll_id']
            scroll_size = page['hits']['total']
            print scroll_size
            while (scroll_size > 0):
                print "Scrolling..."
                # print sid
                # ans.extend(page['hits']['hits'])
                try:
                    page = self.es.scroll(scroll_id=sid, scroll='2m')
                except Exception as e:
                    print 'except', e
                # print page
                # Update the scroll ID
                sid = page['_scroll_id']
                # Get the number of results that we returned in the last scroll
                scroll_size = len(page['hits']['hits'])
                print "scroll size: " + str(scroll_size)
        # ans = page
        # print json.dumps(ans, indent=4)

        # return
        """

        try:
            query['query']['constant_score']['filter']['terms']['mainEntity.seller.telephone.name'] = phone_numbers
            ans = self.es.search(index='webpage', body=query)       
        except Exception as e: 
            print e
            return
            raise Exception('phone number is incorrect')
        
        ans = ans['hits']['hits']
        

        if output_path:
            file_handler = open(output_path, 'wb')
            # file_handler.write(json.dumps(ans, sort_keys=True, indent=4))
            i = 0
            for item in ans:
                print 'process line:', i
                file_handler.write(json.dumps(item['_source']) + '\n')
                i += 1
            file_handler.close()

        return ans

if __name__ == '__main__':
    import sys
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-t','--token', required=True)
    arg_parser.add_argument('-i','--input_path', required=False)
    arg_parser.add_argument('-o','--output_path', required=False)

    args = arg_parser.parse_args()

    streamer = Streamer(args.token)
       
    streamer.generate(input_path=args.input_path, output_path=args.output_path)