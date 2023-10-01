from django.contrib import admin
from .models import Note, Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_public', 'text']
    list_filter = ['is_public']
    list_editable = ['is_public']

admin.site.register(Note)
admin.site.register(Feedback, FeedbackAdmin)

