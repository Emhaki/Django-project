from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()

    # 2. template에 보내준다.
    context = {
        "posts": posts,
    }

    return render(request, "posts/index.html", context)


def create(request):

    return render(request, "posts/create.html")


def new(request):
    # 1. parameter로 날라온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 2. DB에 저장
    Post.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }
    return render(request, "posts/new.html", context)


def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    post = Post.objects.get(pk=pk_)
    context = {
        "post": post,
    }

    return render(request, "posts/edit.html", context)


def detail(request, pk_):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다.
    # 불러온 데이터를 변수에 할당
    post = Post.objects.get(pk=pk_)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)


def update(request, pk_):
    # update할 특정 데이터를 불러온다. -> pk_ 를 사용해서
    post = Post.objects.get(pk=pk_)

    title_ = request.GET.get("title")
    content_ = request.GET.get("context")

    # 데이터를 수정
    post.title = title_
    post.content = content_

    # 데이터를 수정한 것을 반영(save)
    post.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect("posts:detail", post.pk)


def delete(request, pk):
    # pk에 해당하는 글 삭제

    Post.objects.get(id=pk).delete()

    return redirect("posts:index")
