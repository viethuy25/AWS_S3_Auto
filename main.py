# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:24:38 2020

@author: vieth
"""

import aws_utils
from flask import Flask, request, render_template, session, redirect
import flask_utils

app = Flask(__name__)

flask_utils.app.run()