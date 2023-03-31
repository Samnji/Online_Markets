from django.db import models
from django.contrib.auth.models import User

FURNITURE_CHOICES = (
    ('TVs & Audio', 'TVs & Audio'),
    ('Phones & Tablets', 'Phones & Tablets'),
    ('Fashion', 'Fashion'),
    ('Gaming', 'Gaming'),
    ('Health & Beauty','Health & Beauty'),
    ('Appliances', 'Appliances'),
    ('Computing', 'Computing'),
    ('Baby Products', 'Baby Products'),
    ('Sporting Goods','Sporting Goods'),
    ('Furniture','Furniture'),
)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    image = models.ImageField(upload_to="images/")
    category = models.CharField(choices=FURNITURE_CHOICES, max_length=20)
    old_price = models.PositiveIntegerField(null=True, blank=True)
    new_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
