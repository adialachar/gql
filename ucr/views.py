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


    query1 = '''
        query{
            profiles{
                user{
                    email,
                    password

                }
                firstName,
                lastName
            }
        }
        '''

    query2 = """
        query{
        profiles(firstName:"Daniel"){
                user{
                    email,
                    password
                }
                lastName

            }

        }
            """


    result = schema.execute(query1)

    if result.data:
        return JsonResponse(result.data)
    else:
        print(result.errors)
        return JsonResponse({"Success":False})
    #return JsonResponse({"Success":True})
