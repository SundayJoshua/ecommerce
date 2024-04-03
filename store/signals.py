from django.contrib.auth.models import User




@receiver(post_save, sender = User, dispatch_uid = 'save_new_user_customer')
def save_customer(sender, instance, created, ** kwargs):
   user = instance
if created:
   customer = UserProfile(user = user)
customer.save()