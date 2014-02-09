from django.views.generic import RedirectView
from django.core.urlresolvers import reverse


class RootRouter(RedirectView):
    """
    Route user to his/her profile is logged in otherwise, show the
    welcoming page.
    """
    def get_redirect_url(self, **kwargs):
        if self.request.user.is_authenticated():
            return reverse('profile-detail', args=(self.request.user.username,))
        else:
            return reverse('home')