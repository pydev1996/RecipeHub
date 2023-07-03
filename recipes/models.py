from django.contrib.auth.models import User
from django.db import models

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} - {self.recipe.recipe_name}'


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('veg', 'Vegetarian'),
        ('Non-veg', 'Non-Vegetarian'),
        ('Breakfast', 'Breakfast'),
        ('Snacks', 'Snacks'),
        ('Rice', 'Rice'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    processtime=models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='veg')
    likes = models.IntegerField(default=0)
    youtube_links = models.URLField(default='', max_length=200)



    def __str__(self):
        return self.recipe_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name