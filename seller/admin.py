from django.contrib.auth.decorators import login_required
from userprofile.models import Profile
from django.shortcuts import render, redirect

@login_required
def admin_dashboard(request):

    profile = Profile.objects.get(user=request.user)

    if profile.role != "admin":
        return redirect("home")

    return render(request, "admin_dashboard.html")