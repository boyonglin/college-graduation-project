import speech_recognition as sr
import webbrowser as wb
import os, sys
import winsound
import re, requests
from bs4 import BeautifulSoup
import pyautogui
import win32gui, win32api
import win32com.client, win32clipboard
import requests.packages.urllib3
import globals
import tkinter as tk
import threading
import excel
import time
import test_speaker_realtime

window = tk.Tk()
window.iconbitmap('voice_square.ico')
window.attributes('-topmost', True)
window.title('Welcome to Sound Genie')
window.geometry('450x300')

requests.packages.urllib3.disable_warnings()
wscript = win32com.client.Dispatch("WScript.Shell")
pyautogui.FAILSAFE=False
r = sr.Recognizer()

canvas = tk.Canvas(window, height=324, width=240)
image_file = tk.PhotoImage(file='AI.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='left')

text = tk.Text(window, width=26, height=1, font=("italic",13))
text.place(x=220, y=120)
text.insert('end', '你可以說"指令"來查詢功能')

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True) #守護線程
    t.start()


def youtube():
    text.delete(1.0, 'end')
    text.insert('end', '您想搜尋什麼?')
    image_file = tk.PhotoImage(file='AI.gif')
    image = canvas.create_image(0,0, anchor='nw', image=image_file)
    winsound.PlaySound("audio/search.wav", winsound.SND_FILENAME)
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            speak = r.recognize_google(audio,language='zh-TW')
            print('您所說的話: ' + speak)
            text.delete(1.0, 'end')
            text.insert('end', '您所說的話: ' + speak)
        if '離開' in speak:
            pyautogui.hotkey('ctrl', 'w')
            return
        else:
            #這裡搜尋所講的話 並且可以選擇要挑哪個網址開啟
            url_yt="https://www.youtube.com/results?search_query=" + speak
            wb.open(url_yt)
            winsound.PlaySound("audio/mission.wav", winsound.SND_FILENAME)

            # 這邊把搜尋到的結果網址一個一個揪出來
            res = requests.get(url_yt, verify=False)
            soup = BeautifulSoup(res.text, 'html.parser')
            last = None

            myList = []
            for entry in soup.select('a'):  # soup.select('a')得到了很多條網址字串  for每個字串一個一個處理
                m = re.search("v=(.*)", entry['href'])  # 網址篩選條件
                if m:
                    target = m.group(1)  # 這邊引進得到的網址字串
                    if target == last:
                        continue
                    if re.search("list", target):
                        continue
                    last = target
                    myList.append(target)
                    #print(target)

            def yt_film():
                try:
                    text.delete(1.0, 'end')
                    text.insert('end', '請選擇第一部到第五部影片')
                    image_file = tk.PhotoImage(file='AI.gif')
                    image = canvas.create_image(0,0, anchor='nw', image=image_file)
                    winsound.PlaySound("audio/choose.wav", winsound.SND_FILENAME)
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=10, phrase_time_limit=5)
                        choose = r.recognize_google(audio, language='zh-TW')
                        print('您所說的話: ' + choose)
                        text.delete(1.0, 'end')
                        text.insert('end', '您所說的話: ' + choose)
                        if '一' in choose:
                            wb.open("https://www.youtube.com/watch?v=" + myList[0])
                            text.delete(1.0, 'end')
                            text.insert('end', '第一部影片已開啟')

                        elif '二' in choose:
                            wb.open("https://www.youtube.com/watch?v=" + myList[1])
                            text.delete(1.0, 'end')
                            text.insert('end', '第二部影片已開啟')

                        elif '三' in choose:
                            wb.open("https://www.youtube.com/watch?v=" + myList[2])
                            text.delete(1.0, 'end')
                            text.insert('end', '第三部影片已開啟')

                        elif '四' in choose:
                            wb.open("https://www.youtube.com/watch?v=" + myList[3])
                            text.delete(1.0, 'end')
                            text.insert('end', '第四部影片已開啟')

                        elif '五' in choose:
                            wb.open("https://www.youtube.com/watch?v=" + myList[4])
                            text.delete(1.0, 'end')
                            text.insert('end', '第五部影片已開啟')

                        elif '重新' in choose:
                            pyautogui.hotkey('ctrl', 'w')
                            youtube()
                        elif '離開' in choose:
                            pyautogui.hotkey('ctrl', 'w')
                            return
                        else:
                            print("Sorry, I didn't catch you.")
                            image_file = tk.PhotoImage(file='AI_no.gif')
                            image = canvas.create_image(0,0, anchor='nw', image=image_file)
                            winsound.PlaySound("audio/again.wav", winsound.SND_FILENAME)
                            yt_film()
                except:
                    print("Sorry, I didn't catch you.")
                    image_file = tk.PhotoImage(file='AI_no.gif')
                    image = canvas.create_image(0,0, anchor='nw', image=image_file)
                    winsound.PlaySound("audio/again.wav", winsound.SND_FILENAME)
                    yt_film()

            yt_film()

    except:
        print("Sorry, I didn't catch you.")
        image_file = tk.PhotoImage(file='AI_no.gif')
        image = canvas.create_image(0,0, anchor='nw', image=image_file)
        winsound.PlaySound("audio/again.wav", winsound.SND_FILENAME)
        youtube()

