import vk
import time
import settings
import psutil
import datetime
session = vk.Session()
api = vk.API(session, access_token=settings.vk_token, v='5.60', lang='ru')

find = 0

while True:
    find = 0
    for proc in psutil.process_iter():
        if proc.name() == "osu.exe":
            pid = proc.pid
            processNameFull = psutil.Process(pid).name()
            processName = processNameFull[:-4]
            process = psutil.Process(pid).create_time()
            processD = datetime.datetime.fromtimestamp(process).strftime("%H:%M:%S")
            processStatus = psutil.Process(pid).status()
            print("Current status: IN GAME | " + str(processName) + " (" + str(processStatus) + ")")
            find = 1
            time.sleep(10)
        if proc.name() == "pycharm64.exe":
            pid = proc.pid
            processName = psutil.Process(pid).name()[:-6]
            processStatus = psutil.Process(pid).status()
            print("Current status: PROGRAM | " + str(processName) + " (" + str(processStatus) + ")")
            find = 1
            time.sleep(10)
        if proc.name() == "chrome.exe":
            pid = proc.pid
            processName = psutil.Process(pid).name()[:-4]
            processStatus = psutil.Process(pid).status()
            print("Current status: IN BROWSER | " + str(processName) + " ("+str(processStatus)+")")
            find = 1
            time.sleep(10)
        if find == 0:
            print("Current status: IDLE | idle.exe (running)")
