"""ReferProject URL Configuration

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
from django.urls import path
from testapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_View,name="home"),
    path('upi/',views.Upi_View,name="upi"),
    path('crypto/',views.Crypto_View,name="crypto"),
    path('stock/',views.Stock_View,name="stock"),
    path('rummy/',views.Rummy_View,name="rummy"),
    path('(?p<year>\d{4})/(?p<month>\d{2})/(?p<day>\d{2})/(?p<app>[-\w]+)/$',views.app_detail_view,name='app_detail')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
