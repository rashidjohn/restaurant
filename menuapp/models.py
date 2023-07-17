from django.db import models
import uuid
# Create your models here.

class Menu(models.Model):
    FOOD_TYPE = (
        ('breakfast','breakfast'),
        ('launch','launch'),
        ('dinner','dinner'),
    )
    type = models.CharField(max_length=50, choices=FOOD_TYPE, default='breakfast')

    name = models.CharField(max_length=200)
    info = models.CharField(max_length=300)
    price = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='menu_images')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name