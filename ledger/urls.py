from django.urls import path

from .views import *

urlpatterns = {
    path('', index, name="index"),
    path('recipes/list', recipes_list, name='recipes'),
    path('recipe/', recipe, name='recipe'),
}

app_name="ledger"