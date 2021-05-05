from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'email', 'phone', 'timestamp')
  list_display_links = ('first_name', 'email', 'phone',)
  search_fields = ('first_name', 'email', 'phone',)
  ordering = ['timestamp']