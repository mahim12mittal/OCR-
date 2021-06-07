from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutocr', views.aboutocr, name='aboutocr'),
    # path('/request_page', views.request_page, name='request_page')
]
