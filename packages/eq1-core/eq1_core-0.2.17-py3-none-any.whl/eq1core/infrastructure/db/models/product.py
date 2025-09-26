from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from .common import CommonModel


class ProductModel(CommonModel, Base):
    __tablename__ = 'products'
    # __table_args__ = {'extend_existing': True}

    name = Column(String(50), nullable=False, comment='제품 이름')
    code = Column(String(50), nullable=False, unique=True, comment='제품 코드')
    thumbnail_path = Column(String(100), nullable=True, unique=False, comment='썸네일 이미지 경로')

    components = relationship('ComponentModel', back_populates='product')
