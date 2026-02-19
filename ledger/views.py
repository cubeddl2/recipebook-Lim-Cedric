from django.http import HttpResponse
from django.shortcuts import render
from .models import RecipeIngredient, Recipe

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    return HttpResponse('Hello World! This came from the index view')

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)

def recipe(request, id):
    ctx = { 'recipe', RecipeIngredient.objects.get(id=id)}
    return render(request, "ledger/recipe.html", ctx)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'

class RecipesListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'