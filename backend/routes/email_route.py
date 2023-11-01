from backend.models.common import db
from backend.models.donor import Donor
from flask import Blueprint, jsonify, request

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = Blueprint('email', __name__)

from backend.models.common import db
from backend.models.donor import Donor
from flask import Blueprint, jsonify, request

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

email = Blueprint('email', __name__)

# Define a dictionary to map frequencies to timedelta intervals
FREQUENCY_INTERVALS = {
    'daily': timedelta(days=1),
    'weekly': timedelta(weeks=1),
    'monthly': timedelta(days=30),  # Approximate, adjust as needed
    'quarterly': timedelta(days=90),  # Approximate, adjust as needed
}

@email.route('/send_donation_reminder', methods=['GET'])
def send_donation_reminder():
    # Get all donor emails from the Donor table
    donor_records = get_all_donor_records()

    if donor_records:
        # Customize the donation reminder content
        subject = "Donation Reminder"
        body = "This is a reminder to make your donation."

        for donor in donor_records:
            # Calculate the next reminder date based on the donor's frequency
            if donor.frequency in FREQUENCY_INTERVALS:
                next_reminder_date = donor.next_donation_date + FREQUENCY_INTERVALS[donor.frequency]
                
                # Check if it's time to send a reminder
                if next_reminder_date.date() <= datetime.now().date():
                    send_email(subject, body, donor.email)
                    
                    # Update the next_donation_date
                    donor.next_donation_date = next_reminder_date

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'Donation reminder emails sent successfully'}), 200
    else:
        return jsonify({'message': 'No donors found in the database'}), 404

def get_all_donor_records():
    donor_records = Donor.query.filter(Donor.email.isnot(None)).all()
    
    return donor_records

def send_email(subject, body, to_email):
    # Email configuration
    sender_email = "testduans@gmail.com"  # Your sender email
    sender_password = "dovv oswy ttjy egcg"  # Your sender email password
    smtp_server = "smtp.gmail.com"  # Your SMTP server address
    smtp_port = 587  # Your SMTP server port (usually 587 for TLS)

    # Create a message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email  # Use the donor's email as the recipient
    message["Subject"] = subject

    # Attach the message body
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS (port 587)
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

        # Disconnect from the server
        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Email sending failed: {str(e)}")
