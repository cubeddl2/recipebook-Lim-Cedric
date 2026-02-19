from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('recipes_list', args=[str(self.name)])

class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredients")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")

