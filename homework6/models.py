from pydantic import BaseModel, Field, EmailStr
from settings import settings
from datetime import date


class UserIn(BaseModel):
    firstname: str = Field(..., title='Имя пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., title='Фамилия пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., description='Email', max_length=settings.EMAIL_MAX_LENGTH)
    password: str = Field(..., min_length=8, max_length=settings.PASSWORD_MAX_LENGTH, description='Пароль')


class UserOut(BaseModel):
    firstname: str = Field(..., title='Имя пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., title='Фамилия пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., description='Email', max_length=settings.EMAIL_MAX_LENGTH)


class User(BaseModel):
    id: int
    firstname: str = Field(..., title='Имя пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., title='Фамилия пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., description='Email', max_length=settings.EMAIL_MAX_LENGTH)
    password: str = Field(..., min_length=8, max_length=settings.PASSWORD_MAX_LENGTH, description='Пароль')


class ProductIn(BaseModel):
    title: str = Field(..., title='Название', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    description: str = Field(..., title='Описание', max_length=300)
    price: float = Field(..., title='Цена', gt=0)


class Product(BaseModel):
    id: int
    title: str = Field(..., title='Название', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    description: str = Field(..., title='Описание', max_length=300)
    price: float = Field(..., title='Цена', gt=0)


class OrderIn(BaseModel):
    user_id: int = Field(..., title='ID покупателя', gt=0)
    product_id: int = Field(..., title='ID товара', gt=0)
    order_date: date = Field(..., title="Дата заказа", format='%Y-%m-%d')
    delivered: bool = Field(title='Выполнен', default=False)


class Order(BaseModel):
    id: int
    user_id: int = Field(..., title='ID покупателя', gt=0)
    product_id: int = Field(..., title='ID товара', gt=0)
    order_date: date = Field(..., title="Дата заказа", format='%Y-%m-%d')
    delivered: bool = Field(title='Выполнен', default=False)
