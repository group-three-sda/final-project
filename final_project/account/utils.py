from django.core.mail import send_mail
from django.conf import settings


def mail(username, user_email):
    subject = "Thanks for open account in our service."
    message = f"{username} \
            Welcome in Snapvisite service. We are happy to see you here.Don't waste your time and snap your first visit!\
            Our service is still very young, so fell good to send to us your fresh ideas about new functionalities.\
            Thank you!"
    from_email = settings.EMAIL_HOST_USER
    to_email = [user_email, ]
    send_mail(subject, message, from_email, to_email)
