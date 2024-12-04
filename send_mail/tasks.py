from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import send_mail
from celeryapp import settings
# Create your views here.
@shared_task(bind=True)
def send_mail_function(self):
    users = User.objects.exclude(is_superuser = True)
    for user in users:
        mail_subject = "Alert"
        message = "Your subscription will expire soon. Please Renew Now"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
            )
    return "Done"