from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail

from .models import Publication, Subscriber 

@receiver(post_save, sender=Publication)
def send_newsletter_on_post(sender, instance, created, **kwargs):
    if created:  
        subscribers = Subscriber.objects.all()
        if subscribers.exists():
            subject = f"Nouvel article : {instance.titre}"
            message = f"Bonjour ! Un nouvel article vient d'être publié : {instance.titre}.\n\nDécouvrez-le ici : https://monblog-f2p8.onrender.com/#idees"
            from_email = 'djibrila6299@gmail.com'
            
            
            mails = [
                (subject, message, from_email, [sub.email]) 
                for sub in subscribers
            ]    
           
            send_mass_mail(mails, fail_silently=False)