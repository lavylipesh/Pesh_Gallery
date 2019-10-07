from django.test import TestCase
from .models import Category,Location,Image

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.animation= Category(name = 'Animatons')
    def test_instance(self):
        self.assertTrue(isinstance(self.animation,Category))
    def test_save_method(self):
        self.animations.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(editors) > 0)       



