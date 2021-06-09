from .ui import Alerts
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, String, Integer, Column, DateTime

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
        self.single_product = None
        self.alert = Alerts("red")

    def add_product(self, company, name):
        self.company = company
        self.name = name

        try:
            entry = Product(company=self.company,
                            name=self.name)
            session.add(entry)
            session.commit()

            return True

        except:
            return False

    def get_all_products(self):
        self.all_products = session.query(Product).all()
        return self.all_products

    def get_product(self, id):
        try:
            self.single_product = session.query(
                Product).filter(Product.id == id).first()

            return self.single_product

        except:
            return self.alert.warning(f"There is nothing in the DB with the product id {id}")

    def update_product(self, product, company, name):
        self.product = product
        self.product.name = name
        self. product.company = company
        session.commit()

    def delete_product(self, product_id):
        try:
            self.product_to_delete = session.query(
                Product).filter(Product.id == product_id).delete()
            session.commit()

            return True

        except:
            return False
