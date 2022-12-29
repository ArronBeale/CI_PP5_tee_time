# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from products.models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCategoryModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Category'
        )

    def tearDown(self):
        self.category.delete()

    def test_str_method(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_get_friendly_name(self):
        self.assertEqual(
            self.category.get_friendly_name(),
            self.category.friendly_name
            )


class TestProductModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Category'
        )
        self.product = Product.objects.create(
            code='test',
            brand='Test Brand',
            name='Test Product',
            description='Test description',
            has_sizes=True,
            price=99.99,
            category=self.category,
            rating=4.3,
        )

    def tearDown(self):
        self.product.delete()
        self.category.delete()

    def test_str_method(self):
        self.assertEqual(str(self.product), self.product.name)
