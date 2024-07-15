from django.urls import path
from .views import IndexView
from hexlet_django_blog.article import views

urlpatterns = [
    path('', IndexView.as_view()),
]