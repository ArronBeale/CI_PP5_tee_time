# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
# Internal:
from .models import Product, Category
from .forms import ProductForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestViews(TestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@email.com'
        )
        self.user.is_superuser = True
        self.user.save()

        # Create test category
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Category'
        )
        # Create test product
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
        self.user.delete()

    def test_all_products_view(self):
        # Test that all_products view is accessible
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_detail_view(self):
        # Test that product_detail view is accessible
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_view(self):
        # Test that add_product view is accessible and form is displayed
        url = reverse('add_product')
        login = self.client.login(
            username='test_user', password='test_password')
        self.assertTrue(login)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form'], ProductForm)

    def test_add_product_view_submission(self):
        # Test that add_product view correctly handles form submission
        url = reverse('add_product')
        login = self.client.login(
            username='test_user',
            password='test_password'
            )
        self.assertTrue(login)
        data = {
            'code': 'new_product',
            'brand': 'New Brand',
            'name': 'New Product',
            'description': 'New product description',
            'has_sizes': True,
            'price': 99.99,
            'category': self.category,
            'rating': 4.3,
        }
        response = self.client.post(url, data)
        # Check that the view redirects to the product detail page
        self.assertEqual(response.status_code, 200)

    def test_delete_product_view(self):
        # Test that delete_product view correctly handles form submission
        url = reverse('delete_product', args=[self.product.id])
        login = self.client.login(
            username='test_user',
            password='test_password'
            )
        self.assertTrue(login)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        # Check that product is no longer in database
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
