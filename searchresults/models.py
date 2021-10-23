from django.db import models


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=64)
    keywords = models.CharField(max_length=4096)
    recipe = models.CharField(max_length=8192)
    image = models.CharField(max_length=256)
    ingredients = models.CharField(max_length=2048)
    preptime = models.CharField(max_length=11)  # prep time = "XXX minutes"|"XX minutes"|"X minutes", X {0-9}
    info = models.CharField(max_length=2048)

    def __str__(self):
        return self.recipe_name
