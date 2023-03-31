from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product

class PostProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user1 = User.objects.create_user(
            username='testuser1',
            email='testuser1@gmail.com',
            password='Password#1',
        )

        test_user1.save

        # Create a product
        test_product1 = Product.objects.create(
            seller=test_user1,
            name='Dutch designer Ward Wijnant',
            description='explores sawing techniques resulting in geometric patchworks that make the wood grains pop in his BLEND collection.',
            image='images/chair1.jpg',
            category='Furniture',
            old_price=18000,
            new_price=15000,
        )

        test_product1.save

    def testPostProduct(self):
        product = Product.objects.get(id=1)

        seller = f'{product.seller}'
        name = f'{product.name}'
        description = f'{product.description}'
        image = f'{product.image}'
        category = f'{product.category}'
        old_price = product.old_price
        new_price = product.new_price

        self.assertEqual(seller, 'testuser1')
        self.assertEqual(name, 'Dutch designer Ward Wijnant')
        self.assertEqual(description, 'explores sawing techniques resulting in geometric patchworks that make the wood grains pop in his BLEND collection.')
        self.assertEqual(image, 'images/chair1.jpg')
        self.assertEqual(category, 'Furniture')
        self.assertEqual(old_price, 18000)
        self.assertEqual(new_price, 15000)