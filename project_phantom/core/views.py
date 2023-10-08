from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 #Esta libreria hace que si se intenta bucar un objeto que no existe, de un error 404.
from .forms import CustomUserCreationForm, GameCategoryForm
from .models import GameCategory


# Create your views here.
# creamos la pagina de inicio
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirige al home o a donde desees después de registrar al usuario
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') # Redirige al home al usuario una vez se de al boton de logout

def create_game_category(request):
    if request.method == 'POST':
        form = GameCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_categories')
    else:
        form = GameCategoryForm()
    return render(request, 'create_game_category.html', {'form': form})


def edit_game_category(request, pk):
    category = get_object_or_404(GameCategory, pk=pk)
    if request.method == 'POST':
        form = GameCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('game_categories')
    else:
        form = GameCategoryForm(instance=category)
    return render(request, 'edit_game_category.html', {'form': form, 'category': category}) #mostrar y permitir la edición de la categoría de juego.


def delete_game_category(request, pk):
    category = get_object_or_404(GameCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('game_categories')
    return render(request, 'delete_game_category.html', {'category': category})

def game_categories(request):
    categories = GameCategory.objects.all()
    return render (request, 'game_categories.html', {'categories': categories})






