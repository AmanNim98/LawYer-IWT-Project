from django.urls import include, path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('login/', views.LoginView, name = 'LoginView' ),
    path('contactUs/', views.ContactUs, name = 'contactUs'),
]