from django.http import HttpResponse
from .models import MyModel
from django.db import transaction
import threading
import time

def test_signal(request):
    # Check if the signal is executed in the same thread
    print(f"View thread: {threading.current_thread().name}")
    
    start_time = time.time()
    
    try:
        # Simulate a database transaction with rollback
        with transaction.atomic():
            MyModel.objects.create(name="Test Object")
            raise Exception("Simulating a transaction failure")  # This will rollback the transaction
    except Exception as e:
        print(f"Transaction failed: {str(e)}")

    end_time = time.time()
    return HttpResponse(f"Object creation attempted. Total time: {end_time - start_time} seconds")
