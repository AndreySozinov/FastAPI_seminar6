from pydantic import BaseModel, Field, EmailStr
from settings import settings
from datetime import date


class UserIn(BaseModel):
    firstname: str = Field(..., title='Имя пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., title='Фамилия пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    birthday: date = Field(..., title="Дата рождения", format='%Y-%m-%d')
    email: EmailStr = Field(..., description='Email', max_length=settings.EMAIL_MAX_LENGTH)
    address: str = Field(..., title='Адрес', min_length=5)
    password: str = Field(..., min_length=8, max_length=settings.PASSWORD_MAX_LENGTH, description='Пароль')


class UserOut(BaseModel):
    firstname: str = Field(..., title='Имя пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., title='Фамилия пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    birthday: date = Field(..., title="Дата рождения", format='%Y-%m-%d')
    email: EmailStr = Field(..., description='Email', max_length=settings.EMAIL_MAX_LENGTH)
    address: str = Field(..., title='Адрес', min_length=5)


class User(BaseModel):
    id: int
    firstname: str = Field(..., title='Имя пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., title='Фамилия пользователя', min_length=2, max_length=settings.NAME_MAX_LENGTH)
    birthday: date = Field(..., title="Дата рождения", format='%Y-%m-%d')
    email: EmailStr = Field(..., description='Email', max_length=settings.EMAIL_MAX_LENGTH)
    address: str = Field(..., title='Адрес', min_length=5)
    password: str = Field(..., min_length=8, max_length=settings.PASSWORD_MAX_LENGTH, description='Пароль')
