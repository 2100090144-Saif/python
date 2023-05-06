import datetime
import requests
import qrcode
from django.contrib import auth, messages
from django.contrib.auth.models import User


from .models import datetime1
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import contactus
from .models import reguser
from django.contrib.auth import authenticate
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, UserProfileForm

def home(request):
    return HttpResponse("Hello world example of PFSD Django framework")




def function1(request):
    return render(request, 'p1.html')


# def function2(request):
#     var1 = datetime.datetime.now()
#     data = datetime1(time12=var1)
#     data.save()
#     return HttpResponse(var1)

#temprature
# def city(request):
#     return render(request, 'tempcity.html')
# def temp(request):
#     city1 = request.POST.get('city')
#
#     api_key = 'fbdcb3297c21556bdbaf6445e3d56559'
#     weather_data = requests.get(
#         f"https://api.openweathermap.org/data/2.5/weather?q={city1}&units=imperial&APPID={api_key}")
#
#     if weather_data.json()['cod'] == '404':
#         return HttpResponse("Not found")
#     else:
#         weather = weather_data.json()['weather'][0]['main']
#         temp = round(weather_data.json()['main']['temp'])
#         # °C = [(°F-32)×5] / 9
#         temp1 = (((temp - 32) * 5) / 9)
#         # print(type(temp))
#         return HttpResponse(f"temperature of {city1} is {temp}ºF or {temp1}ºC")

#qr-code
# def qrcode1(request):
#     return render(request, 'qrcode1.html')
#
#
# def qrcode12(request):
#     if request.method == 'POST':
#         sid = request.POST.get('sid')
#         sname = request.POST.get('sname')
#         data1 = sid+sname
#         qr = qrcode.QRCode(version=1, box_size=30, border=5)
#         qr.add_data(data1)
#         qr.make(fit=True)
#         img = qr.make_image(fill_color='black', back_color='white')
#         img.save('static/images/klu.png')
#         img1 = open('static/images/klu.png', 'rb')
#         response = FileResponse(img1)
#         return response
#     else:
#         return HttpResponse("not working")



def contactus1(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment+'\n\n--------------------------Thanks for your feedback--------------------------'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        send_mail(
            'Thank you for contacting AgriTech System',
            tosend,
            '2100090144csit@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail sent</center></h1>")
    else:
        HttpResponse("<h1>error</h1>")



def function3(request):
    return render(request, 'contactus.html')


def registeruser(request):
    return render(request, 'register.html')


def register(request):
    '''user_form = SignupForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)
        user.set_password(user.password)
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()'''
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        #data1 = reguser(name=name,email=email,password=password)
        #data1.save()
        user = User.objects.create_user(username=name, password=password, email=email)
        user.save()
        return HttpResponse("<h1><center>Register succeessfully please login again</center></h1>")
    else:
        HttpResponse("<h1>error</h1>")


def loginuser(request):
    return render(request, 'login1.html')


def loggedin(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("<h1><center>login success</center></h1>")
        else:
            messages.info(request, 'invalid username or password')
            return redirect('loginu')
    else:
        HttpResponse("<h1>error</h1>")



