import psutil
import pyautogui
import time
import os
import pygetwindow._pygetwindow_win as gw  # for checking active window apps.
# THIS MODULE IS RELATED TO AUTOMATION OF APPLICATIONS USING SHORTCUTS AND UI CONTROLS


chrome = None
wmplayer = None


def check_running_apps():
    global chrome
    global wmplayer
    for i in gw.getAllTitles():
        if "Google Chrome" in i:
            chrome = i
    for i in gw.getAllTitles():
        if "Windows Media Player" in i:
            wmplayer = i


def activate_window(appName):
    # Activates the Minimized window
    try:
        Window = gw.getWindowsWithTitle(appName)[0]
        Window.restore()
        # Window.maximize()
        Window.activate()
    except:
        print('Error Occured.')

    return Window


def playerCtrl(cmd):
    check_running_apps()
    w = activate_window(wmplayer)
    if any(list(map(lambda x: x in cmd, ["play", "start",  "sound"]))):
        pyautogui.hotkey("ctrl", "p")
    if any(list(map(lambda x: x in cmd, ['pause', 'silent', 'stop']))):
        pyautogui.hotkey("ctrl", "s")
    elif any(list(map(lambda x: x in cmd, ["volume up", "raise volume", "increse volume", "play louder"]))):
        pyautogui.hotkey("f9")
    elif any(list(map(lambda x: x in cmd, ["volume down", "reduce volume", "decrease volume", "lower volume"]))):
        pyautogui.hotkey("f8")
    elif any(list(map(lambda x: x in cmd, ["mute", "halt", "silent", "unmute"]))):
        pyautogui.hotkey("f7")
    elif any(list(map(lambda x: x in cmd, ["next", "another"]))):
        pyautogui.hotkey("Ctrl", "f")
    elif any(list(map(lambda x: x in cmd, ["previous", "last"]))):
        pyautogui.hotkey("Ctrl", "b")
    elif any(list(map(lambda x: x in cmd, ["close player", "quit music player"]))):
        w.close()


def commonCtrl(cmd):
    if "copy" in cmd:
        pyautogui.hotkey("ctrl", "c")
    elif "paste" in cmd:
        pyautogui.hotkey("ctrl", "v")
    elif "select all" in cmd:
        pyautogui.hotkey("ctrl", "a")
    elif "rename" in cmd:
        pyautogui.hotkey("f2")
    elif "rename" in cmd:
        pyautogui.hotkey("Enter")
    elif "close app" in cmd:
        pyautogui.hotkey("alt", "f4")


def chromeCtrl(cmd):
    check_running_apps()
    if chrome == None:
        return
    activate_window(chrome)

    if "new tab" in cmd:
        pyautogui.hotkey("ctrl", "t")
    elif "next tab" in cmd:
        pyautogui.hotkey("ctrl", "tab")
    elif "previous tab" in cmd:
        pyautogui.hotkey("ctrl", "shift", "tab")
    elif "previous" in cmd:
        pyautogui.hotkey("Alt", "left")
    elif "next" in cmd:
        pyautogui.hotkey("Alt", "right")
    elif "show history" in cmd or "history" in cmd:
        pyautogui.hotkey("ctrl", "h")
    elif "show download" in cmd or "downloads" in cmd:
        pyautogui.hotkey("ctrl", "j")
    elif "close tab" in cmd:
        pyautogui.hotkey("ctrl", "w")
    elif "move down" in cmd or "scroll down" in cmd:
        pyautogui.press("space")
        # print("scroll")
    elif "close Chrome" in cmd or "quit Chrome":
        pyautogui.hotkey("alt", "f")
        pyautogui.press('x')
    else:
        pyautogui.press("space")


def TakeScreenShot():
    path = "C:\\Users\\siva reddy\\Pictures\\Screenshots\\ScreenShot{}.png".format(
        str(time.time()))
    pyautogui.screenshot(path)
    os.startfile(path)


# Types Anything Spoke
def VoiceType(text):
    pyautogui.typewrite(text, interval=0.1)
