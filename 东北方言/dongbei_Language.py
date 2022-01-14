'''
将查询到的东北方言进行朗读
使用TTS语音引擎
'''


import winsound
import win32com
from win32com.client import Dispatch,constants

#初始化字典
speak_out = win32com.client.Dispatch('sapi.spvoice')
lang = {"埋汰":"脏","卡了":"摔倒，栽跟头了","磕碜":"难看","嘎哈":"有什么事","上该里溜达":"上街上，到处闲逛","唠嗑":"谈话，聊天","稀罕":"喜欢","白唬":"瞎说，不着边际"}

# 按照字典值，定时顺序输出东北方言的函数view（），间隔为1秒

def view():
    for key,value in lang.items():
        # 按照字典输出方言
        print(key,":",value)
        # 朗读方言
        speak(key+"    "+value)

def speak(str):
    # 读方言
    speak_out.speak(str)
    # 输出结束语
    winsound.PlaySound(str,winsound.SND_ASYNC)

print("   东北方言\n")
print("说明： 输入“q”退出；输入“s”按照顺序输出并朗读内容。")
while True:
    word = input("请输入要查找的东北方言：").strip()
    if word.lower() == 'q':
        break
    #遍历方言
    if word.lower() == 's':
        view()
    else:
        # 如果指定键的值不存在时，返回该默认值
        note = lang.get(word,"no")
        print(note)
        # 查找输入的方言，朗读并且解释
        if note != "no":
            print(word,":",note)
            speak(word + ":   "+note)
        else:
            print("没有检索到东北方言！")