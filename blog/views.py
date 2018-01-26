from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html",{'posts': posts})

def show(request, id):
    post = Post.objects.get(id = id)
    return render(request, "show.html",{'post': post})

def new(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']
        post = Post(title=title,body=body)
        post.save()
        return redirect('/posts') 
    else:
        return render(request, 'new.html')

def update(request, id):
    if(request.method == 'POST'):
        post = Post.objects.get(id = id)        
        title = request.POST['title']
        body = request.POST['body']
        post.title = title
        post.body = post.body
        post.save()
        return redirect('/posts')
    else:
        post = Post.objects.get(id = id)        
        return render(request, 'edit.html',{'post': post})

def delete(request, id):
    if(request.method == 'POST'):
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('/posts')
    else:
        return redirect(f'/posts/{id}')