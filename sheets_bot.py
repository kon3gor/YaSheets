import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
import util
import datetime


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


class SheetsProxy(object):

    sheet_id: str
    service: Resource

    def __init__(self, sheet_id: str) -> None:
        self.sheet_id = sheet_id
        self.service = self._auth()

    def _auth(self) -> Resource:
        creds_file = os.environ.get("CREDS_FILE_NAME")
        creds = service_account.Credentials.from_service_account_file(
            filename=creds_file,
            scopes=SCOPES
        )
        return build('sheets', 'v4', credentials=creds)

    def append_range(self, values: list, range: str) -> None:
        body = {
            "values": values
        }
        result = self.service.spreadsheets().values().append(
            spreadsheetId=self.sheet_id,
            valueInputOption="RAW",
            body=body,
            range=range
        ).execute()
        return result

    def read_range(self, range: str) -> dict:
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.sheet_id,
            range=range
        ).execute()
        return result


def add_answer(sheet_id: str, answer: dict) -> None:
    proxy = SheetsProxy(sheet_id)
    header = check_has_header(proxy)
    answer["date"] = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))
    if (not header):
        header = list(answer.keys())
        range = f"A1:{util.num_to_char(len(header))}1"
        proxy.append_range([header], range)

    new_header_values = has_new_header_values(header, answer.keys())
    if (new_header_values):
        print(new_header_values, header)
        old_len = len(header)
        new_len = old_len + len(new_header_values)
        header += new_header_values
        range = f"{util.num_to_char(old_len + 1)}1:{util.num_to_char(new_len)}1"
        proxy.append_range([new_header_values], range)

    values = []
    for header_value in header:
        values.append(answer.get(header_value, "-"))

    range = f"A1:{util.num_to_char(len(values))}1"
    proxy.append_range([values], range)


# Either returns new header values of the sheet or returns None if there is nothing new
def has_new_header_values(header: list, new_header: list) -> list:
    m = {}
    new_header_values = []

    for hv in header:
        m[hv] = True

    for hv in new_header:
        if m.get(hv, False):
            continue
        new_header_values.append(hv)

    return new_header_values


# Either returns header of the sheet or returns None if there is no header
def check_has_header(proxy: SheetsProxy) -> list:
    range = "A1:Z1"
    first_row_values = proxy.read_range(range).get("values", None)
    if (first_row_values):
        return first_row_values[0]
    else:
        return None
