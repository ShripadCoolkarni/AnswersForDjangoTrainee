from django.http import HttpResponse
from .models import MyModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

signal_output = ""

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    global signal_output
    signal_output = "Signal triggered. Start processing...\n"
    time.sleep(5) 
    signal_output += "Signal processing complete.\n"

def test_signal(request):
    global signal_output
    MyModel.objects.create(name="Test Object")
    formatted_output = signal_output.replace("\n", "<br>")
    return HttpResponse(f"Object created.<br><br>{formatted_output}")
