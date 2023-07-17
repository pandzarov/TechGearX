"""
URL configuration for TechGearX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from TechGearXapp.views import home, register, login, logout, launch, shop, add_post, add_to_cart, cart, \
    remove_from_cart, profile, products, remove_post

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("register/", register, name="register"),
                  path('home/', home, name="home"),
                  path('', home, name="home"),
                  path('login/', login, name="login"),
                  path('logout/', logout, name="logout"),
                  path('launch/', launch, name="launch"),
                  path('shop/', shop, name="shop"),
                  path('shop/add-post', add_post, name="add_post"),
                  path('add_to_cart/<int:post_id>/', add_to_cart, name='add_to_cart'),
                  path('cart/', cart, name='cart'),
                  path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
                  path('profile/', profile, name='profile'),
                  path('products/', products, name='products'),
                  path('remove_post/<int:post_id>/', remove_post, name='remove_post'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
