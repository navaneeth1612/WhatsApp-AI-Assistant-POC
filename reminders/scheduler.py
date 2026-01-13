from apscheduler.schedulers.background import BackgroundScheduler
from app.whatsapp import send_message

scheduler = BackgroundScheduler()
scheduler.start()

def set_reminder(time, phone, text):
    scheduler.add_job(send_message, 'date', run_date=time, args=[text, phone])
