import json
from django.shortcuts import render
from django.http import JsonResponse
from .schema import schema

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




    query0 = '''
        query{
            users{
                email,
                password
            }

        }

        '''

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
