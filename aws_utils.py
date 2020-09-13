# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:13:12 2020

@author: vieth
"""
import boto3
import pandas as pd
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
    bucket = s3.Bucket(bucket_name) # example: energy_market_procesing
    
    initial_df = pd.DataFrame()
    # Iterates through all the objects, doing the pagination for you. Each obj
    # is an ObjectSummary, so it doesn't contain the body. You'll need to call
    # get to get the whole body.
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        print (key)
        print (file_name)
        
        if key.lower()==file_name.lower():
            body = obj.get()['Body']#.read()
            initial_df = pd.read_csv(body) #obj['Body']) # 'Body' is a key wor
    
    #obj = s3.get_object(Bucket= bucket_name, Key= file_name) 
    
    #initial_df = pd.read_csv(obj['Body']) # 'Body' is a key wor
    
    return initial_df

def new_all(s3, bucket_name, file_name, region_name):
    location = {'LocationConstraint': region_name}
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    upload_dataset(s3, bucket_name, file_name)