# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:24:38 2020

@author: vieth
"""

import aws_utils
import json

with open('data/bucket_policy.json',) as f:
    data = json.load(f)

# Output: {'key_id': , "secret_key" : , "region_name" : }
print(data)

file_name = 'iris.csv'
s3 = aws_utils.s3_conn(data['key_id'], data['secret_key'], data['region_name'])

bucket_name = 'newbie-test-1'

#aws_utils.upload_dataset(s3, bucket_name, file_name)
#aws_utils.new_all(s3, 'new-test-1', file_name, region_name)

file = aws_utils.read_csv(s3, bucket_name, file_name)

print (s3)
print (file)