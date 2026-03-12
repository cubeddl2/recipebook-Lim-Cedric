from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('recipes/list', RecipesListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view(), name='add_image')
]

app_name = "ledger"
