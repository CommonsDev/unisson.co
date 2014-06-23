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



def create_profile(user=None, profile=None, *args, **kwargs):
    """
    Create user profile if necessary
    """
    if profile:
        return { 'profile': profile }
    if not user:
        return
    return { 'profile': Profile.objects.get_or_create(user=user)[0] }


def set_guardian_permissions(user=None, profile=None, *args, **kwargs):
    """
    Give the user permission to modify themselves
    """
    if not user or not user.is_authenticated():
        return
    if profile:
        # Give permissions to view and change profile
        for perm in ASSIGNED_PERMISSIONS['profile']:
            assign(perm[0], user, profile)

    # Give permissions to view and change itself
    for perm in ASSIGNED_PERMISSIONS['user']:
        assign(perm[0], user, user)


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