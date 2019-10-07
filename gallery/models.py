from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name 

class Image(models.Model):
    image = models.ImageField(upload_to 'static/')
    name = models.CharField(max_length = 60)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    