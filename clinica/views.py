# accounts/views.py
from django.shortcuts import  render, redirect
from .forms import CriarUsuário
from django.contrib.auth import login
from django.contrib import messages

def register_user(request):
    if request.method == "POST":
        form = CriarUsuário(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/inicio/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CriarUsuário()
    return render(request, "registration/signup.html", context={"form":form})

