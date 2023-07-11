from django.db import models
import uuid
# Create your models here.

class Menu(models.Model):
    tag = models.OneToOneField('Tag', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=300)
    price = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='menu_images')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name