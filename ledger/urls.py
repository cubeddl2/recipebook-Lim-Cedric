from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('recipes/list', RecipesListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
]

app_name = "ledger"
