from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)
    

    def __str__(self):
        return self.name
    def save_category(self):
        self.save()
    

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name 

class Image(models.Model):
    my_image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_description = models.CharField(max_length=60)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
   
    @classmethod
    def search_by_category(cls,search_term):
        name = cls.objects.filter(category__name__icontains = search_term)
        return name