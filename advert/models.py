from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

FURNITURE_CHOICES = (
    ('TV & Audio', 'TV & Audio'),
    ('Phones & Tablet', 'Phones & Tablet'),
    ('Fashion', 'Fashion'),
    ('Gaming', 'Gaming'),
    ('Health & Beauty','Health & Beauty'),
    ('Appliance', 'Appliance'),
    ('Computing', 'Computing'),
    ('Baby Product', 'Baby Product'),
    ('Sporting Good','Sporting Good'),
    ('Furniture','Furniture'),
)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    image = models.ImageField(upload_to="images/")
    category = models.CharField(choices=FURNITURE_CHOICES, max_length=50)
    old_price = models.PositiveIntegerField(null=True, blank=True)
    new_price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class ProductOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.quantity} {self.product.name}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductOrder)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
