import unittest
from unittest.mock import patch, MagicMock
from products.repositories import ProductRepository
from products.models import Product
from extensions import db
from flask import Flask
import os
from products.services import ProductService, ProductDTO

class TestProductRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config.from_object('config_test')
        db.init_app(cls.app)
        cls.app.app_context().push()

    @patch('products.repositories.Product.query')
    def test_get_all(self, mock_query):
        mock_query.all.return_value = ['product1', 'product2']
        result = ProductRepository.get_all()
        self.assertEqual(result, ['product1', 'product2'])
        mock_query.all.assert_called_once()

    @patch('products.repositories.Product.query')
    def test_get_by_id(self, mock_query):
        mock_product = MagicMock()
        mock_query.get.return_value = mock_product
        result = ProductRepository.get_by_id(1)
        self.assertEqual(result, mock_product)
        mock_query.get.assert_called_once_with(1)

    @patch('products.repositories.db.session')
    def test_create(self, mock_session):
        mock_product = MagicMock()
        ProductRepository.create(mock_product)
        mock_session.add.assert_called_once_with(mock_product)
        mock_session.commit.assert_called_once()

    @patch('products.repositories.db.session')
    def test_update(self, mock_session):
        ProductRepository.update()
        mock_session.commit.assert_called_once()

    @patch('products.repositories.db.session')
    def test_delete(self, mock_session):
        mock_product = MagicMock()
        ProductRepository.delete(mock_product)
        mock_session.delete.assert_called_once_with(mock_product)
        mock_session.commit.assert_called_once()

class TestProductService(unittest.TestCase):

    @patch('products.services.ProductRepository.get_all')
    def test_get_all_products(self, mock_get_all):
        mock_get_all.return_value = ['product1', 'product2']
        result = ProductService.get_all_products()
        self.assertEqual(result, ['product1', 'product2'])
        mock_get_all.assert_called_once()

    @patch('products.repositories.ProductRepository.get_by_id')
    def test_get_product_by_id(self, mock_get_by_id):
        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = 'Test Product'
        mock_product.price = 100.0
        mock_product.picture = 'test.png'
        mock_product.description = 'Test Description'
        mock_get_by_id.return_value = mock_product

        expected_dto = ProductDTO(1, 'Test Product', 100.0, 'test.png', 'Test Description')
        result = ProductService.get_product_by_id(1)

        print(result)
        self.assertEqual(result, expected_dto)
        mock_get_by_id.assert_called_once_with(1)

    @patch('products.services.ProductRepository.create')
    @patch('products.services.Product')
    def test_create_product(self, mock_product_class, mock_create):
        mock_product = MagicMock()
        mock_product_class.return_value = mock_product
        result = ProductService.create_product('Product1', 100, 'desc')
        self.assertEqual(result, mock_product)
        mock_create.assert_called_once_with(mock_product)
        mock_product_class.assert_called_once_with(name='Product1', price=100, description='desc')

    @patch('products.services.ProductRepository.update')
    @patch('products.services.ProductRepository.get_by_id')
    def test_update_product(self, mock_get_by_id, mock_update):
        mock_product = MagicMock()
        mock_get_by_id.return_value = mock_product
        result = ProductService.update_product(1, 'Product1', 100, 'pic.jpg', 'desc')
        self.assertEqual(result, mock_product)
        self.assertEqual(mock_product.name, 'Product1')
        self.assertEqual(mock_product.price, 100)
        self.assertEqual(mock_product.picture, 'pic.jpg')
        self.assertEqual(mock_product.description, 'desc')
        mock_update.assert_called_once()
        mock_get_by_id.assert_called_once_with(1)

    @patch('products.services.ProductRepository.update')
    @patch('products.services.ProductRepository.get_by_id')
    def test_update_product_picture(self, mock_get_by_id, mock_update):
        mock_product = MagicMock()
        mock_get_by_id.return_value = mock_product
        result = ProductService.update_product_picture(1, 'new_pic.jpg')
        self.assertEqual(result, mock_product)
        self.assertEqual(mock_product.picture, 'new_pic.jpg')
        mock_update.assert_called_once()
        mock_get_by_id.assert_called_once_with(1)

    @patch('products.services.ProductRepository.delete')
    @patch('products.services.ProductRepository.get_by_id')
    def test_delete_product(self, mock_get_by_id, mock_delete):
        mock_product = MagicMock()
        mock_get_by_id.return_value = mock_product
        result = ProductService.delete_product(1)
        self.assertTrue(result)
        mock_delete.assert_called_once_with(mock_product)
        mock_get_by_id.assert_called_once_with(1)
if __name__ == '__main__':
    unittest.main()