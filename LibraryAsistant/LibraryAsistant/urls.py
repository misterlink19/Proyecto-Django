"""LibraryAsistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
from Libreria import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
<<<<<<< HEAD
=======
    path('ConsultaDeLibros/', views.CLibrosView.as_view(), name='CLibros'),
>>>>>>> 8d9d8ac94f1bd17e37a94d6417fad419d53ec7de
    path('admin/', admin.site.urls),
    path('Libreria/', include('Libreria.urls')),
    path('', RedirectView.as_view(url='/Libreria/', permanent=True)),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)