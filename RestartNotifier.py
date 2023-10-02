# ctypes required for using GetTickCount64()
import ctypes
from win10toast import ToastNotifier
from time import sleep, time
import configparser
import os
import sys

Config = configparser.ConfigParser()
# getting the library in which GetTickCount64() resides
lib = ctypes.windll.kernel32
toast = ToastNotifier()
try:
    basePath = sys._MEIPASS
    iconPath = os.path.join(basePath, "alert.ico")
    if not os.path.exists(iconPath):
        iconPath = "alert.ico"
except:
    iconPath = "alert.ico"

def get_config():
    
    if os.path.exists("./config.ini"):

        Config.read("./config.ini")
        config = {"Message":Config.get("Main", "Message"), 
                "NotificationTitle":Config.get("Main", "NotificationTitle"),
                "Repeat": bool(Config.get("Main", "Repeat")),
                "Duration":int(Config.get("Main", "Duration")),
                "Threaded":bool(Config.get("Main", "Threaded")),
                "RepeatIntervalHour":int(Config.get("Main", "RepeatIntervalHour")),
                "LoopDelay":int(Config.get("Main", "LoopDelay")),
                "NotifyStart":bool(Config.get("Main", "NotifyStart"))
                }
        return config
    else:
        print("Using default")
        config = {"Message": "Your device has been on for more than a day, we recommend restarting your device when possible",
                "NotificationTitle":"Restart reminder",
                "Repeat":True,
                "Duration":20,
                "Threaded":True,
                "LoopDelay":1,
                "NotifyStart":True
                }
        return config
    


def get_uptime():
    # calling the function and storing the return value
    t = lib.GetTickCount64()
    
    # since the time is in milliseconds i.e. 1000 * seconds
    # therefore truncating the value
    t = int(str(t)[:-3])
    
    # extracting hours, minutes, seconds & days from t
    # variable (which stores total time in seconds)
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    
    
    return days


config = get_config()


if config["LoopDelay"] < 1:
    config["LoopDelay"] = 1

lastNotified = 0

if config["NotifyStart"]:
    toast.show_toast(
    "Start notification",
    "Restart Notifier started",
    duration = 5,
    icon_path = iconPath,
    threaded = config["Threaded"],
    )



while 1:
    sleep(config["LoopDelay"])
    
    days = get_uptime()
    
    if days >= 1:
        if (time() - lastNotified) > (config["RepeatIntervalHour"] * 60 * 60):
            lastNotified = time()
            print("Notify")


            toast.show_toast(
            config["NotificationTitle"],
            config["Message"],
            duration = config["Duration"],
            icon_path = iconPath,
            threaded = config["Threaded"],
            )
            if not config["Repeat"]:
                break
