from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=0, null=True, blank=True)
    image = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.name, self.price)
    
