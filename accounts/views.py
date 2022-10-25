from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# 로그인 페이지


def signup(request):
    # POST 요청 처리
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # UserCreationForm은 ModelForm을 상속받음
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("posts:main")

    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


# 로그인이 안되어있으면 접속 불가
@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }

    return render(request, "accounts/detail.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect("posts:main")
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

        return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("accounts:login")
