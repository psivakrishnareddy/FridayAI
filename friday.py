# FRIDAY A.I ASSISTANT CREATED BY P. SIVA KRISHNA REDDY
# HELPS TO PERFORM TASKS LIKE, MAIL,CALENDERS , BROWSING, SEARCHING,WEATHER, NEWS, OPEN SITE,FILE,
# RUN SCRIPTS,CASUAL TALKS
from google import google  # pip install google-search-api
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import random
import os
import webbrowser
import pickle
import ctypes
import subprocess
import threading
import time as t
import datetime
import smtplib
import weatherApi  # owp api
import sys
import UI.UserInterface as ui
import calenderGoogle  # my google calendar module note the Spelling
from chatme import Respond_To_Command
from myscripts.news_api import send_top_news
import myscripts.systemUtility as su
import myscripts.cmdProtocols.voiceControls as vc
import myscripts.reminder as remindr
from FaceRecognition.recognize import Face_Recognizer_Friday
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# to prevent UserWarnings from printing in console
# Modules Loaded Here
# My modules


for i in range(150):
    t.sleep(0.01)
    ui.root.update()

# Setting the Engine voice
Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
Engine.setProperty('voice', voices[1].id)
vrate = Engine.getProperty('rate')
Engine.setProperty('rate', vrate)

error_count = 0  # count for no response from user

os.system('cls')  # Clears the Screen


def Art_Friday():
    # ui.lbl.cancelloop()
    ui.lbl.next_frame(0, 50)
    print('''
                ▒█▀▀▀ ▒█▀▀█ ▀█▀ ▒█▀▀▄ ░█▀▀█ ▒█░░▒█ 　 ░█▀▀█ ▀█▀ 
                ▒█▀▀▀ ▒█▄▄▀ ▒█░ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄█ 　 ▒█▄▄█ ▒█░ 
                ▒█░░░ ▒█░▒█ ▄█▄ ▒█▄▄▀ ▒█░▒█ ░░▒█░░ 　 ▒█░▒█ ▄█▄''')


# Command Knowlwdes
make_note_list = ['make a note', 'remember this', 'write this down']

calender_ask_list = ['check my schedules', 'show my schedules', 'check my plans', 'show my plans', 'am i busy',
                     'what do we have', 'what are my plans', 'when do i have', 'when is', 'do i have', "What are my upcoming events"]

email_contacts = {"shiva": 'p.sivakrishnareddy.siva@gmail.com',
                  'school': 'liveschoolfoundation@gmail.com', 'coordinator': 'mvp@rmkcet.ac.in', 'guide': 'samnaresh@gmail.com'}

Accept_words_list = ['yes', 'sure', 'ok', 'okay', 'yeah', 'do that', 'alright']

open_launch_list = {'open': 'open',  'launch': 'launch'}

Search_dict = {'who': 'who', 'what': 'what', 'whose': 'whose', 'why': 'why'}

google_search_list = ['can', 'learn']

weather_list = ['whats weather', 'how is weather',
                'weather details', 'about weather']

Shutdown = ['ok bye', 'bye', 'goodbye',
            'close', 'see you tomorrow', 'exit']

Standby_Triggers = ['nothing', 'standby', 'sleep',
                    'go sleep', 'bye for now', 'catch you later']


site_list = {'facebook': 'www.facebook.com', 'twitter': 'www.twitter.com', 'soundcloud': 'www.soundcloud.com', 'youtube': 'www.youtube.com', 'google': 'www.google.com', 'google': 'www.google.com',
             'skillrack': 'www.skillrack.com', 'hackerearth': 'www.hackerearth.com', 'hackerrank': 'www.hackerrank.com', 'amazon': 'www.amazon.in', 'youtube': 'www.youtube.com', 'university': 'coe2.annaedu.ac.in'}

common_apps = {"calculator": "C:\\WINDOWS\\system32\\calc.exe",
               'code': 'C:\\Users\\siva reddy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
               "photoshop": "C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (64 Bit)\\Photoshop.exe"}


