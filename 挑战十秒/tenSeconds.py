from tkinter import *
from tkinter.messagebox import *
import time
import random
root = Tk()
rans = [0.1,0.08,0.06,0.04]
count = 0
start = False

def ten():
    global start
    global count
    num = random.choice(rans)
    fight['text'] = '停止'
    if not start:
        start = True
        while start:
            time.sleep(num)
            count += 0.2
            show['text'] = format(count,'.1f')
            show.update()
        if show['text'] == str(10.0):
            warn = showwarning(title='挑战10秒',message='挑战成功！！')
        else:
            warn = showwarning(title='挑战10秒',message='挑战失败！')
    else:
        start = False
        fight['text'] = '继续挑战'
        count = 0

root.title('挑战10秒')
root.wm_attributes('-topmost',1)
root.geometry('200x80')
root.resizable(width = True,height=True)
topic = Label(root,text = '挑战10秒')
topic.pack()
show = Label(root,text = str(count))
show.pack()
fight = Button(root,text='开始挑战',command = ten)
fight.pack()
mainloop()