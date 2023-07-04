from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
# Create your views here.
def url_views(request):
    print('url_views()')
    data = {'code':'001', 'msg':'ok'}
    return HttpResponse('<h1>url_views</h1>')
    #return JsonResponse(data) 

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username:{username}')
    print(f'request.GET:{request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method:{request.method}')

    if request.method =='GET':
        print(f'request.GET: {request.GET}')
    if request.method =='POST':
        print(f'request.POST:{request.POST}')
    return render(request,'view.html')