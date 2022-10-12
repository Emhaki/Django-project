from django.shortcuts import redirect, render

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # UserCreationForm은 ModelForm을 상속받음
        if form.is_valid():
            form.save()
            return redirect("posts:main")

    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user": user}

    return render(request, "accounts/detail.html", context)
