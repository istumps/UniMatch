from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
app_name = "core"

urlpatterns = [
    path("",views.index, name = "index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name = "core/login.html", authentication_form=LoginForm), name="login"),


    path('account/', views.account, name='account'),
    path('account/settings/', views.account_settings, name='account_settings'),
    path('logout/', views.logout_view, name='logout'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
