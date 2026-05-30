from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from userprofile.models import Profile

@login_required
def seller_dashboard(request):

    profile = Profile.objects.get(user=request.user)

    if profile.role != "seller":
        return redirect("home")

    return render(request, "seller_dashboard.html")