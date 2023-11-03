from django.contrib import admin
from .models import Proposal,ProposalSectionForm,UserProfile
# Register your models here.


admin.site.register(Proposal)
admin.site.register(ProposalSectionForm)
# admin.site.register(saved_proposals)
admin.site.register(UserProfile)