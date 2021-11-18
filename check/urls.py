from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from check import views as user_views
from .forms import CustomAuthForm

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='check/login.html', redirect_authenticated_user = True, authentication_form=CustomAuthForm), name = 'login-login'),
	path('check/', views.check, name = 'mydb'),
	path('submitted/', views.submitted, name = 'submitted'),
]