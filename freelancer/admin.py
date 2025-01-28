from django.contrib import admin
from .models import Freelancer


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'user__email', 'created_at')
    search_fields = ('user__first_name', 'user__email')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)
