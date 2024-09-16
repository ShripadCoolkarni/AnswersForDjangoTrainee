from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    output = "Signal triggered. Start processing...\n"
    time.sleep(5)
    output += "Signal processing complete.\n"
    return output 
