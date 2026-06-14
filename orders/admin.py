from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
        'price',
        'quantity',
        'total_amount',
        'status',
        'created_at'
    )

    list_filter = ('status', 'created_at')
    search_fields = ('name', 'user__username', 'phone')
    ordering = ('-created_at',)

    list_editable = ('status',)
    date_hierarchy = 'created_at'

    readonly_fields = (
        'created_at',
    )