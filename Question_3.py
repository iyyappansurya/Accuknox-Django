#Yes, by default it runs in the same transaction as the caller
#by default, django does autocommit for every transacation, by explicitly defining transaction as atomic everything
#under this will be considered as one transaction
#In the below example, first we create a user and then add to group, but then we roll back, if both are different
# transactions then one will be true and other false

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def addUser(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name="default_group")
        instance.groups.add(group)
        print("User added to group.")

def transaction1():
    try:
        with transaction.atomic():  
            user = User.objects.create(username="transaction_test_user")
            print("User created.")
            
            raise Exception("Simulated error: rolling back transaction.")
    except Exception as e:
        print(f"Exception occurred: {e}")

transaction1()

user_exists = User.objects.filter(username="transaction_test_user").exists()
group_exists = Group.objects.filter(name="default_group", user__username="transaction_test_user").exists()

print("User exists: " ,user_exists)
print("User in group: " ,group_exists)
