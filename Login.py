import speech_recognition as sr
import numpy as np
import threading
import winsound
import pickle,time
import wave,os
from scipy.io import wavfile
from scipy.fftpack import dct
from tkinter import messagebox
from tkinter import StringVar
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import librosa.display,librosa
import test_speaker
import record_audio
import train_models
import globals
import excel

def voice():
    excel.popen1()
    globals.initialize()
    import PyAutoGUI
    winsound.PlaySound(\"audio/vcmode.wav\", winsound.SND_FILENAME)
    while globals.var==1:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print(\"Speak:\")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=10,phrase_time_limit=3)

            data = r.recognize_google(audio, language='zh-TW')
            print(\"您所說的話: \" + data )

            def listen():
                try:
                   with sr.Microphone() as source:
                        print(\"請說出您的帳戶名稱:\")
                        winsound.PlaySound(\"audio/username.wav\", winsound.SND_FILENAME)
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=20, phrase_time_limit=3)
                        speak = r.recognize_google(audio,language='zh-EN')
                        print(\"User name: \" + speak)
                        PyAutoGUI.write(speak)
                        winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
                except:
                    return listen()

            if '註冊' in data:
                PyAutoGUI.sign_up()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '錄音' in data:
                PyAutoGUI.record()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '開始' in data:
                PyAutoGUI.recording()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '波形' in data:
                PyAutoGUI.wave()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '關閉' in data:
                PyAutoGUI.close()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '寫入' in data:
                PyAutoGUI.insert()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '結束' in data:
                PyAutoGUI.record_finish()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '訓練' in data:
                PyAutoGUI.train()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '完成' in data:
                PyAutoGUI.sign_finish()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '驗證' in data:
                PyAutoGUI.user_ver()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '登入' in data:
                globals.var==0
                PyAutoGUI.log_in()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
                excel.pclose()
            elif '確定' in data:
                PyAutoGUI.confirm()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
            elif '使用者' in data:
                PyAutoGUI.user_name()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
                listen()
            elif '帳號' in data:
                PyAutoGUI.account()
                winsound.PlaySound(\"audio/dong.wav\", winsound.SND_FILENAME)
                listen()

        except sr.UnknownValueError:
                print(\"Could not understand audio\")

        except sr.RequestError as e:
            print(\"Could not request results; {0}\".format(e))

        except:
            pass

window = tk.Tk()
window.iconbitmap('voice_square.ico')
window.attributes('-topmost', True)
window.title(\"Welcome to Voice ID system\")
window.geometry(\"450x300\")

from IPython.display import display_html
def restartkernel():
    window.destroy()
    display_html(\"<script>Jupyter.notebook.kernel.restart()</script>\",raw=True)
window.wm_protocol('WM_DELETE_WINDOW', restartkernel)

# welcome image
canvas = tk.Canvas(window, height=200, width=450)
image_file = tk.PhotoImage(file=\"welcome.gif\")
image = canvas.create_image(0, 0, anchor=\"nw\", image=image_file)
canvas.pack(side=\"top\")

# user information
tk.Label(window, text=\"  Account : \").place(x=50, y= 160)
tk.Label(window, text=\"Password : \").place(x=50, y= 200)

var_usr_name = tk.StringVar()
var_usr_name.set(\"User_name\")
entry_usr_name = tk.Entry(window, width=25, textvariable=var_usr_name)
entry_usr_name.place(x=135, y=160)

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True) # 守護線程
    t.start()

def verify_record():
    usr_name = var_usr_name.get()
    vornot = \"C:\\\\Users\\\\USER\\\\GUI_SpeakerID\\\\development_set\\\\\"+usr_name+\"_verify.wav\"
    if os.path.exists(vornot):
        os.remove(vornot)
    else:
        pass
    thread_it(mprogress)
    record_audio.record_audio(vornot, record_second=4)
    ft = open(\"voice_list_test.txt\", \"w\")
    ft.write(usr_name+\"_verify.wav\"+\"\\n\")
    # ft.close()

def mprogress():
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill=\"green\")
    x = 200
    n = 178/x
    for i in range(x):
        n = n+178/x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0.02)

    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill=\"white\")
    x = 200
    n = 178/x

    for t in range(x):
        n = n+178/x
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        time.sleep(0)

canvas = tk.Canvas(window, width=178, height=3, bg=\"white\")
canvas.place(x=133, y=221)

def usr_log_in():
    globals.call()
    usr_name = var_usr_name.get()
    globals.speaker_call = var_usr_name.get()
    vornot = \"C:\\\\Users\\\\USER\\\\GUI_SpeakerID\\\\development_set\\\\\"+usr_name+\"_verify.wav\"
    if not os.path.isfile(vornot):
        tk.messagebox.showerror(\"Error\", \"Error, Please verify your voice first.\")
    else:
        test_speaker.test_speaker()
        os.remove(vornot)
        with open(\"usrs_info.pickle\", \"rb\") as usr_file:
            usrs_info = pickle.load(usr_file)
        if usr_name in usrs_info:
            if globals.speaker == usr_name:
                globals.var=0
                tk.messagebox.showinfo(title=\"Welcome\", message=\"How are you ? \" + usr_name)
                window.destroy()
                import voice_instruction
                voice_instruction
            else:
                tk.messagebox.showerror(\"Error\", \"Error, Your password is wrong, try again.\")
        else:
            is_sign_up = tk.messagebox.askyesno(\"Welcome\", 
                                   \"You have not signed up yet. Sign up today?\")
            if is_sign_up:
                usr_sign_up()

def usr_sign_up():
    globals.initialize()
    try:
        with open(\"usrs_info.pickle\", \"rb\") as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open(\"usrs_info.pickle\", \"wb\") as usr_file:
            usrs_info = {\"admin\": \"admin\"}
            pickle.dump(usrs_info, usr_file)
    def sign_to_voice_identification():
        nn = new_name.get()
        fileName = \"C:\\\\Users\\\\USER\\\\GUI_SpeakerID\\\\speaker_models\\\\\"+nn+\".gmm\"
        with open(\"usrs_info.pickle\", \"rb\") as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if nn in exist_usr_info:
            tk.messagebox.showerror(\"Error\", \"The user has already signed up!\")
        elif not os.path.isfile(fileName):
            tk.messagebox.showerror(\"Error\", \"Please record and train first!\")
        else:
            exist_usr_info[nn] = nn+\".gmm\"
            with open(\"usrs_info.pickle\", \"wb\") as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(\"Welcome\", \"You have successfully signed up!\")
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.iconbitmap('voice_square.ico')
    window_sign_up.attributes('-topmost', True)
    window_sign_up.geometry(\"330x180\")
    window_sign_up.title(\"Sign up window\")

    def usr_record():
        window_record = tk.Toplevel(window)
        window_record.iconbitmap('voice_square.ico')
        window_record.attributes('-topmost', True)
        window_record.geometry(\"380x290\")
        window_record.title(\"Record voice window\")
        text = tk.Text(window_record, width=24, height=1,  font=(\"italic\", 10))
        text.place(x=170, y=95)

        nn = new_name.get()
        f = open(\"voice_list_enroll.txt\", \"w\")
        text.insert(\"end\", \"請針對斜體字進行錄音\")
        excel.popen2()

        def start_record():
            file_dir = \"C:\\\\Users\\\\USER\\\\GUI_SpeakerID\\\\development_set\"
            file_name = nn+\"_0\"+str(globals.n)+\".wav\"
            file_abs = os.path.join(file_dir, file_name)

            if os.path.exists(file_abs):
                text.delete(1.0, \"end\")
                text.insert(\"end\", \"* ERROR\")
                return
            else:
                thread_it(progress)
                text.delete(1.0, \"end\")
                text.insert(\"end\", \"* recording\")
                record_audio.record_audio(file_abs, record_second=4)

        def insert():
            f = open(\"voice_list_enroll.txt\", \"a\")
            f.write(text.get(1.0, \"end\"))
            list_voice.insert(\"end\", text.get(1.0, \"end\"))
            text.delete(1.0, \"end\")

        def Graph():
            window_Graph = tk.Toplevel(window)
            window_Graph.iconbitmap('voice_square.ico')
            window_Graph.attributes('-topmost', True)
            window_Graph.geometry(\"502x632\")
            window_Graph.title(\"Waveform observation\")

            fig = plt.figure(figsize=(7, 6))
            ax1 = fig.add_subplot(311)
            ax2 = fig.add_subplot(312)
            ax3 = fig.add_subplot(313)
            plt.subplots_adjust(wspace =0, hspace =0.5) # 調整子圖間距

            canvas = FigureCanvasTkAgg(fig, master=window_Graph)
            canvas.get_tk_widget().grid(ipady=100)

            file_dir = \"C:\\\\Users\\\\USER\\\\GUI_SpeakerID\\\\development_set\"
            file_name = nn+\"_0\"+str(globals.n-1)+\".wav\"
            file_abs = os.path.join(file_dir, file_name)

            ### 繪製語音波形
            def plot_time(signal, sample_rate):
                time = np.arange(0, len(signal)) * (1.0 / sample_rate)
                ax1.plot(time, signal)
                ax1.set_xlabel('Time(s)')
                ax1.set_ylabel('Amplitude')
                ax1.set_title(\"Original wave\")
                ax1.grid()

            sample_rate, signal = wavfile.read(file_abs)
            signal = signal[0: int(4 * sample_rate)]
            pre_emphasis = 0.97 # 預加重(Pre-Emphasis)
            emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
            plot_time(emphasized_signal, sample_rate)

            ### 繪製聲紋圖
            f = wave.open(file_abs, \"rb\")
            strData = f.readframes(len(signal))
            waveData = np.frombuffer(strData, dtype=np.short)
            waveData = waveData * 1.0/max(abs(waveData)) # 歸一化
            # 將音頻信號規整乘每行一路通道信號的格式，即該矩陣一行為一個通道的採樣點，共nchannels=1行
            waveData = np.reshape(waveData, [len(signal), 1]).T
            f.close()

            frame_size, frame_stride = 0.025, 0.01
            # 每幀點數 N = t*fs, 通常情況下值為256或512
            frame_length, frame_step = int(round(frame_size * sample_rate)), int(round(frame_stride * sample_rate))
            signal_length = len(emphasized_signal)
            num_frames = int(np.ceil(np.abs(signal_length - frame_length) / frame_step)) + 1

            pad_signal_length = (num_frames - 1) * frame_step + frame_length
            z = np.zeros((pad_signal_length - signal_length))
            pad_signal = np.append(emphasized_signal, z)

            indices=np.arange(0,frame_length).reshape(1,-1)+np.arange(0,num_frames*frame_step,frame_step).reshape(-1,1)
            frames = pad_signal[indices]

            hamming = np.hamming(frame_length)
            frames *= hamming
            NFFT = 512
            mag_frames = np.absolute(np.fft.rfft(frames, NFFT))
            pow_frames = ((1.0 / NFFT) * (mag_frames ** 2))
            low_freq_mel = 0
            high_freq_mel = 2595 * np.log10(1 + (sample_rate / 2) / 700)
            nfilt = 40
            # 所有的mel中心點，為了方便後面計算mel濾波器組，左右兩邊各補一個中心點
            mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  
            hz_points = 700 * (10 ** (mel_points / 2595) - 1)
            fbank = np.zeros((nfilt, int(NFFT / 2 + 1)))  # 各個mel濾波器在能量譜對應點的取值
            bin = (hz_points / (sample_rate / 2)) * (NFFT / 2)  # 各個mel濾波器中心點對應FFT的區域編碼，找到有值的位置
            for i in range(1, nfilt + 1):
                left = int(bin[i-1])
                center = int(bin[i])
                right = int(bin[i+1])
                for j in range(left, center):
                    fbank[i-1, j+1] = (j + 1 - bin[i-1]) / (bin[i] - bin[i-1])
                for j in range(center, right):
                    fbank[i-1, j+1] = (bin[i+1] - (j + 1)) / (bin[i+1] - bin[i])
            filter_banks = np.dot(pow_frames, fbank.T)
            filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)
            filter_banks = 20 * np.log10(filter_banks)  # dB


            # 找到與當前framesize最接近的2的正整數次方
            nfftdict = {}
            lists = [32, 64, 128, 256, 512, 1024]
            for i in lists:
                nfftdict[i] = abs(frame_length - i)
            sortlist = sorted(nfftdict.items(), key=lambda x: x[1]) # 按與當前frame_length差值升序排列
            frame_length = int(sortlist[0][0]) # 取最接近當前frame_length的那個2的正整數次方值為新的frame_length


            spectrum, freqs, ts, fig = ax2.specgram(waveData[0], NFFT = NFFT, Fs =sample_rate, 
                                                 window=np.hamming(M = frame_length), noverlap=frame_stride, 
                                                 mode=\"default\", scale_by_freq=True, sides=\"default\", 
                                                 scale=\"dB\", xextent=None)
            ax2.set_xlabel(\"Time(s)\")
            ax2.set_ylabel(\"Frequency(Hz)\")
            ax2.set_title(\"Spectrogram\")

            ### 繪製MFC圖形
            def plot_MFC(spec, note):
                heatmap = plt.pcolor(spec)
                plt.colorbar(mappable=heatmap)
                ax3.set_xlabel('Time(s)')
                ax3.set_ylabel(note)
                ax3.set_title(\"MFC\")
                plt.tight_layout()

            num_ceps = 12
            mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1:(num_ceps+1)]
            cep_lifter = 23 # 對MFCC進行正弦提升（sinusoidal liftering），加重高頻部分，使噪音弱化
            (nframes, ncoeff) = mfcc.shape
            n = np.arange(ncoeff)
            lift = 1 + (cep_lifter / 2) * np.sin(np.pi * n / cep_lifter)
            mfcc *= lift
            plot_MFC(mfcc.T, 'MFC Coeffs')

        def progress():
            # 填充進度條
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill=\"green\")
            x = 200  # 控制進度條時間
            n = 200/x  # 200是矩形填充滿的次數
            k = 100/x
            for i in range(x):
                n = n+200/x
                k = k+100/x
                canvas.coords(fill_line, (0, 0, n, 60))
                if k >= 100:
                    var.set(\"100%\")
                else:
                    var.set(str(round(k))+\"%\")
                window_record.update()

                window.update()
                time.sleep(0.02)  # 控制進度條流動的速度

            # 清空進度條
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill=\"white\")
            x = 200
            n = 200/x

            for t in range(x):
                n = n+200/x
                # 以矩形的長度作為變量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)  # 時間為0，即快速清空進度條

            text.delete(1.0, \"end\")
            text.insert(\"end\", nn+\"_0\"+str(globals.n)+\".wav\")
            globals.n = globals.n+1

        var = StringVar()
        var.set(\"0%\")

        canvas = tk.Canvas(window_record, width=200, height=22, bg=\"white\")
        canvas.place(x=60, y=35)

        def close():
            # f.close()
            excel.pclose()
            window_record.destroy()

        # 資料儲存為 voice_list
        voice_list = tk.StringVar()
        list_voice = tk.Listbox(window_record, width=15, height=8, listvariable=voice_list)
        list_voice.place(x=20, y=95)

        lb_progress = tk.Label(window_record, text=\"Recording progress : \")
        lb_progress.place(x=20, y=10)
        lb_list = tk.Label(window_record, text=\"Voice list : \")
        lb_list.place(x=20, y=70)
        lb_status = tk.Label(window_record, text=\"Status Bar : \")
        lb_status.place(x=170, y=70)
        lb_spectrogram = tk.Label(window_record, text=\"Spectrogram : \")
        lb_spectrogram.place(x=170, y=150)
        lb_percentage = tk.Label(window_record, textvariable = var)
        lb_percentage.place(x=20, y=35)

        btn_record = tk.Button(window_record, text=\"Start record\", command=lambda:thread_it(start_record))
        btn_record.place(x=280, y=35)
        btn_insert = tk.Button(window_record, text=\"Insert\", command=insert)
        btn_insert.place(x=53, y=240)
        btn_graph = tk.Button(window_record, width=20, text=\"Click to view\", command=Graph)
        btn_graph.place(x=170, y=180)
        btn_finish = tk.Button(window_record, width=8, text=\"Finish\", command=close)
        btn_finish.place(x=210, y=240)

    def training():
        train_models.train_models()

    new_name = tk.StringVar()
    tk.Label(window_sign_up, text=\"User name: \").place(x=20, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=140, y=10)

    tk.Label(window_sign_up, text=\"Record voice: \").place(x=20, y=50)
    btn_record_voice = tk.Button(window_sign_up, width=20, text=\"Click here to record\", command=usr_record)
    btn_record_voice.place(x=140, y=50)

    tk.Label(window_sign_up, text=\"Train model: \").place(x=20, y= 90)
    btn_train_model = tk.Button(window_sign_up, width=20, text=\"Click here to train\", command=training)
    btn_train_model.place(x=140, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text=\"Sign up\", command=sign_to_voice_identification)
    btn_comfirm_sign_up.place(x=140, y=130)

# login and sign up button
btn_login = tk.Button(window, width=10, text=\"Log in\", command=usr_log_in)
btn_login.place(x=145, y=245)
btn_sign_up = tk.Button(window, text=\"Sign up\", command=usr_sign_up)
btn_sign_up.place(x=245, y=245)
btn_mic = tk.Button(window, text=\"User verify\", width=24, command=lambda:thread_it(verify_record))
btn_mic.place(x=135, y=197)
btn_voice = tk.Button(window, text=\"VOICE\", command=lambda:thread_it(voice))
btn_voice.place(x=350, y=197)

window.mainloop()