'''FUNCTION FOR SPEAKING '''


def speak(audio):
    ui.lbl.cancelloop()
    print(f"Friday : {audio}")
    Engine.say(audio)
    ui.setCompText(audio)
    ui.lbl.next_frame(328, 364)
    Engine.runAndWait()
    ui.lbl.cancelloop()


# time in hour as global
time = int(datetime.datetime.now().hour)


def WishMe():
    # print(time)
    greeting = None
    if time < 4:
        greeting = "good morning Boss.. Looks like your working early today"
    elif 4 <= time < 12:
        greeting = "Good morning Boss"
    elif 12 <= time < 16:
        greeting = "Good AfterNoon Boss"
    elif 16 <= time <= 21:
        greeting = "Good Evening Boss"
    elif time >= 22:
        greeting = "Good Night Boss"
    speak(greeting)


def TakeCommand():
    # MAIN FUNCTION TO READ A USER VOICE INPUT
    ui.lbl.cancelloop()

    rObject = sr.Recognizer()
    audio = ''
    global error_count
    with sr.Microphone() as source:
        print("Listening...")
        ui.lbl.next_frame(184, 260)

        ui.setCompText("Listening...")
        ui.setUserText("Waiting For Commands..")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
        rObject.pause_threshold = 1

    try:
        query = rObject.recognize_google(audio, language='en-in')
        print("You :", query)
        ui.setUserText(query)
        error_count = 0
        ui.lbl.cancelloop()
        return query
    except sr.UnknownValueError as e:
        ui.lbl.cancelloop()
        ui.lbl.next_frame(50, 170)
        speak("Could not understand your audio, PLease try again !")
        error_count = error_count+1
        return ''

    except sr.RequestError as e:
        ui.lbl.cancelloop()
        speak("Network Error Boss.. Cant help you at the Moment... Reconnecting..")
        ui.lbl.next_frame(50, 170)
        print("Reconnecting... ")
        return 'errorfoundinlistening'

# Wake trigger Module


def Wake_listening():
    # TAKE COMMAND VARIATION FOR WAKE COMMAND INPUT
    speech = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        # print("Listening...")

        # recording the audio using speech recognition
        audio = speech.listen(source, phrase_time_limit=5)
        speech.pause_threshold = 0.6

    try:

        query = speech.recognize_google(audio, language='en-in')
        # print("You : ", query)
        return query
    except sr.UnknownValueError as e:
        return ''

    except sr.RequestError as e:
        speak("Network Error Boss.. Cant help you at the Moment... Reconnecting..")
        print("Reconnecting... ")
        return 'errorfoundinlistening'


def googleSearch(query):
    webbrowser.open_new_tab('www.google.co.in/search?q={}'.format(query))
    try:
        search_results = google.search(query, 1)
    except:
        speak('Unable to retrive results to speak')
        return
    i = 0
    for result in search_results:
        if i > 2:
            break
        finalres = result.description.rsplit('.', 3)[0]
        if finalres != '':
            i += 1
        title = result.name.split('https://')[0]
        print('Title:', title)
        print('Url:', result.link)
        speak(finalres)
        print()


def knowAbout(query, tp=''):
    # Searching

    speak('Give me a minute')
    ui.lbl.next_frame(365, 444)
    try:
        results = wikipedia.summary(query, sentences=2)
        speak(results)
        if tp == 'gnl':
            speak('Shall i show Google results?')
            if user_prompt_yes_no():
                speak('Here is what Google Says..')
                googleSearch(query)
    except:
        if tp != 'wkp':
            speak('Here is what i found..')
            googleSearch(query)
            return
        speak('Sorry i cant find about it in wikipedia...')
        speak('Shall i search Google ??')
        # ans = TakeCommand().lower().strip()
        if user_prompt_yes_no():
            speak('Here is what i found..')
            googleSearch(query)
        else:
            return


