"""
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
○ id: int (идентификатор пользователя, генерируется автоматически)
○ username: str (имя пользователя)
○ email: str (электронная почта пользователя)
○ password: str (пароль пользователя)
API должно поддерживать следующие операции:
○ Получение списка всех пользователей: GET /users/
○ Получение информации о конкретном пользователе: GET /users/{user_id}/
○ Создание нового пользователя: POST /users/
○ Обновление информации о пользователе: PUT /users/{user_id}/
○ Удаление пользователя: DELETE /users/{user_id}/
📌 Для валидации данных используйте параметры Field модели User.
📌 Для работы с базой данных используйте SQLAlchemy и модуль databases.
"""
import uvicorn
from fastapi import FastAPI

from task1.database import database
from users import router, logger

app = FastAPI()

app.include_router(router, tags=['users'])


@app.get('/')
async def root():
    logger.info('Отработал GET запрос.')
    return {"message": "User list manager"}


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
