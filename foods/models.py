from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telegram_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = ['username']
    

    def __str__(self) -> str:
        try:
            return self.username
        except ValueError:
            return self.telegram_id

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title
    

class SubCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"
        ordering = ['title']
    
    def __str__(self) -> str:
        return self.title

class Food(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name
