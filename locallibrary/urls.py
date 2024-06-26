"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# Added for the catalog app
from django.urls import include

# Added to redirect the root URL
from django.views.generic import RedirectView

# Added to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Added for the catalog app
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Added for the base URL change 
urlpatterns += [
    path('',RedirectView.as_view(url='catalog/', permanent=True)),
]

# Added for the static files 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
