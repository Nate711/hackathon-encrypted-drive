###only uploads plaintext


#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow


# Copy your credentials from the console
CLIENT_ID = '525402384233-lg16n5981raug5jc2ou8rghs2je0s16d.apps.googleusercontent.com'
CLIENT_SECRET = 'zaITwVEagm-bYu4sSd-Z3-T4'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Path to the file to upload
### I am doing things here!
input = raw_input("Enter Filename \n> ")
FILENAME = input#'document.txt'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': input,
  'description': 'A test document',
  'mimeType': 'text/plain'
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)