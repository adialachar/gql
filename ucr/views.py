import json
from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from .schema import schema
from .forms import SignUpForm, ProfileForm
from .models import MyUser, Profile
from . import queries
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import ast

from rest_framework import viewsets
from .serializers import MyUserSerializer
from django.core.mail import EmailMessage
from rest_framework.views import APIView

import jwt


class MyUserView(viewsets.ModelViewSet, APIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

# Create your views here.

@csrf_exempt
def profile(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        result = queries.getProfile(email)
        if result.data:
                return JsonResponse(result.data)
        else:
            print(result.errors)
            return JsonResponse({"Error":"The backend has concked out. It is likely the user doesn't exist. Get Aditya on the line."})


    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})

@csrf_exempt
def login(request):

    if request.method == 'POST':

        # email = request.POST.get('email')
        # password = request.POST.get('password')
        data = json.loads(request.body)
        print(data)
        email = data['user']['email']
        password = data['user']['password']
        print(email)
        print(password)
        #login function
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)

            token = jwt.encode({'user':email}, "SECRET_KEY")
            try:
                decToken = jwt.decode(token, "SECRET_KEY")
            except:
                return JsonResponse({"ur mom": "gei"})

            result = queries.getProfile(email)


            profile_data = json.loads(json.dumps(result.data))
            print(profile_data)
            print(type(profile_data))
            print(token)
            token = token.decode('utf-8')


            return JsonResponse({'user':profile_data, 'jwt':token})

            return JsonResponse({"Success":True})
        else:
            return JsonResponse({"success":False})


    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})





def send_email(subject, body, to):
    email = EmailMessage(subject, body, 'citrushack@gmail.com', to)
    email.send(fail_silently=False)


@csrf_exempt
def email(request):

    if request.method == 'POST':
        print("HELLO")
        data = json.loads(request.body)
        print(data)
        email_addy = data['email']
        result = queries.getUserAndProfile(email=email_addy)
        if result.errors:
            print(result.errors)
            return JsonResponse({"lmao":"heres your issue"})
        if result.data:
            subject = "Thank you for applying to Cutie Hack 2019!"
            body = "Thank you for applying to Cutie Hack this fall. Make sure to check this email for updates from us. We hope to see you there! \n \n Sincerely, \n The Cutie Hack Team"
            send_email(subject=subject, body=body, to=[email_addy])

            return JsonResponse({"Status":"Successfully sent email"})



    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})



def passwordReset(request):



    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})




@csrf_exempt
def validateToken(request):

    token = None
    if 'Authorization' in request.headers:
        print("HEWWO")
        token = request.headers['Authorization']
        print(token)
        token = token.encode('utf-8')
        print(token)

    if not token:
        return JsonResponse({'message':'Token is missing'}), 403

    try:
        decToken = jwt.decode(token, "SECRET_KEY")
    except:
        return JsonResponse({"Error": "Invalid Token"})
    print(decToken)
    email_addy = decToken['user']

    result = queries.getProfile(email_addy)

    if result.data:
        return JsonResponse({'user':result.data})
    else:
        return JsonResponse({"Error":"User does not exist"})


