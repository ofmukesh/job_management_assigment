from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'job', 'status', 'applied_at')
    search_fields = ('freelancer__full_name', 'job__title', 'status')
    readonly_fields = ('applied_at',)
    list_filter = ('status', 'applied_at')
