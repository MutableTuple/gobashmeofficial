from django.shortcuts import render
from .models import Profiles, Message
# Create your views here.
def Messages(request,username):
    user= request.user
    profile = Profiles.objects.get(username=username)       
    messages = Message.objects.filter(recipient=request.user.profiles)
    # if sender in messages:
    #     print("SEnder", sender)
    total_messages = messages.count()
    context={"profile":profile,"messages":messages,"total_messages":total_messages}
    return render(request,"users/messages.html", context)
    