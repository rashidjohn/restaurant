from django.db import models
import uuid

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    lavozim = models.CharField(max_length=300)
    social_facebook = models.CharField(max_length=400, blank=True, null=True)
    social_youtube = models.CharField(max_length=400, blank=True, null=True)
    social_instagram = models.CharField(max_length=400, blank=True, null=True)
    image = models.ImageField(upload_to='team_images')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date = models.DateTimeField()
    people = models.PositiveIntegerField()
    message = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __Str__(self):
        return self.name

