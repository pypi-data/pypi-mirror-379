# -*- coding: utf-8 -*-
"""
simple_gsheet_interface: Module to work with the most simple version with Google Sheets: READ, WRITE and CLEAR data from an existing spreadsheet of Google
"""
__author__  = "Robert Rijnbeek"
__email__   = "robert270384@gmail.com"
__version__ = "0.0.4"

# ============ IMPORTS =============

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource

# ========= BASE PARAMETERS ========

SCOPES = ["https://spreadsheets.google.com/feeds"]

# == GOOGLE SHEET INTERFACE CLASS ==

class GoogleSheetInterface():
    def __init__(self,SheetID, service_account_file_location):
        self.SCOPES = SCOPES 
        self.SERVICE_ACCOUNT_FILE = service_account_file_location
        self.SHEET_ID = SheetID
        self.CREDENTIALS = Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes = self.SCOPES)
        self.SERVICE: Resource = build("sheets", "v4", credentials=self.CREDENTIALS)
        self.SHEET = self.SERVICE.spreadsheets()

    def read(self,RANGE):
        sheet_read = self.SHEET.values().get(spreadsheetId=self.SHEET_ID ,range=RANGE).execute()
        return sheet_read.get("values", [])
    
    def write(self,RANGE,VALUES):
        body = {"values": VALUES}
        return self.SHEET.values().update(spreadsheetId=self.SHEET_ID, range=RANGE, valueInputOption='USER_ENTERED', body=body).execute() #RAW
    
    def clear(self,RANGE):
         return self.SHEET.values().clear(spreadsheetId=self.SHEET_ID ,range=RANGE).execute()

    # =============== EXECUTE TEST CODE ==============

if __name__ == "__main__":

    pass
    