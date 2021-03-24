from django.views.generic.base import TemplateView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'homepage/home.html'