from typing import List
from fastapi import APIRouter, Path
from database import products, database
from homework6.users import logger
from models import Product, ProductIn

product_router = APIRouter()


@product_router.post('/products/', response_model=Product, summary='Add new product')
async def create_product(product: ProductIn):
    query = products.insert().values(title=product.title,
                                     description=product.description,
                                     price=product.price)
    last_record_id = await database.execute(query)
    logger.info('Отработал POST запрос.')
    return {**product.model_dump(), 'id': last_record_id}


@product_router.get('/products/', response_model=List[Product], summary='Read products list')
async def read_products():
    query = products.select()
    logger.info('Отработал GET запрос.')
    return await database.fetch_all(query)


@product_router.get('/products/{product_id}', response_model=Product, summary='Read one product by ID')
async def read_product(product_id: int = Path(..., ge=1, title='The ID of the product')):
    query = products.select().where(products.c.id == product_id)
    logger.info(f'Отработал GET запрос для product ID = {product_id}.')
    return await database.fetch_one(query)


@product_router.put('/products/{product_id}', response_model=Product, summary='Edit product info')
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    logger.info(f'Отработал PUT запрос для product ID = {product_id}.')
    return {**new_product.model_dump(), 'id': product_id}


@product_router.delete('/products/{product_id}', summary='Delete product')
async def delete_product(product_id: int = Path(..., ge=1, title='The ID of the product')):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    logger.info(f'Отработал DELETE запрос для product ID = {product_id}')
    return {'message': f'Product {product_id} deleted'}
