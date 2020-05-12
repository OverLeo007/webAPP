import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
import json


class Item(SqlAlchemyBase):
    __tablename__ = 'items'
    num = sqlalchemy.Column(sqlalchemy.Integer,
                            primary_key=True, autoincrement=True)
    index = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    color = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return json.dumps(
            {'ind': f'{self.index}', 'color': f'{self.color}'})