def is_valid_googleSearch(query):
    try:
        if query.split()[0] in google_search_list:
            return True
        else:
            return False
    except:
        pass


def is_valid_Search(query):
    # Checcking if valid googleSearch
    try:
        if(Search_dict.get(query.split(' ')[0]) == query.split(' ')[0]):
            return True
    except:
        pass


def is_valid_note(Dicts, query):
    for key, value in Dicts.items():
        try:
            if key == query.split(' ')[0]:
                return True
                break
            elif key == query.split(' ')[1]:
                return True
                break
        except IndexError:
            break
            pass
    return False


''' Smtp mail server '''


def sendMail(receiver, content):
    recmail = email_contacts[receiver]
    speak('Sending mail to {} ....'.format(receiver))
    msg = 'Subject: {}\n\n Hi,\n This is Friday AI assistant of Mr.Siva, \n He wants to let you know this... \n {}'.format(
        'F.R.I.D.A.Y AI OF SIVA (URGENT)', content)
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.login('yourmail@gmail.com', 'password')
        mailServer.sendmail('yourmail@gmail.com', recmail, msg)
        speak("Mail sent to {} !!".format(receiver))
    except Exception as e:
        speak("Unable to send mail right now")
        print(e)
    mailServer.close()


def getMailContent():
    cc = 0
    content = TakeCommand()
    while cc < 2:
        cc += 1
        if content == '':
            speak('your msg is empty, Add a msg!!')
            content = TakeCommand()
        else:
            break
    else:
        speak('Boss?? Okay Try sending mail later')
        content = None
        return

    return content


'''Send s ail by gathering info from user'''


def SendingMailPrompts(query):
    rc = 0
    sc = 0
    try:
        receiver = query.split('to')[1].strip()
    except:
        receiver = ''
    while rc < 2:
        rc += 1
        if receiver == '':
            speak('Who is the receiver ??')
            receiver = TakeCommand().lower().strip()
        elif receiver not in email_contacts:
            speak('No cantact with name sir!!')
            return
        else:
            break
    else:
        speak('looks Like your lost, Try again later')
        return
    speak('What should i say ?')
    content = getMailContent()
    if content == None:
        return
    try:
        while sc < 2:
            sc += 1
            speak("Do you  want to send it or Change it or Cancel it??")
            ans = TakeCommand().lower().strip()
            if 'change' in ans:
                content = getMailContent()
                if content == None:
                    return
            elif 'cancel' in ans:
                speak('cancelled')
                return
            elif 'send' in ans:
                break
        else:
            speak('Looks like your lost, Message Has been Cancelled.')
            return

        sendMail(receiver, content)
    except:
        speak("Cant send mails at the moment")


def read_mails_from_gmail():
    from gmailApi import gmailApi
    speak('Let Me Check for Unread Mails in your Inbox!!!')
    mails = gmailApi.list_mails()
    speak('Your Recent Unread E-mails Are:')
    for mail in mails:
        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n")
        speak(" █ " + mail['subject'] + " Sent By " + mail['sender'] + " █ ")
        speak(mail['msg'])
        print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n")


def user_prompt_yes_no():
    # for asking user yes or no
    ans = TakeCommand().lower().strip()
    if str(ans) in Accept_words_list:
        return True
    else:
        return False


def is_valid_calendarTask(lists, query):
    for i in lists:
        if i in query:
            return True
            break
    return False


def note_file(text):
    file_name = "userdata/" + \
        str(datetime.datetime.today()).replace(':', '-') + 'note.txt'
    with open(file_name, 'w') as f:
        f.write(text)
    subprocess.Popen(['notepad.exe', file_name])


def check_calendar(events, query):
    ui.lbl.cancelloop()
    ui.lbl.next_frame(365, 444)

    f = 0
    if events == None:
        speak('No Related event found!! Sir')
        return
    for e in events:
        if query in e[1].lower():
            DT = e[0].split('T')
            TS = DT[1].split('+')
            speak(f'{e[1]} on {DT[0]} at {TS[0]} to {TS[1]}')
            f = 1

    if f == 0:
        speak('No upcoing events Sir')


