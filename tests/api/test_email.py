import unittest
from unittest.mock import Mock, patch, ANY
from datetime import datetime, timedelta
from backend.models.donor import Donor
from backend.routes.automails import send_donation_reminder_task, send_donation_reminder

class SendDonationReminderTaskTest(unittest.TestCase):
    def setUp(self):
        self.donor1 = Donor(email="donor1@example.com", frequency="daily", next_donation_date=datetime.now().date())
        self.donor2 = Donor(email="donor2@example.com", frequency="weekly", next_donation_date=datetime.now().date() - timedelta(days=7))
        self.donor3 = Donor(email="donor3@example.com", frequency="monthly", next_donation_date=datetime.now().date() - timedelta(days=30))
        self.donor4 = Donor(email="donor4@example.com", frequency="quarterly", next_donation_date=datetime.now().date() - timedelta(days=90))

    @patch("backend.email.send_donation_reminder")
    def test_send_donation_reminder_task_daily(self, mock_send_email):
        send_donation_reminder_task("daily")
        mock_send_email.assert_called_with(self.donor1)


class SendDonationReminderTest(unittest.TestCase):
    @patch("backend.email.smtplib.SMTP", autospec=True)
    def test_send_donation_reminder(self, mock_smtp):
        donor = Donor(email="test@example.com", next_donation_date=datetime.now().date())

        send_donation_reminder(donor)

        mock_smtp.assert_called_with("smtp.gmail.com", 587)
        mock_smtp().starttls.assert_called_once()
        mock_smtp().login.assert_called_once_with("testduans@gmail.com", "dovv oswy ttjy egcg")
        mock_smtp().sendmail.assert_called_with("testduans@gmail.com", "test@example.com", ANY)
        mock_smtp().quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
 