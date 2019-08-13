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
# Create your views here.
@csrf_exempt
def apply(request):

    if request.method == 'POST':
        # print(request.body)
        # print("this one is important")
        # print(request.POST)
        # print(type(request.body))
        # b = request.body.decode("utf-8")
        # uz = ast.literal_eval(b)
        # print(repr(uz))
        try:
            #creating user model
            data = json.loads(request.body)
            print(data)
            email = data['email']
            print(email)
            password1 = data['password1']
            print(password1)
            password2 = data['password2']

            first_name = data['first_name']
            last_name = data['last_name']
            school = data['school']

            level_of_study = data['level_of_study']
            graduation_year = data['graduation_year']
            major = data['major']

            gender = data['gender']
            gender_other = data['gender_other']

            date_of_birth = data['date_of_birth']

            race = data['race']
            race_other = data['race_other']
            phone_number = data['phone_number']

            shirt_size = data['shirt_size']
            dietary_restrictions = data['dietary_restrictions']

            linkedin = data['linkedin']
            github = data['github']
            resume = data['resume']

            conduct_box = data['conduct_box']
            share_box = data['share_box']


            if password1 == password2:
                print('passwords match')
                u = MyUser.objects.create_user(email=email, password=password2)

                pf = Profile(first_name=first_name, last_name=last_name, school=school, level_of_study=level_of_study, \
                graduation_year=graduation_year, major=major, gender=gender, gender_other=gender_other, date_of_birth=date_of_birth, \
                race=race, race_other=race_other, phone_number=phone_number, shirt_size=shirt_size, dietary_restrictions=dietary_restrictions, \
                linkedin=linkedin, github=github, resume=resume, conduct_box=conduct_box, share_box=share_box)
                pf.save(commit=False)
                pf.user=u
                pf.save()
            else:
                JsonResponse({"Error": "Passwords do not match"})
        except IntegrityError as e:
            return JsonResponse({"Error": str(e)})
        except Exception as e: 
            return JsonResponse({"Error": str(e)})

        # print("HELLOOOOO")
        #user_form = SignUpForm(json.loads(b))
        # profile_form = ProfileForm(request.POST)
        #print(user_form)
        #if user_form.is_valid(): 
        #    print("good morning vietnam")
             #profile_form.is_valid():
        #    u = user_form.save()
            #pf = profile_form.save(commit=False)
            #pf.user = u
            #pf.save()
        #    print(u)
            # Subject = "Thank you!"
            # from_email = "citrushack@gmail.com"
            # to_email = user_form.cleaned_data.get('email')
            # message = 'Hey ' + str(profile_form.cleaned_data.get('first_name')) + ', Thanks for applying to Cutie Hack 2019. We will be sending out decisions in month, so stay tuned. '

        #    return JsonResponse({"Success":True})
            # send_mail(Subject, message , from_email, [to_email],fail_silently=False)

            # result = queries.getProfile(email=user_form.cleaned_data.get('email'))
            # if result.data:
            #     return JsonResponse(result.data)
            # else:
            #     if result.errors:
            #         return JsonResponse(result.errors)
        # return JsonResponse({"Error":"The backend has concked out. Get Aditya on the line."})
    else:
        print("error")
        # user_form = SignUpForm()
        #profile_form = ProfileForm()
    return JsonResponse({"Error":"Did you send a GET request instead of a POST request?"})
    #return render(request, 'dummyapply.html', {'user_form': user_form})

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
