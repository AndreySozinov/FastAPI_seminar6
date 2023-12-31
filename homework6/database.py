from databases import Database
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String, Text, Float, Date, Boolean
from homework6.settings import settings

database = Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(settings.DATABASE_URL, connect_args={'check_same_thread': False})

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('firstname', String(settings.NAME_MAX_LENGTH)),
              Column('lastname', String(settings.NAME_MAX_LENGTH)),
              Column('email', String(settings.EMAIL_MAX_LENGTH)),
              Column('password', String(settings.PASSWORD_MAX_LENGTH)),
              )

products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('title', String(settings.NAME_MAX_LENGTH)),
                 Column('description', Text(settings.NAME_MAX_LENGTH)),
                 Column('price', Float(settings.EMAIL_MAX_LENGTH)),
                 )

orders = Table('orders', metadata,
               Column('id', Integer, primary_key=True),
               Column('user_id', Integer, foreign_key=True),
               Column('product_id', Integer, foreign_key=True),
               Column('order_date', Date()),
               Column('delivered', Boolean()),
               )

metadata.create_all(engine)