def calendar_events_google(date, s):
    ui.lbl.cancelloop()

    ui.lbl.next_frame(365, 444)

    # finds the event on a given date after conversion from text
    # global s
    date = calenderGoogle.get_date_fromText(date)
    # events = calenderGoogle.get_events(date )
    events = calenderGoogle.get_events(date, s)
    read_calendar_events(events, date)


def read_calendar_events(events, date=None):
    # Reads the Events loaded using calender
    if events is None:
        if date:
            speak(f'No plans on {date} sir!')
        else:
            speak('no upcoming events Sir')
    else:
        if date:
            speak(f'you have {len(events)} events  on {date} ')
            for e in events:
                DT = e[0].split('T')
                TS = DT[1].split('+')
                speak(f'{e[1]} at {TS[0]} to {TS[1]}')

        else:
            speak('You have these upcoming events')
            for e in events:
                DT = e[0].split('T')
                TS = DT[1].split('+')
                speak(f'{e[1]} at {TS[0]} to {TS[1]} on {DT[0]}')


def weather_details(q):
    ui.lbl.cancelloop()
    ui.lbl.next_frame(365, 444)

    city = 'sriharikota'
    if 'in' in q:
        index = q.find('in')
        q = q.replace('in', '')
        city = q[index:].strip()
    wd = weatherApi.get_current_weather(city)

    print("\n atmospheric pressure (in hPa unit) = " +
          wd['CP'] +
          "\n humidity (in percentage) = " +
          wd['CH'] +
          "\n wind Speed (in kmph) = " +
          wd['ws'])
    speak('Weather looks like ' +
          wd['desp'] + ' and current Temperature at ' + wd['CT'] + ' in ' + wd['name'])


def health_care():
    speak("Take care of your self")


def show_news():
    # shows top news
    ui.lbl.cancelloop()
    ui.lbl.next_frame(365, 444)
    news = send_top_news()
    speak('Reading Top News!')
    l = []
    nl = '\n'
    Article = random.choices(news, k=5)
    for i in range(5):
        #  produced duplicates
        # print("Title :")
        nl += "News " + str(i+1) + " » " + Article[i]['title'] + '\n'
        l.append(Article[i]['url'])
    speak(nl)
    speak('let me show news pages')
    for i in l:
        webbrowser.open_new_tab(i)


def reminder_setter(query):
    remindrDesp, remTime = remindr.find_time_desp(query)
    if remTime == 0:
        speak("cant set reminder ,Try Again!!")
        return
    remindr.remainder_init(remindrDesp, remTime)


def bored_function():
    # Function to perform Bore actions!!

    bored_list = {"code": "Practice Coding Boss", "youtube": "Enjoy Watching!!",
                  "nil": "Not sure,How to help At the moment", "game": "Try playing Games!!"}

    speak("Let me Try find something")
    from myscripts.bored_user import bored_run
    x = bored_run()
    if x == 'news':
        show_news()
    elif x == 'joke':
        speak('Let me Tell you a joke')
        from myscripts.bored_user import tell_joke
        j, p = tell_joke()
        speak(j)
        speak(p)
        speak("Haha, oh god That was Funny!")
    elif x == 'nil':
        speak('Not sure,How to help At the moment')
    else:
        speak(bored_list[x])


def Authenticate_User():
    ui.lbl.cancelloop()
    ui.lbl.next_frame(365, 444)
    speak("Initiating.. Authentication Sequence..Stare The Camera!")
    user = Face_Recognizer_Friday()
    os.system('cls')
    if user:
        Art_Friday()
        WishMe()
    else:
        speak("Unable To Recognize.. Failed To access FRIDAY AI !!")
        exit()


