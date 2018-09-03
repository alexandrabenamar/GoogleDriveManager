from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1fwX3JyFo2I_ojpIDePvgOj9aQH039xQfaOznVxZwDhU'
SAMPLE_RANGE_NAME = 'A2:E'

def getemailadress(item, mailadress):
    """
        Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
    """
    store = file.Storage('tokenSheet.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('./credentials/credentialsSheet.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1fwX3JyFo2I_ojpIDePvgOj9aQH039xQfaOznVxZwDhU'
    RANGE_NAME = 'A2:E'

    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            if (row[1].lower() == mailadress):
                return(row[2])
        return

if __name__ == '__main__':
    getemailadress(item, mailadress)
