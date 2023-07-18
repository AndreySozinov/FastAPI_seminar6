from typing import List
from fastapi import APIRouter, Path
from database import orders, database, users, products
from homework6.users import logger
from models import Order, OrderIn

order_router = APIRouter()


@order_router.post('/orders/', response_model=Order, summary='Add new order')
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id,
                                   product_id=order.product_id,
                                   order_date=order.order_date,
                                   delivered=order.delivered)
    last_record_id = await database.execute(query)
    logger.info('Отработал POST запрос.')
    return {**order.model_dump(), 'id': last_record_id}


@order_router.get('/orders/', response_model=List[Order], summary='Read orders list')
async def read_order():
    """query = orders.select()"""
    query = orders.select().join(users, users.c.id == orders.c.user_id).\
        join(products, products.c.id == orders.c.product_id)
    logger.info('Отработал GET запрос.')
    return await database.fetch_all(query)


@order_router.get('/orders/{order_id}', response_model=Order, summary='Read one order by ID')
async def read_order(order_id: int = Path(..., ge=1, title='The ID of the order')):
    query = orders.select().where(orders.c.id == order_id)
    logger.info(f'Отработал GET запрос для order ID = {order_id}.')
    return await database.fetch_one(query)


@order_router.put('/orders/{order_id}', response_model=Order, summary='Edit order info')
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    logger.info(f'Отработал PUT запрос для order ID = {order_id}.')
    return {**new_order.model_dump(), 'id': order_id}


@order_router.delete('/orders/{order_id}', summary='Delete order')
async def delete_order(order_id: int = Path(..., ge=1, title='The ID of the order')):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    logger.info(f'Отработал DELETE запрос для order ID = {order_id}')
    return {'message': f'Product {order_id} deleted'}
