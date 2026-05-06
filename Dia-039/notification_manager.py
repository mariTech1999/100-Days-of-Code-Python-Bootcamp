import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_SID']
        self.auth_token = os.environ['TWILIO_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ['TWILIO_PHONE'],
            body = message_body,
            to=os.environ['TWILIO_MY_PHONE'],

        )
        print(f"Message sent: {message.sid}")