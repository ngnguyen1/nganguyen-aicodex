class ProductDTO:
    def __init__(self, id, name, price, picture, description):
        self.id = id
        self.name = name
        self.price = price
        self.picture = picture
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'picture': self.picture,
            'description': self.description
        }

    def __eq__(self, other):
        if isinstance(other, ProductDTO):
            return self.to_dict() == other.to_dict()
        return False