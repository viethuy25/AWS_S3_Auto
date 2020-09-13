# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:13:12 2020

@author: vieth
"""
import boto3
import csv

def s3_conn(key_id, secret_key, regional_name):
    # get a handle on s3
    session = boto3.Session(
                    aws_access_key_id= key_id,
                    aws_secret_access_key=secret_key,
                    region_name=regional_name)
    
    s3 = session.resource('s3')

    return s3


def upload_dataset(s3, bucket_name, file_name):
    # get a handle on the bucket that holds your file
    bucket = s3.Bucket(bucket_name) # example: energy_market_procesing
    
    print(bucket)
    
    #upload files to S3 bucket
    bucket.upload_file(file_name, Key='Iris.csv')
    
def read_csv (s3,bucket_name, file_name):
    
obj = s3.get_object(Bucket= bucket, Key= file_name) 
# get object and file (key) from bucket

initial_df = pd.read_csv(obj['Body']) # 'Body' is a key wor

def new_all(s3, bucket_name, file_name, region_name):
    location = {'LocationConstraint': region_name}
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    upload_dataset(s3, bucket_name, file_name)