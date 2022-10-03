from cgitb import handler
from django.urls import path
from . import views


# domain.com/first_app/simple_view

"""
메인(R): 게시글의 목록(/posts/) / 게시글 상세
작성(C): 글을 작성하는 페이지(/posts/new/) / 작성 완료
수정(U): 글을 수정하는 페이지 / 수정 완료
삭제(D): 글 삭제 완료
"""

app_name = "posts"

urlpatterns = [
    path("", views.main, name="main"),
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
    path("edit/<int:pk_>", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("update/<int:pk_>", views.update, name="update"),
    path("index/", views.index, name="index"),
    path("deco/", views.deco, name="decoration"),
]

# handler404 = "my__site.page_not_found"
