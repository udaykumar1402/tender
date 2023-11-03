from django import forms
from .models import Proposal,UserProfile,ProposalSectionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
            'title',
            'company_name',
            'contact_name',
            'contact_email',
            'contact_phone',
            'proposal_summary',
            'project_planning',
            'financing',
        ]


class Createuser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class DeleteProposalForm(forms.Form):
    confirm = forms.BooleanField(required=True, widget=forms.HiddenInput, initial=True)

class ProposalSection(forms.ModelForm):
    class Meta:
        model = ProposalSectionForm
        fields = ['proposal', 'section_name', 'content', 'position']


