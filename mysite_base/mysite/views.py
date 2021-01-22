from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    tmplate_name = "home.html"