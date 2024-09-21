# Test Cases Documentation

## UserService Test Cases

### Test Case 1: Get All Users
- **Test Method**: `test_get_all_users`
- **Description**: Verify that the `get_all_users` method returns all users.
- **Mock**: `UserRepository.get_all`
- **Expected Result**: The method should return a list of users.
- **Assertions**:
  - Check if the result is equal to `['user1', 'user2']`.
  - Verify that `UserRepository.get_all` is called once.

### Test Case 2: Get User by ID
- **Test Method**: `test_get_user_by_id`
- **Description**: Verify that the `get_user_by_id` method returns the correct user by ID.
- **Mock**: `UserRepository.get_by_id`
- **Expected Result**: The method should return the user with the specified ID.
- **Assertions**:
  - Check if the result is equal to the mocked user.
  - Verify that `UserRepository.get_by_id` is called once with the correct ID.

### Test Case 3: Create User
- **Test Method**: `test_create_user`
- **Description**: Verify that the `create_user` method adds a user to the database.
- **Mock**: `UserRepository.create`
- **Expected Result**: The method should add the user to the database and return the created user.
- **Assertions**:
  - Check if `UserRepository.create` is called once with the mocked user.
  - Verify that the returned user has the correct attributes.

### Test Case 4: Update User
- **Test Method**: `test_update_user`
- **Description**: Verify that the `update_user` method updates the user in the database.
- **Mock**: `UserRepository.get_by_id`, `UserRepository.update`
- **Expected Result**: The method should update the user and return the updated user.
- **Assertions**:
  - Check if `UserRepository.get_by_id` is called once with the correct ID.
  - Verify that `UserRepository.update` is called once.
  - Check if the returned user has the updated attributes.

### Test Case 5: Delete User
- **Test Method**: `test_delete_user`
- **Description**: Verify that the `delete_user` method deletes a user from the database.
- **Mock**: `UserRepository.get_by_id`, `UserRepository.delete`
- **Expected Result**: The method should delete the user from the database and return `True`.
- **Assertions**:
  - Check if `UserRepository.get_by_id` is called once with the correct ID.
  - Verify that `UserRepository.delete` is called once with the mocked user.
  - Check if the method returns `True` when the user is deleted.

### Test Case 6: Get User by Email
- **Test Method**: `test_get_user_by_email`
- **Description**: Verify that the `get_user_by_email` method returns the correct user by email.
- **Mock**: `UserRepository.get_by_email`
- **Expected Result**: The method should return the user with the specified email.
- **Assertions**:
  - Check if the result is equal to the mocked user.
  - Verify that `UserRepository.get_by_email` is called once with the correct email.

### Test Case 7: Validate Email
- **Test Method**: `test_is_valid_email`
- **Description**: Verify that the `is_valid_email` method correctly validates email addresses.
- **Expected Result**: The method should return `True` for valid emails and `False` for invalid emails.
- **Assertions**:
  - Check if the method returns `True` for valid emails.
  - Check if the method returns `False` for invalid emails.

## ProductService Test Cases

### Test Case 1: Get All Products
- **Test Method**: `test_get_all_products`
- **Description**: Verify that the `get_all_products` method returns all products.
- **Mock**: `ProductRepository.get_all`
- **Expected Result**: The method should return a list of products.
- **Assertions**:
  - Check if the result is equal to `['product1', 'product2']`.
  - Verify that `ProductRepository.get_all` is called once.

```bash
$ curl -X GET "http://127.0.0.1:5000/products/" -H "accept: application/json"
```

### Test Case 2: Get Product by ID
- **Test Method**: `test_get_product_by_id`
- **Description**: Verify that the `get_product_by_id` method returns the correct product by ID.
- **Mock**: `ProductRepository.get_by_id`
- **Expected Result**: The method should return the product with the specified ID.
- **Assertions**:
  - Check if the result is equal to the mocked product.
  - Verify that `ProductRepository.get_by_id` is called once with the correct ID.

```bash
$ curl -X GET "http://127.0.0.1:5000/products/{id}" -H "accept: application/json"
```

### Test Case 3: Create Product
- **Test Method**: `test_create_product`
- **Description**: Verify that the `create_product` method adds a product to the database.
- **Mock**: `ProductRepository.create`
- **Expected Result**: The method should add the product to the database and return the created product.
- **Assertions**:
  - Check if `ProductRepository.create` is called once with the mocked product.
  - Verify that the returned product has the correct attributes.

```bash
$ curl -X POST "http://127.0.0.1:5000/products/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name": "New Product", "price": 19.99, "description": "A new product description"}'
```

### Test Case 4: Update Product
- **Test Method**: `test_update_product`
- **Description**: Verify that the `update_product` method updates the product in the database.
- **Mock**: `ProductRepository.get_by_id`, `ProductRepository.update`
- **Expected Result**: The method should update the product and return the updated product.
- **Assertions**:
  - Check if `ProductRepository.get_by_id` is called once with the correct ID.
  - Verify that `ProductRepository.update` is called once.
  - Check if the returned product has the updated attributes.

```bash
$ curl -X PUT "http://127.0.0.1:5000/products/{id}" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name": "Updated Product", "price": 29.99, "description": "An updated product description"}'
```

### Test Case 5: Delete Product
- **Test Method**: `test_delete_product`
- **Description**: Verify that the `delete_product` method deletes a product from the database.
- **Mock**: `ProductRepository.get_by_id`, `ProductRepository.delete`
- **Expected Result**: The method should delete the product from the database and return `True`.
- **Assertions**:
  - Check if `ProductRepository.get_by_id` is called once with the correct ID.
  - Verify that `ProductRepository.delete` is called once with the mocked product.
  - Check if the method returns `True` when the product is deleted.


```bash
$ curl -X DELETE "http://127.0.0.1:5000/products/{id}" -H "accept: application/json"
```

## ProductService Test Cases

### Test Case 6: Update Product Image
- **Test Method**: `test_update_product_image_success`
- **Description**: Verify that the `update_product_image` method updates the product image successfully.
- **Mock**: `ProductRepository.get_by_id`, `ProductRepository.update`
- **Expected Result**: The method should update the product image and return the updated product.
- **Assertions**:
  - Check if `ProductRepository.get_by_id` is called once with the correct ID.
  - Verify that `ProductRepository.update` is called once.
  - Check if the returned product has the updated image attribute.

```bash
$ curl -X POST "http://127.0.0.1:5000/products/{id}/upload_image" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "image=@./abc.png"
```
