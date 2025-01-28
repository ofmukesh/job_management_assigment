from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')
    search_fields = ('title', 'description')
    readonly_fields = ('posted_at',)
    list_filter = ('posted_at',)
