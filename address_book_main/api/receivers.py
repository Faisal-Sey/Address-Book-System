from django.dispatch import receiver
from . import signals
from django.core.mail import send_mail
from django.conf import settings


@receiver(signals.upload_complete)
def upload_complete(sender, bool, **kwargs):
  if (sender == "upload_complete" and bool):
    try:
      send_mail(
        subject="Upload Complete",
        message="Your Upload is complete",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list = [settings.RECIPIENT_ADDRESS]
      )
    except Exception as e:
      pass