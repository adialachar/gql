from django.shortcuts import render
from django.http import JsonResponse
from .schema import schema
# Create your views here.


def index(request):

    #return render(request, 'index.html', context={})
    query = '''
        query{
            users{
                name,
                lastName
            }

        }

        '''
    result = schema.execute(query)


    return JsonResponse(result.data)
