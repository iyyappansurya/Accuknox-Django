# By deafault, signals are executed synchronously
# In the below example only after task1 is completed task2 will start till then task2 will be waiting
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def task1(sender, instance, created, **kwargs):
    if created:
        print("Signal received, starting a task1...")
        print("Signal task1 complete.")

@reciever(post_save,sender=User)
def task2(sender, instance, created, **kwargs):
    if created:
        print("Signal received, starting a task2...")
        print("Signal task2 complete.")

print("Saving the user...")

user = User.objects.create(username="test_user")

print("User saved.")
