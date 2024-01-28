from django.contrib import admin
from .models import Note, Feedback , Skill, SkillDetail

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_public', 'text']
    list_filter = ['is_public']
    list_editable = ['is_public']

admin.site.register(Note)
admin.site.register(Skill)
admin.site.register(SkillDetail)
admin.site.register(Feedback, FeedbackAdmin)

