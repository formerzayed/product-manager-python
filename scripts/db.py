from sqlalchemy import create_engine, String, Integer, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
import getpass

user = getpass.getuser()

db_name = "database.db"

engine = create_engine(f"sqlite:///{db_name}", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)

    company = Column(String)
    name = Column(String)

    date = Column(DateTime, default=datetime.utcnow())


class DB():

    def __init__(self):
        self.company = None
        self.name = None

        self.all_products = None

    def add_product(self, company, name):
        self.company = company
        self.name = name

        entry = Product(company=self.company,
                        name=self.name)
        session.add(entry)
        session.commit()

    def get_all_products(self):
        self.all_products = session.query(Product).all()
        return self.all_products
