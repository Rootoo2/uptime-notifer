# uptime-notifer

Simple notifier that informs user when a device has been left on for too long.

Config.ini - Default  
[Main]  
Message: Your device has been on for more than a day, we recommend restarting your device when possible.  
NotificationTitle: Restart reminder  
Repeat: True  
Duration: 20  
Threaded: True  
RepeatIntervalHour: 1  
LoopDelay: 1  
NotifyStart: True

---

Description  
Message: Long message in notification  
NotificationTitle: Title of notification  
Repeat: Whether to repeat the notification or not  
Duration: Length of notification message  
Threaded: Smoother running creates side process for notification  
RepeatIntervalHour: Repeat timer  
LoopDelay: Delay of checking up time, longer = less resources  
NotifyStart: Notifies the user when the app has started

---

c:\path\to\package.msi /quiet /qn
