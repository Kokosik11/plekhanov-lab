from django.contrib import admin
from .models import Post, Project, Feedback

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'status')
    list_editable = ('status',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'created_on',)
    ordering = ['created_on']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'status')
    list_editable = ('status',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'created_on',)
    ordering = ['created_on']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'uuid')
    list_display_links = ('email', 'uuid',)
    search_fields = ('name', 'email', 'phone', 'uuid',)
    ordering = ['name']

admin.site.site_title = 'Администрирование Лаборатории'
admin.site.site_header = 'Лаборатория Графического дизайна и веб-проектирования'