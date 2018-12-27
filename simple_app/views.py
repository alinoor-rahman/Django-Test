from django.shortcuts import render
from django.views.generic import TemplateView

# step 4 - define views -> make templates in app and define htmls


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"
