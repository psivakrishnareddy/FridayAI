from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pytz
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


MONTHS = ['january', 'febuary', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']
DAYS = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']
DAY_EXTENSIONS = ['rd', 'th', 'nd', 'st']


def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def get_events(day, service):
    # Call the Calendar API

    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    e = []

    if not events:
        # print('No upcoming events found.')
        return None
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            e.append((start, event['summary']))
        return e


def get_upcoming_events(service, date=None):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    if date:
        now = datetime.datetime.combine(date, datetime.datetime.min.time())
        # end_date = datetime.datetime.combine(day,datetime.datetime.max.time())
        utc = pytz.UTC
        now = now.astimezone(utc)
        # end_date = end_date.astimezone(utc)
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    e = []

    if not events:
        # print('No upcoming events found.')
        return None
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            e.append((start, event['summary']))
        return e


def get_upcoming_events_month(day, service):
    # Call the Calendar API

    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = date + datetime.timedelta(days=31)
    end_date = datetime.datetime.combine(
        end_date, datetime.datetime.min.time())
    # print(end_date)
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                          maxResults=6, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    e = []

    if not events:
        # print('No upcoming events found.')
        return None
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            e.append((start, event['summary']))
        return e


def get_date_fromText(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count('today') > 0:
        return today
    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENSIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year+1
    if day < today.day and month == -1 and day != -1:
        month = month + 1
    if month == -1 and day != -1:
        month = today.month
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()

        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count('next') >= 1:
                dif += 7

        return today + datetime.timedelta(dif)
    if month == -1 and day == -1 and day_of_week == -1:
        current_day_of_week = today.weekday()

        dif = day_of_week - current_day_of_week
        if text.count('tomorrow') >= 1:
            dif = 1
        else:
            dif = 0
        return today + datetime.timedelta(dif)
    if month != -1 and day == -1 and day_of_week == -1:
        day = 1

    if month == -1 and day == -1:
        return None

    return datetime.date(month=month, day=day, year=year)


# s = authenticate_google()
# text = 'what do we have on 24'
# print(get_date_fromText(text))
# print(get_events(get_date_fromText(text), s))
# print(get_upcoming_events(s))

''' You can ask about abt a date in anyway'''
