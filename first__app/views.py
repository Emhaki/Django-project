from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Tree, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm, TreeForm

# Create your views here.
def intro(request):

    return render(request, "posts/intro.html")

def base(request):
    # 작성된 메시지 갯수
    comment = Comment.objects.all()
    comment_message = comment.count()

    context = {
        "comment_message": comment_message,
    }
    return render(request, "posts/base.html", context)


@login_required
def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Comment.objects.all()
    # 작성된 메시지 갯수
    post_message = posts.count()
    

    # 2. template에 보내준다.
    context = {
        "posts": posts,
        "post_message": post_message,
    }

    return render(request, "posts/index.html", context)


def main(request):

    comment_form = CommentForm()

    oduck = False
    santaoduck = False
    comment = Comment.objects.order_by("pk")
    # 작성된 메시지 갯수
    comment_message = comment.count()

    # 상점에서 3개짜리를 샀을 때, 코인이 3개보다 많을 때
    # 3개보다 적을때 경고 알림을 주는 elif 문 삽입해야할듯
    if (
        Comment.objects.filter(coin=1).count() >= 0
        and request.method == "POST"
        and request.POST.get("price-3")
    ):

        for _ in range(3):
            c = Comment.objects.order_by("coin").values()[0]

            for k, v in c.items():
                if k == "id":
                    id_key = c[k]
            comment = Comment.objects.get(id=id_key)
            comment.coin = 2
            comment.save()
            santaoduck = True

    # 상점에서 1개짜리를 샀을 때, 코인이 1개보다 많을 때
    if (
        Comment.objects.filter(coin=1).count() >= 1
        and request.method == "POST"
        and request.POST.get("price-1")
    ):

        c = Comment.objects.order_by("-coin").values()[0]

        for k, v in c.items():
            if k == "id":
                id_key = c[k]

            comment = Comment.objects.get(id=id_key)
            comment.coin = 1
            comment.save()
            oduck = True

    # 코인값이 1인 것들(남은돈)을 카운트
    coin = Comment.objects.filter(coin=1).count()

    context = {
        "coin": coin,
        "comment_message": comment_message,
        "comment_form": comment_form,
        "oduck": oduck,
        "santaoduck": santaoduck,
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


def create(request, user_pk):

    comments = Comment.objects.all()
    comment_message = comments.count()

    if request.method == "POST":
      tree_form = TreeForm(request.POST)
      if tree_form.is_valid():
        tree = tree_form.save(commit=False)
        tree.user = request.user
        tree.save()
        messages.success(request, "트리가 생성됐어요!")
        return redirect("posts:user_tree", user_pk)
    else:
      tree_form = TreeForm()
      
    # comment_form = CommentForm(request.POST)

    # if comment_form.is_valid():
    #     comment = comment_form.save(commit=False)
    #     comment.user = request.user
    #     messages.success(request, "마음이 전달됐어요!")
    #     comment.save()
    #     return redirect("posts:main")
    

    context = {
        "comments": comments,
        "comment_message": comment_message,
        "tree_form":tree_form,
    }
    return render(request, 'posts/create.html', context)

# def tree(request):
#   if request.method == 'POST':
#     tree_form = TreeForm(request.POST)
#     if tree_form.is_valid():
#       tree = tree_form.save(commit=False)
#       tree.user = request.user
#       messages.success(request, "트리가 만들어졌어요!")
#       tree.save()
#       return redirect('posts:user_tree')

def user_tree(request, user_pk):

  return render(request, 'posts/user_tree.html')

def user_tree_create(request, user_pk):

  tree = get_object_or_404(Tree, pk=user_pk)
  if request.method == "POST":
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.tree = tree
      comment.user = request.user
      # messages.success(request, "마음이 전달됐어요!")
      comment.save()
      return redirect('posts:user_tree', user_pk)
  else:
    comment_form = CommentForm()

  context = {
    "comment_form": comment_form,
  }

  return render(request, 'posts/user_tree_create.html', context)


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



def comment_create(request, user_pk):

    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
      comment_form = CommentForm(request.POST)
    
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)

          # if request.user != get_object_or_404(get_user_model(), username=username):
          # 요청된 유저가 어나니머스 라면
          print(comment)
          print("입니다.")
          comment.save()
    
    context = {
      "user": user,
    }
    return render(request, 'posts/main.html', context)

def user_main(request, pk):
  if request.user.is_authenticated:
    user = get_object_or_404(get_user_model(), pk=pk)
    comment = Comment.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment_forms = comment_form.save(commit=False)
      comment_forms.comment = comment
      comment_forms.save()
    return redirect("posts:main", pk)
  else:
    messages.warning(request, "마음을 전달하기 위해선 로그인이 필요합니다.")
    return redirect("accounts:login")
  
  

#  오류 페이지
# def page_not_found(request, exception):

#     return render(request, "404.html", status=404)
