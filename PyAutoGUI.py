import pyautogui

def sign_up():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/sign_up.png')))
def record():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/record.png')))
def recording():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/recording.png')))
def wave():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/wave.png')))
def close():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/close.png')))
def insert():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/insert.png')))
def record_finish():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/record_finish.png')))
def train():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/train.png')))
def sign_finish():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/sign_finish.png')))
def user_ver():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/user_ver.png')))
def log_in():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/log_in.png')))
def confirm():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/confirm.png')))
def user_name():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/user_name.png')))
def account():
    pyautogui.click((pyautogui.locateCenterOnScreen('PyAutoGUI/account.png')), clicks=2)
def write(speak):
    pyautogui.hotkey('ctrl', 'space')
    pyautogui.typewrite(speak)