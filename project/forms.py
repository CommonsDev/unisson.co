# forms.py
from django import forms

from project.models import Project, Practice, Positionpractice

class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','positionpractice')

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
