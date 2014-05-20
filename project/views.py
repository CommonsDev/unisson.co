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
from django.views.generic.edit import FormView
from django.shortcuts import render_to_response, get_object_or_404, redirect
from project.models import Project, Practice, Usage
from .forms import ProjectAddForm

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
    

class UsageListView(ListView):
    """
    List all usages
    """
    model = Project
    template_name = 'project/usage_list.html'
    context_object_name = 'project'
    

class ProjectStartView(FormView):
    """
When one starts a project, after having selected a topic
"""
    template_name = 'project/add.html'
    form_class = ProjectAddForm
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        project = form.save(commit=False)
        project.save()

        messages.success(self.request, _("Project '%(project_name)s' added" % {'project_name':project.name}))
        
        return super(ProjectStartView, self).form_valid(form)





