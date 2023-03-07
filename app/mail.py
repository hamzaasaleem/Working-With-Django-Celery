# from django.core import mail
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# from django-celery-demo.settings import
from .enums import SetupStatus
from .models import EmailSchedule

# def send_email():
#     subject = 'Subject'
#     html_message = render_to_string('testmail.html', {'context': 'values'})
#     plain_message = strip_tags(html_message)
#     from_email = 'iamtahir727@gmail.com'
#     to = 'iamtahir727@gmail.com'
#
#     mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)


class EmailService(object):

    def send_email(self, email):
        subject = 'confirm via email'
        html_message = render_to_string('testmail.html')
        message = strip_tags(html_message)
        recepient = email
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient], html_message=html_message,
                      fail_silently=False)
            instance = EmailSchedule.objects.get(email=email)
            instance.status = SetupStatus.disabled
            instance.save()
            instance.task.enabled = False
            instance.task.save()
        except Exception as e:
            print(e)
