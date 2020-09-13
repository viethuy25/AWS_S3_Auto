# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:38:08 2020

@author: vieth
"""

import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})
app.run()