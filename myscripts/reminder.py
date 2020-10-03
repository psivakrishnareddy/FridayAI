import time
import keyboard
from playsound import playsound
import threading


def remainder_alarm(text, timeremind):
    print("thread running..")
    local_time = float(timeremind)
    local_time = local_time * 60
    time.sleep(local_time)
    print(text)
    print("Press Space to stop")
    while True:
        playsound("./sounds/ffact.wav")
        time.sleep(0.5)
        if keyboard.is_pressed('space'):
            break
    return


def find_time_desp(query):
    HH = 0
    MM = 0
    D = ''
    desp = query.split('about')[1].replace(
        'after', '', 1).strip().replace('  ', ' ', 1)
    # print(desp)
    for i in desp:
        if i.isdigit():
            break
        D += str(i)
    tdata = query.split()
    # print(tdata)
    try:
        hindex = tdata.index('hour')
    except ValueError:
        hindex = 0
    try:
        if query.find('minutes') >= 0:
            mindex = tdata.index('minutes')
        if query.find('minute') >= 0:
            mindex = tdata.index('minute')
    except ValueError:
        mindex = 0
    try:
        HH = int(tdata[hindex-1]) if hindex > 0 else 0
        MM = int(tdata[mindex-1]) if mindex > 0 else 0
    except:
        HH = 0
        MM = 0
    return D.strip(), int(HH) * 60 + int(MM)


def remainder_init(text, time):
    t1 = threading.Thread(target=remainder_alarm, args=(text, time))
    t1.start()


# dd, x = find_time_desp("remind me about xyz and abc after 20 minute")
# print(dd, x)
