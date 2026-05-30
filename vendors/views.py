from django.shortcuts import render
from .models import Vendor


def vendor_dashboard(request):

    vendors = Vendor.objects.all()

    return render(

        request,

        'vendor_dashboard.html',

        {

            'vendors': vendors

        }

    )