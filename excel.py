import win32com.client
import pythoncom
import time

def popen1():
    pythoncom.CoInitialize()
    global excel
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = True
    global workbook
    workbook = excel.Workbooks.Open(r"C:\Users\USER\GUI_SpeakerID\voice_control.xlsx")

def popen2():
    pythoncom.CoInitialize()
    global excel
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = True
    global workbook
    workbook = excel.Workbooks.Open(r"C:\Users\USER\GUI_SpeakerID\instruction.xlsx")
    
def pclose():
    workbook.Close(False)
    excel.Application.Quit()
    pythoncom.CoUninitialize()