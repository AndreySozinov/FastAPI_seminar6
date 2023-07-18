"""
Необходимо создать базу данных для интернет-магазина. База данных должна
состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
содержать информацию о доступных товарах, их описаниях и ценах. Таблица
пользователи должна содержать информацию о зарегистрированных
пользователях магазина. Таблица заказы должна содержать информацию о
заказах, сделанных пользователями.
○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
имя, фамилия, адрес электронной почты и пароль.
○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
название, описание и цена.
○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
заказа.
Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц
(итого шесть моделей).
📌 Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
○ Чтение всех
○ Чтение одного
○ Запись
○ Изменение
○ Удаление
"""
import uvicorn
from fastapi import FastAPI
from homework6.database import database
from users import user_router, logger
from products import product_router
from orders import order_router

app = FastAPI()

app.include_router(user_router, tags=['users'])
app.include_router(product_router, tags=['products'])
app.include_router(order_router, tags=['orders'])


@app.get('/')
async def root():
    logger.info('Отработал GET запрос.')
    return {"message": "My Internet Shop"}


@app.on_event('startup')
async def startup():
    logger.info('Подключение базы данных.')
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    logger.info('Отключение базы данных.')
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
