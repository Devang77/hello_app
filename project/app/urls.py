from django.urls import path,include
from .views import Hello
urlpatterns = [
    path('hello/', Hello.as_view()),
]