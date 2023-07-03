from django.shortcuts import redirect, render
from .models import Product


def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        product = Product(username=username, email=email, password=password, password2=password2)
        product.save()

        return redirect('registro_completo')  # Corrección: Redirigir a la URL 'registro_completo'

    return render(request, 'signup.html')


def login_view(request):
    return render(request, 'login.html')

def validaciones_view(request):
    return render(request, 'validaciones_login.js')

def validacionsig_view(request):
    return render(request, 'validaciones_singup.js')
