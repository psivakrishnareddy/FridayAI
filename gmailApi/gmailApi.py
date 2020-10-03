from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

service = None


def Authenticate_gmail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    global service
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('gmailApi/token.pickle'):
        with open('gmailApi/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'gmailApi/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('gmailApi/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)


def list_mails():
    mail = []
    # global service
    # # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])

    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'])

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(
        userId='me', labelIds=['UNREAD'], q="in:inbox is:unread -category:(promotions OR social)", maxResults=5).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
    else:
        for message in messages:
            # message = messages[0]
            msg = service.users().messages().get(
                userId='me', id=message['id'], format="full").execute()
            headers = msg["payload"]["headers"]
            # print(headers)
            for i in headers:
                if i['name'] == "Subject":
                    subject = i['value']
                if i['name'] == "From":
                    Sender = i['value']
            # print("==================================\n")
            # print("█ " + subject + " Sent By " + Sender + " █")
            # print(msg['snippet'])
            # print("==================================\n")
        # print(msg)
            c = {"subject": subject, 'msg': msg['snippet'], 'sender': Sender}
            mail.append(c)
        return mail


Authenticate_gmail()
