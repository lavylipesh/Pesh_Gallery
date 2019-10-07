from django.test import TestCase
from .models import Category,Location,Image

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.animation= Category(name = 'Animations')
   
   def test_instance(self):
        self.assertTrue(isinstance(self.animation,Category))
    
    
    def test_save_method(self):
        self.animation.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class LocationTestClass(models.Model):
    def setUp(self):
         
        self.category= Category(name = 'Animations')
        self.animation.save_animation()

     
        self.new_image = image(name = 'image')
        self.new_image.save()

        self.new_location= Location(title = 'Test Location',post = 'This is a random test Post',category = self.animation)
        self.new_location.save()

        self.new_location.category.add(self.new_category)

    def tearDown(self):
        Category.objects.all().delete()
        image.objects.all().delete()
        Location.objects.all().delete()
    



