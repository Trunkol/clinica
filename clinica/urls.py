"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import SignUpView

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout', auth_views.logout_then_login, name="logout"),
    path('register/', SignUpView.as_view(), name='signup'),
    path('', include('core.urls')),
    path("select2/", include("django_select2.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }), url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }), ]

