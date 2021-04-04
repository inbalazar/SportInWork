from win10toast import ToastNotifier
import os, time, schedule

toast = ToastNotifier()

def run_app():
    os.system('py ScreenManager.py')
    print("Clicked!")

def get_ready_notification():
    toast.show_toast(title="SportInWork",
                     msg="Your workout starts in 2 minutes!!!\n\n\nGet ready!",
                     icon_path='logo2.ico',
                     duration=10,
                     callback_on_click=lambda: run_app())

def Workout_notification():
    toast.show_toast(title="SportInWork",
                     msg="Your workout starting!!!\n\n\nClick here to get started!",
                     icon_path='logo2.ico',
                     duration=10,
                     callback_on_click=lambda: run_app())

schedule.every().wednesday.at("14:25").do(get_ready_notification)
schedule.every().wednesday.at("14:35").do(Workout_notification)

while True:
    schedule.run_pending()
    time.sleep(1)