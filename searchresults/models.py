from django.db import models


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=64)
    recipe = models.CharField(max_length=8196)
    image = models.CharField(max_length=256)

    def __str__(self):
        return self.recipe_name
