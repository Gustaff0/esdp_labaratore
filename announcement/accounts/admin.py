from django.contrib import admin
from accounts.models import Number

# Register your models here.

class NumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'user']
    list_filter = ['user']
    search_fields = ['user']
    fields = ['id', 'number', 'user']
    readonly_fields = ['id']


admin.site.register(Number, NumberAdmin)