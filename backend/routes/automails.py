from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

from backend.models.common import db
from backend.models.donor import Donor
import smtplib

# Define the intervals for reminders
FREQUENCY_INTERVALS = {
    'daily': timedelta(days=1),
    'weekly': timedelta(weeks=1),
    'monthly': timedelta(days=30),  # Approximate, adjust as needed
    'quarterly': timedelta(days=90),  # Approximate, adjust as needed
}

def send_donation_reminder_task(frequency):
    donor_records = Donor.query.filter_by(frequency=frequency).all()

    if donor_records:
        for donor in donor_records:
            next_reminder_date = donor.next_donation_date + FREQUENCY_INTERVALS[donor.frequency]

            if next_reminder_date.date() <= datetime.now().date():
                send_donation_reminder(donor)

def send_donation_reminder(donor):
    subject = "Donation Reminder"
    body = "This is a reminder to make your donation."

    sender_email = "testduans@gmail.com"  # Your sender email
    sender_password = "dovv oswy ttjy egcg"  # Your sender email password
    smtp_server = "smtp.gmail.com"  # Your SMTP server address
    smtp_port = 587  # Your SMTP server port (usually 587 for TLS)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = donor.email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS (port 587)
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, donor.email, message.as_string())
            print(f"Email sent successfully to {donor.email}")
            donor.next_donation_date = datetime.now() + FREQUENCY_INTERVALS[donor.frequency]
            db.session.commit()
    except Exception as e:
       print(f"Email sending failed: {str(e)}")

if __name__ == "__main__":
    # Create a BackgroundScheduler
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Schedule the tasks
    scheduler.add_job(send_donation_reminder_task, CronTrigger(hour=0), args=['daily'])
    scheduler.add_job(send_donation_reminder_task, CronTrigger(day_of_week='mon', hour=0), args=['weekly'])
    scheduler.add_job(send_donation_reminder_task, CronTrigger(day='1', hour=0), args=['monthly'])
    scheduler.add_job(send_donation_reminder_task, CronTrigger(month='1', day='1', hour=0), args=['quarterly'])


