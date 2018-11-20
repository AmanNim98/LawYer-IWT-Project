from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def LoginView(request):
    dictV = {}
    if request.method == 'POST':
        userLogin = user.objects.get(email = request.POST['username'], password = request.POST['password'])
        print(userLogin)
        if (userLogin):
            messages.success(request, "User Logged in successfully")
            return render(request, 'index.html')
        else:
            messages.error(request,'User not found please recheck your credentials')
    return render(request, 'login.html', dictV)

def ContactUs(request):
    if request.method == 'POST':
        newQuery = contactUs(name = request.POST['name'], phone = request.POST['phone'], email = request.POST['email'], country = request.POST['country'], subject = request.POST['subject'])
        newQuery.save()
        messages.success(request, "Your contact information has been successfully saved.")
        return render(request, 'index.html')
    return render(request, 'contact-us.html')
