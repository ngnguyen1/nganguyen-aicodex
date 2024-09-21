import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
UPLOAD_FOLDER = UPLOAD_FOLDER