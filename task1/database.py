from databases import Database
from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String, Date, Text
from task1.settings import settings

database = Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(settings.DATABASE_URL, connect_args={'check_same_thread': False})

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('firstname', String(settings.NAME_MAX_LENGTH)),
              Column('lastname', String(settings.NAME_MAX_LENGTH)),
              Column('birthday', Date()),
              Column('email', String(settings.EMAIL_MAX_LENGTH)),
              Column('address', Text()),
              Column('password', String(settings.PASSWORD_MAX_LENGTH)),
              )

metadata.create_all(engine)
