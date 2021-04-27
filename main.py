import vk
import time
import settings
import psutil
import os
import datetime
from os import system, name
session = vk.Session()
api = vk.API(session, access_token=settings.vk_token, v='5.60', lang='ru') #access_token=settings.vk_token

if (api):
    statusVK = input("Status number #")
    if (statusVK == "1"):
        _ = system('cls')
        api.status.set (text="Wibe (Idle)", group_id=0)
        print("Current status: IDLE (1)")
        statusVK = input("Status number #")
    if (statusVK == "2"):
        _ = system('cls')
        
        process_name = "chrome.exe" # Proccess name (can with .exe and without)
        pid = None

        while True:
            current_date_time = datetime.datetime.now()
            current_timeFull = current_date_time.time()
            current_time = str(current_timeFull)[:-7]
            for proc in psutil.process_iter():
                if proc.name() == process_name:
                    pid = proc.pid
                    proccessNameFull = psutil.Process(pid).name()
                    proccessName = proccessNameFull[:-4]
                    proccess = psutil.Process(pid).create_time()
                    proccessD = datetime.datetime.fromtimestamp(proccess).strftime("%H:%M:%S")
                    print (str(psutil.Process(pid).status()))
                    api.status.set (text="Playing "+str(proccessName)+" (InGame) | Start time: " + str(proccessD) + "\nCurrent time: " + str(current_time), group_id=0)
                    print("Current status: INGAME | "+str(proccessName)+" (2)")
                    time.sleep(10)

        statusVK = input("Status number #9")
        if (statusVK == "9"):
            psutil.Process(pid).kill()
    if (statusVK == "3"):
        _ = system('cls')
        anime = input("Anime, which you are watching rn: ")
        api.status.set (text="Watching anime: " + str(anime) + " (Browser)", group_id=0)
        print("Current status: BROWSER | "+str(anime)+" (3)")
        statusVK = input("Status number #")