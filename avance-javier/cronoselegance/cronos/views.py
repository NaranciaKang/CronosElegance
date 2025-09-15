from django.shortcuts import render, redirect
from .models import Alumno, Producto, Wishlist
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def principal(request):
    obj = Alumno.objects.raw('select * from cronos_alumno')
    context = {
        'data': obj
    }
    return (render(request, 'index.html',context))


def toggle_wishlist(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    wishlist_item, created = Wishlist.objects.get_or_create(usuario=request.user, producto=producto)

    if not created:  
        wishlist_item.delete()
        return JsonResponse({'status': 'removed', 'message': 'Producto eliminado de tu wishlist'})
    
    return JsonResponse({'status': 'added', 'message': 'Producto añadido a tu wishlist'})


def ver_wishlist(request):
    wishlist = Wishlist.objects.filter(usuario=request.user).select_related("producto")
    return render(request, "wishlist.html", {"wishlist": wishlist})


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Autenticar automáticamente después de registrarse
            return redirect("login")  # o a otra página
    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})
