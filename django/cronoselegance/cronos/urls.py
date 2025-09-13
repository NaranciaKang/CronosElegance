from django.urls import path
from .views import principal
from . import views

urlpatterns = [
    path('',principal,name='principal'),
    path('wishlist/toggle/<int:producto_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.ver_wishlist, name='ver_wishlist'),
]
