"""budget_notebook URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from projects import urls
from apps.hungerapps import urls as urlsHunger
from apps.aroundApps import urls as urlsAround


urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include(urls.urlpatterns)),
    
    path('users/', include('apps.users.urls')),
    path('categories/', include('apps.categories.urls')),
    path('products/', include('apps.products.urls')),
    path('carts/', include('apps.carts.urls')),
    path('orders/', include('apps.orders.urls')),
    path('hungerapps/', include(urlsHunger.urlpatterns)),
    path('around/', include(urlsAround.urlpatterns)),
   
    
]
