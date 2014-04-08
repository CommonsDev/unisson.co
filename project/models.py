import os
from django.db import models
from autoslug.fields import AutoSlugField

def project_upload(instance, filename):
    return os.path.join("project", filename)

class ProjectCategory(models.Model):
    """
    A Category such as "Place, Community, Platform, ..."
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Practice(models.Model):
    practice = models.CharField(max_length=200)
    description = models.TextField()
    interest = models.TextField()
    example = models.TextField()
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return unicode(self.practice)

class Positionpractice(models.Model):
    practice = models.ForeignKey(Practice)
    position = models.IntegerField(default=0)
    description = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
            return  u"%s - %s" % (self.practice, self.position)

class Usage(models.Model):
    label = models.CharField(max_length=200)
   
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.usage


class Project(models.Model):
    """
    Root object for a project. 
    """
    slug = AutoSlugField(populate_from='name',
                         always_update=False)

    name = models.CharField(verbose_name=('name'),
                            		max_length=150)

    baseline = models.CharField(verbose_name=("one line description"),
                                    max_length=180)
    description = models.TextField()
    website = models.URLField(verbose_name=('website'),
                              max_length=200,
                              null=True,
                              blank=True)
    
    picture = models.ImageField(upload_to=project_upload, null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, related_name='project')

    positionpractice = models.ManyToManyField(Positionpractice, verbose_name=("positionpractice"),)
    
    usage = models.ForeignKey(Usage, null=True, blank=True)

    def __unicode__(self):
    	return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', (self.slug,))
