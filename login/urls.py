from django.urls import path
from login.views import LoginFromView, LogoutView

urlpatterns = [
    path('', LoginFromView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),


]