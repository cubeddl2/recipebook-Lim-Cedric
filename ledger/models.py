from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    shortBio = models.TextField(validators=[MinLengthValidator(255,
                                            "The field must contain at least 255 characters!")])

    def __str__(self):
        return self.user.username

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete = models.CASCADE,
        related_name = "recipe",
        null = True,
        blank = True
    )
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', kwargs={'pk' : self.pk})

    class Meta: 
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
        )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE, 
        related_name="ingredients"
        )

    def __str__(self):
        return '{}x {} from {}'.format(self.quantity, self.ingredient.name, self.recipe.name)

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='media/images/', null=False)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        related_name = "image",
        null = True,
        blank = True
    )
