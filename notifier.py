from notifypy import Notify

def notification(title, msg, icon = '', audio = ''):
    notification = Notify()
    notification.title = title
    notification.message = msg
    if icon != '': notification.icon = icon
    if audio != '': notification.audio = audio
    notification.send()


notification(
    f'  Yamete Kuda Sai', 
    '',
    '../icon.png', '../yameto.wav'
)