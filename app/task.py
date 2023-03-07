# from celery import shared_task
# from time import sleep
# from .mail import *
#
# @shared_task()
# def send_email_task(email):
#     return EmailService().send_email(email)


from celery import shared_task

from .mail import EmailService
from .models import EmailSchedule


@shared_task(name="computation_heavy_task")
def computation_heavy_task(setup_id):
    setup = EmailSchedule.objects.get(id=setup_id)
    print('''Running task for setup {setup_title}.'''.format(
        setup_title=setup.title))
    EmailService().send_email(setup.email)
