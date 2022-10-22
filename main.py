from plyer import notification
import time
a = 0
while a == 0:
    notification.notify(
        title="PLEASE DRINK WATER!!",
        message = "Drinking Water is essential \n About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon="Iconsmind-Outline-Glass-Water.ico",
        timeout=10
    )
    time.sleep(3600)


