from turtle import update
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

User = get_user_model()

class Post(models.Model):
    
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    # DB Fields
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    body = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    
    class meta:
        ordering = ("publish",)
        
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass
    
    def __init__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:post_detail", kwargs={"slug": self.slug})
    
        