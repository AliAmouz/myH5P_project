import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:3.141592@localhost/h5p_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
