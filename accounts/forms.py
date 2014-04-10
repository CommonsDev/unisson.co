from django import forms

from userena.forms import EditProfileForm

class ProfileEditForm(EditProfileForm):

    class Meta(EditProfileForm.Meta):
        exclude = EditProfileForm.Meta.exclude + ['user', 'privacy']
