# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:24:38 2020

@author: vieth
"""

import aws_utils

key_id = 'AKIAR7OANEE3C4GP2AHP'
secret_key = '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'
region_name = 'us-east-2'

file_name = 'iris.csv'
s3 = aws_utils.s3_conn(key_id, secret_key, region_name)

bucket_name = 'newbie-test-1'

#aws_utils.upload_dataset(s3, bucket_name, file_name)
#aws_utils.new_all(s3, 'new-test-1', file_name, region_name)

print (s3)
