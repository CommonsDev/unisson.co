import os
from django.db import models

def project_upload(instance, filename):
    return os.path.join("project", filename)

class ProjectCategory(models.Model):
    """
    A Category such as "Place, Community, Platform, ..."
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    """
    Root object for a project. 
    """
    name = models.CharField(verbose_name=('name'),
                            		max_length=150)

    baseline = models.CharField(verbose_name=("one line description"),
                                    max_length=180,
                                    null=True,
                                    blank=True,
                                    default=("One line description")
                                ),
    description = models.TextField()
    website = models.URLField(verbose_name=('website'),
                              max_length=200,
                              null=True,
                              blank=True)
    
    picture = models.ImageField(upload_to=project_upload, null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, related_name='project')

    def __unicode__(self):
    	return self.name

