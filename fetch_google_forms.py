import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd
from IPython.display import display

SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1TXZzfvJvpvGe6v70CvVRe5N8hgi74D0T1Trr91juqyA"


def fetch_new_user():
    credentials = None
    
    # Check if token.json file exists
    if os.path.exists("token.json"):
        # Load credentials from the token file
        credentials = Credentials.from_authorized_user_file("token.json", SCOPE)
        
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            # Refresh expired credentials
            credentials.refresh(Request())
        else:
            # Load credentials using client secrets file
            flow = InstalledAppFlow.from_client_secrets_file("google_client_id.json", SCOPE)
            credentials = flow.run_local_server(port=0)
        
        # Save the updated credentials to token.json
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
            
    try:
        # Build the Sheets API service
        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API to get values
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A2:X").execute()
        values = result.get('values', [])

        return values[-1]
    except HttpError as error:
        print(error)


