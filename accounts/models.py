from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


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
