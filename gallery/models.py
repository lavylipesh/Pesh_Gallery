from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    def save_category(self):
        self.save()
    @classmethod
    def search_by_name(cls,search_term):
        category = cls.object.filter(title_icontains = search_term)
        return category

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name 

class Image(models.Model):
    image = models.ImageField(upload_to = 'categories/')
    image_name = models.CharField(max_length = 60)
    image_description = models.CharField(max_length=60)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    