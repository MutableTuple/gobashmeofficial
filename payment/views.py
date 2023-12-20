import stripe
from django.shortcuts import render, redirect
from users.models import Profiles
from django.urls import reverse
# stripe information
stripe.api_key = "pk_test_51NUuIcSB1VPh1S87YA3n8cd2CbvdrGzJpNaXElWqcP54TKCMexi0P81cQi97L7Acvb62wwHM1IwHeClkqUCIwmmV007DQIrxTw"

# Create your views here.
def Payment(request,username):
    profile = Profiles.objects.get(username=username)        
    context={"profile":profile}
    return render(request,"payments/payment.html",context)

def charge(request):
    amount = 5
    if request.method=="POST":
        print("data", request.POST)
        
    return redirect(reverse("success", args=[amount]))
    
def successMessage(request, args):
    amount =args
    return render(request,"base/success.html", {"amount":amount})