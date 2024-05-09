class EmailNotification:
    @staticmethod
    def send_email(subject, message):
        print(f"sending email with subject: {subject} and message: {message}")


class SMSNotification:
    @staticmethod
    def send_sms(message):
        print(f"send sms with message: {message}")


class Notification:
    @staticmethod
    def send(message):
        pass


class EmailNotificationAdapter(Notification):
    def __init__(self, email_notification):
        self.email_notification = email_notification

    def send(self, message):
        self.email_notification.send_email(None, message)


class SMSNotificationAdapter(Notification):
    def __init__(self, smsnotification):
        self.smsnotification = smsnotification

    def send(self, message):
        self.smsnotification.send_sms(message)


def notify(notification):
    return notification.send("This is a test message")


email = EmailNotification()
email_adapter = EmailNotificationAdapter(email)
notify(email_adapter)

sms = SMSNotification()
sms_adapter = SMSNotificationAdapter(sms)
notify(sms_adapter)