def google():
    text.delete(1.0, 'end')
    text.insert('end', '您想搜尋什麼?')
    image_file = tk.PhotoImage(file='AI.gif')
    image = canvas.create_image(0,0, anchor='nw', image=image_file)
    winsound.PlaySound("audio/search.wav", winsound.SND_FILENAME)
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            speak = r.recognize_google(audio,language='zh-TW')
            print('您所說的話: ' + speak)
            text.delete(1.0, 'end')
            text.insert('end', '您所說的話: ' + speak)
        if '離開' in speak:
            pyautogui.hotkey('ctrl', 'w')
            return
        else:
            url_yt="https://www.google.com/search?q=" + speak
            wb.open(url_yt)
            text.delete(1.0, 'end')
            text.insert('end', '已為您搜尋"' + speak + '"')
            winsound.PlaySound("audio/mission.wav", winsound.SND_FILENAME)
            
    except:
        print("Sorry, I didn't catch you.")
        image_file = tk.PhotoImage(file='AI_no.gif')
        image = canvas.create_image(0,0, anchor='nw', image=image_file)
        winsound.PlaySound("audio/again.wav", winsound.SND_FILENAME)
        youtube()

def calc():
    wscript.Run("calc")
    win32api.Sleep(500)
    win = win32gui.FindWindow(None, "小算盤")
    win32api.Sleep(500)
    win32gui.SetForegroundWindow(win)

def close():
    browserExe = "chrome.exe"
    os.system("taskkill /f /im " + browserExe)
    print("Chrome已經關閉。")

globals.initialize()
count=1
instruction=0
def main():
    global instruction
    global count
    winsound.PlaySound("audio/win7.wav", winsound.SND_FILENAME)
    winsound.PlaySound("audio/welcome.wav", winsound.SND_FILENAME)
    winsound.PlaySound("audio/query.wav", winsound.SND_FILENAME)
    while globals.var == 1:  # 此條件永遠true，將無限循環行下去  可以使用 CTRL+C 來中斷。
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("I'm listening...")
                if count>=4:
                    image_file = tk.PhotoImage(file='AI_no.gif')
                    image = canvas.create_image(0,0, anchor='nw', image=image_file)
                else:
                    text.delete(1.0, 'end')
                    text.insert('end', "I'm listening...")
                    image_file = tk.PhotoImage(file='AI.gif')
                    image = canvas.create_image(0,0, anchor='nw', image=image_file)
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=20,phrase_time_limit=3)
                with open("speaker.wav", "wb") as f: 
                    f.write(audio.get_wav_data(convert_rate=16000))
                    
            data = r.recognize_google(audio, language='zh-TW')
            print('您所說的話: ' + data)
            text.delete(1.0, 'end')
            text.insert('end', '您所說的話: ' + data)
            source = "C:\\Users\\USER\\GUI_SpeakerID\\speaker.wav"
            test_speaker_realtime.test_speaker_realtime(source)
            #print("\tdetected as -", globals.speaker_realtime)
            if globals.speaker_realtime == globals.speaker_call:
                print("User is correct.")
                count=1
                if '播放' in data or '暫停' in data:
                    pyautogui.typewrite(['space'])
                    winsound.PlaySound("audio/dong.wav", winsound.SND_FILENAME)
                elif '上' in data:
                    pyautogui.hotkey('alt', 'left')
                elif '下' in data:
                    pyautogui.hotkey('alt', 'right')
                elif '大' in data:
                    pyautogui.typewrite(['volumeup'])
                    winsound.PlaySound("audio/dong.wav", winsound.SND_FILENAME)
                elif '小' in data:
                    pyautogui.typewrite(['volumedown'])
                    winsound.PlaySound("audio/dong.wav", winsound.SND_FILENAME)
                elif 'Google' in data or '搜尋' in data:
                    wb.open('https://www.google.com.tw/')
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟Google')
                    google()
                elif 'Facebook' in data:
                    wb.open('https://www.facebook.com/')
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟Facebook')
                elif 'portal' in data:
                    wb.open('https://portal.ncu.edu.tw/')
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟Portal')
                elif '翻譯' in data or '翻' in data:
                    wb.open('https://translate.google.com.tw/?hl=zh-TW')
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟Google翻譯')
                elif 'YouTube' in data:
                    wb.open("https://www.youtube.com/?gl=TW&hl=zh-TW")
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟YouTube')
                    youtube()
                elif '計算機' in data or '小算盤' in data:
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟windows小算盤')
                    calc()
                elif '指令' in data or 'instruction' in data:
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您開啟指令集')
                    excel.popen2()
                    instruction=1
                elif '關掉' in data or '關閉' in data:
                    pyautogui.hotkey('ctrl', 'w')
                    text.delete(1.0, 'end')
                    text.insert('end', '已為您關閉目前分頁')
                elif '結束' in data:
                    if instruction==1:
                        globals.var = 0
                        excel.pclose()
                        window.destroy()
                        print('Program is closed.')
                        sys.exit(0)
                    else:
                        globals.var = 0
                        window.destroy()
                        print('Program is closed.')
                        sys.exit(0)
                
            else:
                print("Sorry, User is wrong.")
                text.delete(1.0, 'end')
                text.insert('end', "Sorry, User is wrong.")

        except sr.UnknownValueError:
            print("Sorry, I didn't catch you.")
            count=count+1
            if count>=4:
                text.delete(1.0, 'end')
                text.insert('end', 'Hummm?')
                image_file = tk.PhotoImage(file='AI_no.gif')
                image = canvas.create_image(0,0, anchor='nw', image=image_file)
            else:
                pass
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except:
            pass

thread_it(main)

from IPython.display import display_html
def restartkernel():
    window.destroy()
    display_html("<script>Jupyter.notebook.kernel.restart()</script>",raw=True)

window.wm_protocol('WM_DELETE_WINDOW', restartkernel)

window.mainloop()