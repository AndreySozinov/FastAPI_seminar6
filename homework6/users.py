import hashlib
import logging
from typing import List
from fastapi import APIRouter, Path
from database import users, database
from models import User, UserIn, UserOut

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_router = APIRouter()


@user_router.post('/users/', response_model=User, summary='Add new user')
async def create_user(user: UserIn):
    query = users.insert().values(firstame=user.firstname,
                                  lastname=user.lastname,
                                  email=user.email,
                                  password=hashlib.md5(user.password.encode('utf-8')).hexdigest())
    last_record_id = await database.execute(query)
    logger.info('Отработал POST запрос.')
    user.password = hashlib.md5(user.password.encode('utf-8')).hexdigest()
    return {**user.model_dump(), 'id': last_record_id}


@user_router.get('/users/', response_model=List[UserOut],  summary='Read users list')
async def read_users():
    query = users.select()
    logger.info('Отработал GET запрос.')
    return await database.fetch_all(query)


@user_router.get('/users/{user_id}', response_model=UserOut, summary='Read one user by ID')
async def read_user(user_id: int = Path(..., ge=1, title='The ID of the user')):
    query = users.select().where(users.c.id == user_id)
    logger.info(f'Отработал GET запрос для user ID = {user_id}.')
    return await database.fetch_one(query)


@user_router.put('/users/{user_id}', response_model=UserOut, summary='Edit user info')
async def update_user(user_id: int, new_user: UserOut):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    logger.info(f'Отработал PUT запрос для user ID = {user_id}.')
    return {**new_user.model_dump(), 'id': user_id}


@user_router.delete('/users/{user_id}', summary='Delete user')
async def delete_user(user_id: int = Path(..., ge=1, title='The ID of the user')):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    logger.info(f'Отработал DELETE запрос для user ID = {user_id}')
    return {'message': f'User {user_id} deleted'}
