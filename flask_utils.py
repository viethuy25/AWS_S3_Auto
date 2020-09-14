# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:38:08 2020

@author: vieth
"""

from flask import Flask, request, render_template, session, redirect
import aws_utils
import pandas as pd
import json

def read_user(user):
    with open(user,) as f:
        data = json.load(f)

    # Output: {'key_id': , "secret_key" : , "region_name" : }
    print(data)
    return data

app = Flask(__name__)
@app.route('/', methods=("POST","GET"))
def index():
    return render_template("index.html")

@app.route('/table', methods=("POST", "GET"))
def html_table():
    data = read_user('data/bucket_policy.json')
    file_name = 'iris.csv'
    s3 = aws_utils.s3_conn(data['key_id'], data['secret_key'], data['region_name'])
    
    bucket_name = 'newbie-test-1'
    
    #aws_utils.upload_dataset(s3, bucket_name, file_name)
    #aws_utils.new_all(s3, 'new-test-1', file_name, region_name)
    
    file = aws_utils.read_csv(s3, bucket_name, file_name)
    
    print (s3)
    print (type(file))

    # link_column is the column that I want to add a button to
    return render_template("simple.html", column_names=file.columns.values, 
                           row_data=list(file.values.tolist()), zip=zip)

