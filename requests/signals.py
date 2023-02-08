from .models import AccountRequest
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

def confirmRequestRecieved(sender, instance, created, **kwargs):
    
    if created:
        request = instance
        subject = 'MECDM Projects Portal account request confirmation'
        message = 'Hi ' + request.first_name + ',\n\nYour account request is recieved and will be reviewed.\nYou will be notified in 24hrs.\n\nRegards,\nMECDM Projects Team'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [request.email],
            fail_silently=False,
        )
        
post_save.connect(confirmRequestRecieved, sender=AccountRequest)