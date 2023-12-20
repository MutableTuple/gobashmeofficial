from django.shortcuts import render, redirect
from users.models import Profiles,Message
from .forms import MessageForm
from django.contrib.auth.models import User

# Create your views here.
def bashHome(request):
    profile = Profiles.objects.all()
    context={"profile":profile}
    return render(request,"bash/bash-home.html", context)

def basheMe(request,username):
    user= request.user
    profile = Profiles.objects.get(username=username)        
    recipient=Profiles.objects.get(username=username)
    sender = request.user.profiles
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            message.save()
            return redirect(request.path)
            
             #creates objecrt
     
    context={"profile":profile,"form":form,"recipient":recipient,"sender":sender}
    return render(request,"bash/bash-me.html", context)
    
    # if profile.exists():
    # else:
    #     return render(request,"bash/404.html", context)

