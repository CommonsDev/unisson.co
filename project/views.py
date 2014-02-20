from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormView
from django.views.generic import DeleteView, ListView, DetailView
from django.http import HttpResponse

from project.models import Project, Practice


class ProjectDetailView(DetailView):
    model=Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'
   

class ProjectListView(ListView):
    """
    List all projects
    """
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'project'
    
class PracticeListView(ListView):
    """
    List all practices
    """
    model = Practice
    template_name = 'project/practice_list.html'
    context_object_name = 'practice'
    

