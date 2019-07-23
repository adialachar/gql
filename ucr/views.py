import json
from django.shortcuts import render
from django.http import JsonResponse
from .schema import schema
# Create your views here.


def index(request):

    #return render(request, 'index.html', context={})
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

    result = schema.execute(query1, variables={'email':"aacha002@ucr.edu"},)
    #result = schema.execute(query0)
    if result.data:
        return JsonResponse(result.data)
    else:
        print(result.errors)
        return JsonResponse({"Success":False})
    #return JsonResponse({"Success":True})
