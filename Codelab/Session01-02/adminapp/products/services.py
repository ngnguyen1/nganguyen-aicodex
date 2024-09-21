from products.repositories import ProductRepository
from products.models import Product  # Import the Product class
from products.dtos import ProductDTO

class ProductService:
    @staticmethod
    def get_all_products():
        return ProductRepository.get_all()

    @staticmethod
    def get_product_by_id(product_id):
        product = ProductRepository.get_by_id(product_id)
        if product:
            return ProductDTO(product.id, product.name, product.price, product.picture, product.description)
        return None

    @staticmethod
    def create_product(name, price, description=None):
        product = Product(name=name, price=price, description=description)
        ProductRepository.create(product)
        return product

    @staticmethod
    def update_product(product_id, name, price, picture, description=None):
        product = ProductRepository.get_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            product.picture = picture
            product.description = description
            ProductRepository.update()
            return product
        return None

    @staticmethod
    def update_product_picture(product_id, file_path):
        product = ProductRepository.get_by_id(product_id)
        if product:
            product.picture = file_path
            ProductRepository.update()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_by_id(product_id)
        if product:
            ProductRepository.delete(product)
            return True
        return False