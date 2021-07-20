from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html', 
                                    authentication_form=CustomLoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name=''), name='logout'),
]
