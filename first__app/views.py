from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def base(request):
    # 작성된 메시지 갯수
    posts = Post.objects.all()
    post_message = posts.count()

    context = {
        "post_message": post_message,
    }
    return render(request, "posts/base.html", context)


@login_required
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


@login_required
def main(request):
    # DB에 있는 posting Data는 건드리지 않으면서
    # 구매에 따른 재화 감소 기능

    # 재화를 보여주는 함수
    posts = Post.objects.all()
    # 작성된 메시지 갯수
    post_message = posts.count()

    # 상점에서 3개짜리를 샀을 때
    if request.method == "POST" and request.POST.get("price-3"):

        for _ in range(3):
            c = Post.objects.order_by("coin").values()[0]

            for k, v in c.items():
                if k == "id":
                    id_key = c[k]
            post = Post.objects.get(id=id_key)
            post.coin = 2
            post.save()

    # 상점에서 1개짜리를 샀을 때
    if request.method == "POST" and request.POST.get("price-1"):

        c = Post.objects.order_by("-coin").values()[0]

        for k, v in c.items():
            if k == "id":
                id_key = c[k]

            post = Post.objects.get(id=id_key)
            post.coin = 1
            post.save()

    # 코인값이 1인 것들(남은돈)을 카운트
    coin = Post.objects.filter(coin=1).count()

    context = {
        "coin": coin,
        "post_message": post_message,
    }
    return render(request, "posts/main.html", context)


# 상점
@login_required
def deco(request):
    # 재화를 보여주는 함수
    posts = Post.objects.all()
    num = posts.count()
    cnt = num  # + 글쓸때

    # 작성된 메시지 갯수
    post_message = posts.count()

    # deco에서 안보이게

    context = {
        "coin": cnt,
        "post_message": post_message,
    }

    return render(request, "posts/decoration.html", context)


@login_required
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


@login_required
def new(request):
    # new.html에서 input태그의 name을 받아옴
    # 새로고침시 중복해서 작성되는 오류 발생
    if request.method == "POST" and request.POST.get("title"):
        messages.success(request, "마음이 전달됐어요!")
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

        # elif request.method == "GET":
        #     messages.success(request, "마음이 전달됐어요!")
        #     title = request.GET.get("title")
        #     content = request.GET.get("content")
    # 굳이 new 페이지로 이동할 필요 없어보여서 redirect로 index로 이동
    # return redirect("posts:index")
    return render(request, "posts/new.html", context)


@login_required
def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    post = Post.objects.get(pk=pk_)
    context = {
        "post": post,
    }

    return render(request, "posts/edit.html", context)


@login_required
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


@login_required
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


@login_required
def delete(request, pk):
    # pk에 해당하는 글 삭제

    Post.objects.get(id=pk).delete()

    return redirect("posts:index")


#  오류 페이지
# def page_not_found(request, exception):

#     return render(request, "404.html", status=404)
