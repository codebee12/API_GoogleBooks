# API_GoogleBooks
This repo contains simple code and instruction on how to use Google Books API using Python. 

Pre-requisites:
1. Should have Python3 on system.
2. Should have a Google account.
3. Shoud install google-api-client. 

How to install google-api-client:

 Run on Terminal: sudo pip3 install --upgrade google-api-python-client
If your are using an IDE like Spyder then run this on the IPython console:
!pip3 install --upgrade google-api-python-client

If there are issues with installantion, you may have a look at this:
https://stackoverflow.com/questions/35982655/python-install-module-apiclient

Generate API Key using your Google Account:

1. Navigate to the APIs & Services→Credentials panel in GCP Console.
2. Select Create credentials, then select API key from the dropdown menu.
3. Click the Create button. The API key created dialog box displays your newly created key.

Reference: https://cloud.google.com/docs/authentication/api-keys?visit_id=636906006426226894-564985462&rd=1

Before running:
Change the api_key in the code to the one you have generated. 

References: https://developers.google.com/books/
