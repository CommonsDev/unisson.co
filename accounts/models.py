from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from taggit.managers import TaggableManager


from userena.managers import ASSIGNED_PERMISSIONS
from guardian.shortcuts import assign

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    location = models.CharField(max_length=50,
                                null=True, blank=True,
                                help_text=_("City, Country, ..."))    
    about = models.TextField(null=True, blank=True,
                             help_text=_("A few words about you."))

    website = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True,
                               help_text=_("Your twitter username"))
    
    skills = TaggableManager()

    @models.permalink
    def get_absolute_url(self):
        return ('profile-detail', [self.user.id])


# Fix for #14 , using http://stackoverflow.com/questions/12142195/django-userena-edit-profile-forbidden
from django.dispatch import receiver
from django.db.models.signals import post_save
@receiver(post_save, sender=User, dispatch_uid='user.created')
def user_created(sender, instance, created, raw, using, **kwargs):
  """ Adds 'change_profile' permission to created user objects """
  if created:
    from guardian.shortcuts import assign
    try:
      profile = instance.get_profile()
    except:
      # profile does not exists
      profile = Profile(user=instance)
      profile.save()
      
    assign('change_profile', instance, profile)