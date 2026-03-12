from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import RecipeIngredient, Recipe, RecipeImage, Profile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, FormView, UpdateView

def index(request):
    return HttpResponse('Hello World! This came from the index view')

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)

def recipe(request, id):
    ctx = {'recipe', RecipeIngredient.objects.get(id=id)}
    return render(request, "ledger/recipe.html", ctx)

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'accounts/login'

class RecipesListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name']
    template_name = 'ledger/recipe_add.html'

    def form_valid(self,form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'ledger/recipe_image_add.html'

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={'pk': self.kwargs['pk']})
