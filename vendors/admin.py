from django.contrib import admin
from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display = (

        'shop_name',
        'email',
        'phone',
        'verified',
        'total_sales',
        'total_orders',

    )

    search_fields=(

        'shop_name',
        'email'

    )

    list_filter=(

        'verified',

    )