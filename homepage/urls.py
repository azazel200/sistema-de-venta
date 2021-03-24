from django.urls import path
from homepage.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),


]
