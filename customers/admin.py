from django.contrib import admin
from .models import CustomerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'phone',
        'role',
        'created_at'
    )

    list_filter = ('role', 'created_at')

    search_fields = (
        'user__username',
        'phone'
    )

    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    readonly_fields = (
        'created_at',
        'updated_at'
    )
    