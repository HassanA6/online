from django.db.models.signals import post_save, pre_save

# from django.dispatcher import receiver
from django.dispatch import receiver
from .models import User, Userprofile


"""

Sender => User model

Receiver => post_save_create_profile_receiver


"""


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print("created", created)
    if created:
        Userprofile.objects.create(user=instance)
        print("user profile created")

    else:
        try:
            profile = Userprofile.objects.get(user=instance)
            profile.save()
            print("user profile updated")
        except Userprofile.DoesNotExist:
            Userprofile.objects.create(user=instance)
            print("user profile created, as it does not exist")
        # instance.userprofile.save()s


@receiver(pre_save, sender=User)
def pre_save_create_profile_receiver(sender, instance, **kwargs):
    print("created", instance.username)


# post_save.connect(post_save_create_profile_receiver, sender=User)
