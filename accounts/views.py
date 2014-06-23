from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden, Http404, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

from guardian.decorators import permission_required_or_403
from userena.utils import signin_redirect, get_profile_model, get_user_model
from userena import settings as userena_settings
from userena.views import ExtraContextTemplateView
from userena.views import profile_edit as userena_profile_edit, profile_detail as userena_profile_detail
from userena.decorators import secure_required

from .forms import ProfileEditForm

def profile_detail(request, username):
    """
        Add extra context and returns userena_profile_detail view
    """
    extra_context = {}
    user = get_object_or_404(get_user_model(),
                             username__iexact=username)

    # Get profile
    profile_model = get_profile_model()
    profile = user.get_profile()
    # Check perms
    if not profile.can_view_profile(request.user):
        return HttpResponseForbidden(_("You don't have permission to view this profile."))

    # context
    extra_context['profile'] = profile
    extra_context['hide_email'] = userena_settings.USERENA_HIDE_EMAIL

    return userena_profile_detail(request=request, username=username, extra_context=extra_context)

