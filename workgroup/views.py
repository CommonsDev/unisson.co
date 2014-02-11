from django.shortcuts import render


from .models import WorkGroup
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import View
from .utils import lookup_ml_membership
from django.shortcuts import redirect, get_object_or_404
from django.core.cache import cache
from django.contrib import messages
from django.utils.translation import ugettext as _
# Create your views here.


class GroupDetailView(DetailView):
    template_name = 'workgroup/group_detail.html'
    context_object_name = 'workgroup'
    queryset = WorkGroup.objects.prefetch_related('subscribers__profile')

    def get_context_data(self, **kwargs):
        """
Adds the member of the associated ML if there's one
"""
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        
        workgroup = context['workgroup']

        # Look up mailing list members
        context.update(lookup_ml_membership(workgroup))

        return context

class GroupMembersView(GroupDetailView):
    """
    List all members of the given group
    """
    template_name = 'workgroup/group_members.html'


class GroupListArchiveView(GroupDetailView):
    """
    Display mailing lisy archives
    """
    template_name = 'workgroup/group_list_archive.html'

class SubscribeView(View):
    """
    Subscribe a user to the workgroup
    """
    @method_decorator(login_required)
    def get(self, request, workgroup_slug):
        workgroup = get_object_or_404(WorkGroup, slug=workgroup_slug)
        user = request.user

        # Subscibre the user to the workgroup
        workgroup.subscribers.add(user)
        
        # Force cache regeneration
        cache_key = '%s-ml-members' % workgroup.slug
        cache.delete(cache_key)

        # Subscribe the user to the mailing list        
        if workgroup.mailing_list:
            ml = workgroup.mailing_list
            try:
                ml.subscribe(user.email,
                             user.first_name,
                             user.last_name,
                             send_welcome_msg=True)

                messages.success(request, _(u"You have been successfully subscribed to the"
                                            u"%(workgroup_name)s mailing list"
                                            u" (%(user_email)s)" % {'workgroup_name': workgroup.name,
                                                                    'user_email': user.email}
                                            )
                                 )
            except Exception, e:
                messages.error(request, _(u"You couldn't be subscribed to this group:%s" % unicode(e.message, encoding=ml.encoding)))

        next_url = request.GET.get('next_url', None)
        if next_url:
            return redirect(next_url)
        else:
            return redirect(workgroup)


class UnsubscribeView(View):
    """
    Unsubscribe a user to the group
    """
    @method_decorator(login_required)
    def get(self, request, workgroup_slug):
        workgroup = get_object_or_404(WorkGroup, slug=workgroup_slug)
        user = request.user

        # Removing user from workgroup
        workgroup.subscribers.remove(user)
        
        # Force cache regeneration
        cache_key = '%s-ml-members' % workgroup.slug
        cache.delete(cache_key)

        # removing user from mailing list
        if workgroup.mailing_list:
            ml = workgroup.mailing_list
            try:
                ml.unsubscribe(user.email)

                messages.success(request, _(u"You have been successfully unsubscribed from the"
                                            u"%(workgroup_name)s mailing list"
                                            u" (%(user_email)s)" % {'workgroup_name': workgroup.name,
                                                                    'user_email': user.email}
                                            )
                                 )
            except Exception, e:
                messages.error(request, _(u"You couldn't be unsubscribed from this group:%s" % e.message))

        next_url = request.GET.get('next_url', None)
        if next_url:
            return redirect(next_url)
        else:
            return redirect(workgroup)
