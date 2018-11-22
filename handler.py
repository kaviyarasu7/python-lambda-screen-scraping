# requirements -"gspread" "nsetools" "oauth2client" "PyOpenSSL" "bs4" "requests"
import json
import requests
import bs4
from nsetools import Nse
import datetime 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config_file import *

def pull_nse(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response