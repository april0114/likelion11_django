from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .forms import PostBaseForm
from .models import Post



def index(request):
    post_list = Post.objects.all().order_by('created_at') #post 전체 데이터 조회
    context = {
        'post_list':post_list,
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    post_list = Post.objects.filter(writer=request.user)
    context = {
        'post_list' : post_list,
    }
    return render(request, 'posts/post_list.html',context)

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post':post,
    }
    return render(request, 'posts/post_detail.html')

def post_confirm_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

@login_required
def post_create_view(request):
    if request.method =='GET':
        return render(reqeust, 'posts/post_form.html')
    else:
        image =request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user
        )
    return redirect('index')


def post_create_form_view(request):
    if request.method =='GET':
        form= PostBaseForm()
        context = {
            'form':form
        }
        return render(request, 'posts/post_form.html',context)
    else:
      #  Post.objects.create(
      #      image=image,
      #      content=content,
      #      writer=request.user
      #  )
        return redirect('index')

@login_required
def post_update_view(request, id):
    post  = get_object_or_404(Post, id=id, writer=request.user)
    return render(request, 'posts/post_form.html')



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

