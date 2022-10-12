from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Post

# Create your views here.
def base(request):
    # 작성된 메시지 갯수
    posts = Post.objects.all()
    post_message = posts.count()

    context = {
        "post_message": post_message,
    }
    return render(request, "posts/base.html", context)


def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 작성된 메시지 갯수
    post_message = posts.count()

    # 2. template에 보내준다.
    context = {
        "posts": posts,
        "post_message": post_message,
    }

    return render(request, "posts/index.html", context)


def main(request):
    # DB에 있는 posting Data는 건드리지 않으면서
    # 구매에 따른 재화 감소 기능

    # 재화를 보여주는 함수
    posts = Post.objects.all()
    # 작성된 메시지 갯수
    post_message = posts.count()
    # coin 포스팅 갯수

    if request.method == "POST" and request.POST.get("price"):

        c = Post.objects.order_by("-coin").values()[0]

        for k, v in c.items():
            if k == "id":
                id_key = c[k]

            post = Post.objects.get(id=id_key)
            post.coin = 1
            post.save()

    # 코인값이 1인 것들(남은돈)을 카운트
    coin = Post.objects.filter(coin=1).count()

    buying = 0

    context = {
        "coin": coin,
        "post_message": post_message,
    }
    return render(request, "posts/main.html", context)


# 상점
def deco(request):
    # 재화를 보여주는 함수
    posts = Post.objects.all()
    num = posts.count()
    cnt = num  # + 글쓸때

    # 작성된 메시지 갯수
    post_message = posts.count()

    context = {
        "coin": cnt,
        "post_message": post_message,
    }

    return render(request, "posts/decoration.html", context)


def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # 작성된 메시지 갯수
            posts = Post.objects.all()
            post_message = posts.count()
            context = {
                "post_message": post_message,
            }
        elif request.method == "GET":
            posts = Post.objects.all()
            post_message = posts.count()
            context = {
                "post_message": post_message,
            }
        return render(request, "posts/create.html", context)
    else:
        return render(request, "posts/create.html")
    # else:
    #     # 오류일때 회원가입 홈페이지로 보여줌
    #     return redirect("posts:login")


def new(request):

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        # 2. DB에 저장
        Post.objects.create(
            title=title,
            content=content,
        )

        context = {
            "title": title,
            "content": content,
        }

    elif request.method == "GET":
        title = request.GET.get("title")
        content = request.GET.get("content")

        # 2. DB에 저장
        Post.objects.create(title=title, content=content)

        context = {
            "title": title,
            "content": content,
        }
    # 굳이 new 페이지로 이동할 필요 없어보여서 redirect로 index로 이동
    # return redirect("posts:index")
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
    posts = Post.objects.all()
    post_message = posts.count()
    context = {
        "post": post,
        "post_message": post_message,
    }
    return render(request, "posts/detail.html", context)


def update(request, pk_):
    # update할 특정 데이터를 불러온다. -> pk_ 를 사용해서

    if request.method == "POST":
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


#  오류 페이지
# def page_not_found(request, exception):

#     return render(request, "404.html", status=404)

# 로그인 페이지


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 회원가입하면 바로 로그인되게끔 할 수 있음
            return redirect("posts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "posts/signup.html", context)


def login(request):

    if request.method == "POST":
        # AuthenticationForm의 특징 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            return redirect("posts:main")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }

    return render(request, "posts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:main")
