from django.urls import path
from .views import principal
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',principal,name='principal'),
    path('wishlist/toggle/<int:producto_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.ver_wishlist, name='ver_wishlist'),
    # Login con tu HTML "inicio-sesion.html"
    path("login/", auth_views.LoginView.as_view(template_name="inicio-sesion.html"), name="login"),

    # Logout
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Registro con tu HTML "registro.html"
    path("registro/", views.registro, name="registro"),
]



