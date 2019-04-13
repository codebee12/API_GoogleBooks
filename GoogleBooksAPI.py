#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:24:10 2019

@author: busybee
"""


#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pprint
import sys
from apiclient.discovery import build

# Place your API here as a string
api_key = "XXXXXXXX"

# The apiclient.discovery.build() function returns an instance of an API service
# object that can be used to make API calls. The object is constructed with
# methods specific to the books API. The arguments provided are:
#   name of the API ('books')
#   version of the API you are using ('v1')
#   API key
service = build('books', 'v1', developerKey=api_key)

# The books API has a volumes().list() method that is used to list books
# given search criteria. Arguments provided are:
#   volumes source ('public')
#   search query ('android')
# The method returns an apiclient.http.HttpRequest object that encapsulates
# all information needed to make the request, but it does not call the API.
request = service.volumes().list( q='Data Analytics')

# The execute() function on the HttpRequest object actually calls the API.

response = request.execute()

# It returns a Python object built from the JSON response. You can print this
# object or refer to the Books API documentation to determine its structure.
pprint.pprint(response)

# Accessing the response like a dict object with an 'items' key returns a list
# of item objects (books). The item object is a dict object with a 'volumeInfo'
# key. The volumeInfo object is a dict with keys 'title' and 'publisher'.
print ('Found %d books:' % len(response['items']))
for book in response.get('items', []):
  print ('Title: %s, Publisher: %s' % (
    book['volumeInfo']['title'],
    book['volumeInfo']['publisher']))