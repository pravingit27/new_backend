from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    #slug = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100,primary_key=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(null=True,blank=True,upload_to ='post_images')
    created_by = models.ForeignKey('auth.user',related_name='products',on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

class cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{}' .format(self.cart_id)

