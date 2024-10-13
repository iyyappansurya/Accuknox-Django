# Yes, Django signal run in the same thread as the caller
# As they are run synchronously by default, they run in the same thread by default
# In the below example, have just created a separate background task with a different thread, task1 will be running
# on the main thread
import threading

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def task1(sender, instance, created, **kwargs):
    if created:
        print("Signal received, starting a task1...")
        print(f"running in thread: {threading.current_thread().name}")
        print("Signal task1 complete.")

def background_task():
    print(f"Background task running in thread: {threading.current_thread().name}")


background_thread = threading.Thread(target=background_task)
background_thread.start()

print(f"Main running in thread: {threading.current_thread().name}")
print("Saving the user...")

user = User.objects.create(username="test_user")

print("User saved.")
