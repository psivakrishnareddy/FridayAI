from tkinter import *
# from mttkinter import *
from PIL import Image, ImageTk
from itertools import count
import threading
from tkthread import tk, TkThread
import sys
lstart = 0
lend = 444
# def setSe(l , e):
#     lstart  = l
    
def setUserText(comp):
    userText.set(comp)


def setCompText(text):
    compText.set(text)


class ImageLabel(Label):
    """a label that displays images, and plays them if they are gifs"""
    global lstart
    global lend
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
            # self.delay = 500

        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            # self.config(image=self.frames[30])
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

   
    def cancelloop(self):
        self.after_cancel(self.cancel)
        lstart = 0 
        lend = 444

    def next_frame(self , l=None , e = 444):
        global lstart
        global lend
        if(l != None):
            self.loc = l
            lstart = l
            lend = e
        # print(self.loc)
        if(self.loc == lend):
            self.loc = lstart if lstart != 0 else 0
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            # if self.loc == lend:
            #     self.next_frame(lstart, lend)
            # else:
            self.cancel = self.after(self.delay, self.next_frame)


root = tk.Tk()
# root = Tk()

tkt = TkThread(root)

root.title('FRIDAY MARK 3')
root.config(background='Red')
root.geometry('1200x450')
root.resizable(100, 0)
# root.iconbitmap(r'C:\Users\skt\Documents\Karen Mark I\Untitled-1.ico')
# img = ImageTk.PhotoImage(Image.open(
#     r"C:\Users\siva reddy\Desktop\FRIDAY\UI\preview.gif"))
compText = StringVar()
userText = StringVar()


compText.set('Initializing please Wait..')
userText.set('Your Commands Here')

lbl = ImageLabel(root)
lbl.load('../circle_story_by_gleb.gif')
lbl.pack(side="left", fill="both", expand="no")

userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
userFrame.pack(fill="both", expand="yes")

left2 = Message(userFrame, textvariable=userText, bg='gray20', fg='white')
left2.config(font=("Comic Sans MS", 8, 'bold'))
left2.pack(side="right",fill='both', expand=True)

compFrame = LabelFrame(root, text="FRIDAY", font=('Black ops one', 10, 'bold'))
compFrame.pack(fill="both", expand="yes")
left1 = Message(compFrame, textvariable=compText,
                bg='Springgreen2', fg='white')
left1.config(font=("Comic Sans MS", 8, 'bold') )
left1.pack(side="bottom",fill='both', expand=True)
# left1.place(x=40 , y =50)
def closeall():
    sys.exit()
    root.destroy()
# btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'),
#              bg='deepSkyBlue', fg='white', command=clicked).pack(fill='x', expand='no')
btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'),
              bg='powderBlue', fg='Black', command=closeall).pack(side="bottom",fill='x', expand='no')

    


def runUi():
    root.mainloop()
# runUi()
