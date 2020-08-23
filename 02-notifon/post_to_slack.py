# coding: utf-8
import requests
url = '' # Replace with slace webhook URL
data = { "text": "Hello, Tom!"}
requests.post(url, json=data)
