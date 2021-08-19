from django.contrib import admin
from api_v1.models import Announcement, Photo

# Register your models here.


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'author', 'created_at']
    list_filter = ['author', 'created_at']
    search_fields = ['author', 'description']
    fields = ['id', 'description', 'author', 'created_at']
    readonly_fields = ['id', 'created_at']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'announcement']
    list_filter = ['announcement']
    search_fields = ['announcement']
    fields = ['id', 'photo', 'announcement']


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Photo, PhotoAdmin)