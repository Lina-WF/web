import sqlalchemy

from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    describtion = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_sold_out = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    path_to_img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer)
