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
                firstName
                lastName
            }
        }
        '''


    result = schema.execute(query1)


    return JsonResponse(result.data)
    #return JsonResponse({"Success":True})
