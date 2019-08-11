import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from .schema import schema
from .forms import SignUpForm, ProfileForm
from . import queries
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.

def apply(request):

    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            u = user_form.save()
            pf = profile_form.save(commit=False)
            pf.user = u
            pf.save()

            Subject = "Thank you!"
            from_email = "citrushack@gmail.com"
            to_email = user_form.cleaned_data.get('email')
            message = 'Hey ' + str(profile_form.cleaned_data.get('first_name')) + ', Thanks for applying to Cutie Hack 2019. We will be sending out decisions in month, so stay tuned. '


            send_mail(Subject, message , from_email, [to_email],fail_silently=False)

            result = queries.getProfile(email=user_form.cleaned_data.get('email'))
            if result.data:
                return JsonResponse(result.data)
            else:
                if result.errors:
                    return JsonResponse(result.errors)
        return JsonResponse({"Error":"The backend has concked out. Get Aditya on the line."})
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})
    # return render(request, 'dummyapply.html', {'user_form': user_form, 'profile_form': profile_form})

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


def login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        #login function
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({"Success":True})
        else:
            return JsonResponse({"success":False})


        #if the login is successful, return a json that says that success is true, or the profile. If login fails, return success = false

        # return JsonResponse({"Meme":True})
        #or
        # result = queries.getProfile(email=email)
        # return JsonResponse(result.data)


    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})
    # return render(request, 'login.html')



def email(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        result = queries.getUser(email=email)
        if result.data:
            return JsonResponse({"Succ":False})


    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})



def passwordReset(request):



    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})
