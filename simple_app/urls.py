from django.conf.urls import url
from simple_app import views

# step 3 - make urls for the html to render -> go app/views

urlpatterns = [
    url('^$', views.HomePageView.as_view()),
    url('^about/$', views.AboutPageView.as_view()),
]
