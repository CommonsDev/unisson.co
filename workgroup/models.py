import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug.fields import AutoSlugField
from cms.models.pluginmodel import CMSPlugin
from django_mailman.models import List
from workgroup.utils import lookup_ml_membership
from cms.models.fields import PlaceholderField

# Create your models here.

class WorkGroup(models.Model):
    """
A workgroup in a given language, for a given thematic.
"""
    slug = AutoSlugField(populate_from='name',
                         always_update=False)

    name = models.CharField(verbose_name=_('name'),
                            max_length=150)

    language = models.CharField(verbose_name=_('spoken language'),
                                max_length=2,
                                choices=settings.LANGUAGES)

    description = models.TextField(verbose_name=_('Description'),
                                    null=True,
                                    blank=True)
    
    register_button = models.CharField(verbose_name=_('Text for the register button'),
                                    max_length=50,
                                    null=True,
                                    blank=True)
 
    registered_button = models.CharField(verbose_name=_('Text for the register button when registered'),
                                    max_length=50,
                                    null=True,
                                    blank=True)
                                    
    mailing_list = models.ForeignKey(List,
                                     default=None,
                                     null=True, blank=True)

    visible = models.BooleanField(verbose_name=_('visible'),
                                  default=True)
    
    outside_url = models.URLField(_('External URL'),
                                  null=True,
                                  blank=True,
                                  help_text=_("A URL that points to the real discussion tool, if we're not using the built-in (eg Facebook group URL).")
                              )

    subscribers = models.ManyToManyField(User,
                                         verbose_name=_("Subscribers"),
                                         related_name='workgroups',
                                         blank=True
                                      )

    def __unicode__(self):
        return u"%s (%s)" % (self.name,
                             self.get_language_display())


    @models.permalink
    def get_absolute_url(self):
        return ('workgroup-detail', (self.slug,))



class WorkGroupCMS(CMSPlugin):
    workgroup = models.ForeignKey(WorkGroup)

    def copy_relations(self, oldinstance):
        self.workgroup = oldinstance.workgroup