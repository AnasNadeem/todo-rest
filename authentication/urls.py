from django.urls import path
from authentication.views import RegisterAPiView, LoginApiView

urlpatterns = [
    path('register', RegisterAPiView.as_view()),
    path('login', LoginApiView.as_view()),
]