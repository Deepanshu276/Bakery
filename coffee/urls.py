from django.contrib import admin
from django.urls import path, include
from coffee_shop import views as coffeeshop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('coffee_shop.urls')),
    path('account/', include('users_app.urls')),
    path('', coffeeshop_views.home, name='home'),
    path('order', coffeeshop_views.order, name='order'),
    path('contact', coffeeshop_views.contact, name='contact'),
    path('pricing', coffeeshop_views.pricing, name='pricing'),
    path('cake', coffeeshop_views.cake, name='cake')

]
