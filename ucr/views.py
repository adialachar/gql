import json
from django.shortcuts import render
from django.http import JsonResponse
from .schema import schema
from .forms import SignUpForm, ProfileForm
from . import queries
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):

    #return render(request, 'index.html', context={})
    print("Hello my baby")

    if request.method == 'POST':
        print(request.POST.get('Username',-1))
        print(request.POST.get('Email',-1))
        print(request.POST.get('Password',-1))
        print(request.body)
        print("HIIIII")

        return JsonResponse({"Success":True})

    else:
        return JsonResponse({"Success":False})




    query0 = """
        query{
            users{
                email,
                password
            }

        }

        """

    email = "aacha002@ucr.edu"
    query1 = """
    query getProfile($email: String){
            profile(email:$email){
                firstName,
                lastName

            }
        }
        """




    query2 = """
        query{
        profile{
        user(email:"aacha002@ucr.edu"){

                    password
                }
                firstName,
                lastName

            }

        }
            """


    query3 = """
        query{
        user(email:"aacha002@ucr.edu"){
                id,
                password


            }

        }
            """


    mutation0 = """
    mutation createUserAndProfile($email: String, $password: String, $firstName: String, $lastName: String){
                createUser(email: $email, password: $password, firstName:$firstName, lastName:$lastName){

                    user{

                        email,
                        password

                        }

                        profile{

                            firstName,
                            lastName



                        }


                }





                }
                """





    result = schema.execute(mutation0, variables={'email':"dna003@ucr.edu",'password':"password",'firstName':"Daniel",'lastName':"Na"},)
    #result = schema.execute(query0)
    if result.data:
        return JsonResponse(result.data)
    else:
        print(result.errors)
        return JsonResponse({"Success":False})
    #return JsonResponse({"Success":True})



def dummyapply(request):


    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print("HIIIIIII")
            result = queries.getProfile(email=user_form.cleaned_data.get('email'))
            print(result)
            if result.data:
                return JsonResponse(result.data)
            else:
                print(result.errors)
                if result.errors:
                    return JsonResponse(result.errors)
        return JsonResponse({"Success":False})

    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()

    return render(request, 'dummyapply.html', context={'user_form': user_form, 'profile_form': profile_form})

        #
        #
        # result = queries.getProfile({'email':email})
        #
        # if result.data:
        #     return JsonResponse()
        # else:
        #     return JsonResponse(result.errors)