# <===========AUTO CHECK TASKS =============>
@su.tl.job(interval=su.timedelta(seconds=600))
def auto_check_tasks():
    # Battery Monitor
    battStatus = su.battery_check()
    if battStatus != None:
        Engine.say(battStatus)
        print(f"Warning:  {battStatus}")


def initialize_autoCheckTasks():
    su.tl.start()


# <==================== END--AUTOCHECK====================>
# for Waking ai
WAKE_KEY = 'friday'


# ? ======================== THE MAIN PROGRAM ==============================?

# if __name__ == "__main__":
def main():
    global error_count
    # Authenticate_User()
    # Art_Friday()  # UnComment if your are not using athenticate Bruh..
    WishMe()
    speak("Friday at your service...")
    # initialize_autoCheckTasks() # <<<<< For threads to check some actions
    # speak('let me check your schedule today')
    # calendar_events_google(datetime.date.today())
    wakeflag = 1
    wake = ''

    while True:

        if error_count > 3:
            error_count = 0
            wakeflag = 0
            speak('Going Standby mode!')
            ui.lbl.cancelloop()
            ui.lbl.next_frame(240, 325)
        if wakeflag == 0:
            wake = Wake_listening().lower()

            # print(wake)

            if "errorfoundinlistening" in wake:
                speak("Sorry.... Cant help you at the Moment.... Try again later")
                print("Try again later")
                exit()

        if (wakeflag == 1) or (wake.count(WAKE_KEY) > 0):
            if (wake.count(WAKE_KEY) > 0):
                speak('yes boss')
                wakeflag = 1
                wake = ''

            query = TakeCommand().lower()

            if "errorfoundinlistening" in query:
                speak("Sorry.... Cant help you at the Moment.... Try again later")
                print("try again later")
                break
            # makes note for you
            elif query in make_note_list:
                speak('what should i write ?')
                text = TakeCommand()
                if text != 'errorfoundinlistening':
                    note_file(text)
                speak("Done")

            elif any(list(map(lambda x: x in query, weather_list))):
                weather_details(query)
            elif 'remind me' in query:
                reminder_setter(query)

            elif is_valid_calendarTask(calender_ask_list, query):
                speak('let me check..')
                # initiating calender google api
                s = calenderGoogle.authenticate_google()
                if calender_ask_list[0] in query or calender_ask_list[1] in query:
                    d = datetime.date.today()
                    e = calenderGoogle.get_events(d, s)
                    read_calendar_events(e, d)
                elif calender_ask_list[2] in query or calender_ask_list[3] in query or calender_ask_list[10] in query:
                    e = calenderGoogle.get_upcoming_events(s)
                    read_calendar_events(e)
                elif 'when do i have' in query or 'when is my' in query:
                    query = query.replace('when do i have', '').replace(
                        'when is', '').replace('my', '').strip().lower()
                    if query != '':
                        e = calenderGoogle.get_upcoming_events(s)
                        check_calendar(e, query)
                    else:
                        speak('What? Try again')
                        continue
                elif 'in' in query:
                    # write code for month retrival
                    q = query.split('in')[1].strip()
                    date = calenderGoogle.get_date_fromText(q)
                    e = calenderGoogle.get_upcoming_events_month(date, s)
                    read_calendar_events(e)

                else:
                    calendar_events_google(query, s)

            elif "type" in query and query.replace("type", '') != '':
                q = query.replace("type", '', 1).strip()
                vc.VoiceType(q)

            elif any(list(map(lambda x: x in query, ["take screenshot", "capture screen",  "capture screen"]))):
                vc.TakeScreenShot()

            elif 'play music' in query:
                music_dir = 'C:\\Users\\siva reddy\\Music'
                songs = os.listdir(music_dir)
                r = random.randint(0, len(songs)-1)
                while True:
                    if songs[r][-3:] != 'mp3':
                        r += 1
                        continue
                    else:
                        break
                os.startfile(os.path.join(music_dir, songs[r]))
                speak('Enjoy your music')

            elif ("music" in query or "song" in query) and "wmplayer.exe" in su.processes_running_status():
                q = query.replace("music", '', 1).replace("song", '', 1)
                vc.playerCtrl(q)

            elif ("page" in query or "tab" in query) and "chrome.exe" in su.processes_running_status():
                q = query.replace("page", '', 1).replace("browser", '', 1)
                print(q)
                vc.chromeCtrl(q)

            elif query in Standby_Triggers:
                speak("Alright, Friday at your service,All systems Online!")
                ui.lbl.cancelloop()
                ui.lbl.next_frame(240, 325)
                wakeflag = 0

            elif is_valid_note(open_launch_list, query):
                if query.replace('open', '').replace('launch', '') == '':
                    speak('What should i open')
                    q = TakeCommand().lower().strip()
                    if 'nothing' in query:
                        continue
                    query = 'open ' + str(q.strip())
                if is_valid_note(site_list, query):
                    key = query.strip().split(' ')[1]
                    speak("Sure, Opening %s" % (key))
                    webbrowser.open_new_tab(site_list[key])
                elif is_valid_note(common_apps, query):
                    key = query.split(' ')[1].strip()
                    speak('Aye aye Boss')
                    os.startfile(common_apps[key])
                else:

                    speak('sure, {} opened'.format(
                        query.replace('open', '').replace('launch', '')))
                    os.system('explorer C:\\"{}"'.format(
                        query.replace('open', '').replace('launch', '').strip()))
                continue

            elif query in Shutdown:
                if time > 22:
                    speak("Good night Boss")
                else:
                    speak("Bye Boss have a good Day")
                ui.root.destroy()
                sys.exit()
            elif 'lock pc' in query or 'lock system' in query or 'lock windows' in query:
                speak('Sure, Locking pc')
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown pc' in query or 'shutdown system' in query or 'shutdown windows' in query:
                speak('Sure, Turning off Pc')
                os.system('shutdown /s /t 3')
                exit()

            elif 'wikipedia' in query:
                query = query.replace('wikipedia', '')
                knowAbout(query, 'wkp')

            elif is_valid_Search(query) and "you" not in query and "doing" not in query:
                q = query.replace(query.split(' ')[0], '', 1)
                if 'is' in query or 'are' in query:
                    try:
                        # Split at first speace to get keyword
                        q = q.strip().split(' ', 1)[1]
                    except:
                        speak("try again")
                        continue
                else:
                    speak("Please Try again!!")
                    continue
                knowAbout(q, 'gnl')

            elif 'search' in query or is_valid_googleSearch(query):
                if 'search' in query and query.find('search') == 0:
                    query = query.replace('search', '', 1)
                speak('Here is what i found...')
                googleSearch(query)

            elif 'send email' in query or 'send message' in query or 'send mail' in query:
                SendingMailPrompts(query)
            elif 'read mail' in query or 'check mails' in query:
                read_mails_from_gmail()

            else:
                if query != '':
                    # DEEP LEARNING AI MODEL INTENT PREDICTION
                    # Getiing response from Deep learned Model
                    resp, intent = Respond_To_Command(query)
                    if intent == 'Unknown':                  # no intent Matched
                        speak(resp)
                        speak('Do you want to know?')
                        if user_prompt_yes_no():
                            knowAbout(query, 'gnl')
                        else:
                            continue
                    elif intent == "health_care":  # HEALTH INTENT
                        health_care()
                    elif intent == "bored_user":
                        bored_function()

                    elif intent == "news_request":
                        speak("Let me Get Some News!")
                        show_news()
                    elif intent == "battery_status_details":
                        speak(su.battery_status())
                    elif intent == "reminder_alert":
                        reminder_setter(query)

                    else:
                        speak(resp)
                else:
                    continue


# MultiThread Non Blocking

threading.Thread(target=main, daemon=False).start()
ui.runUi()
