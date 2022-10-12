from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

jwt: JWTManager = JWTManager()
db: SQLAlchemy = SQLAlchemy()