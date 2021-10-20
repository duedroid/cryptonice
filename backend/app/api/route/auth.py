from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.future import select

from core.security import get_password_hash
from core.security import create_access_token, verify_password
from db.database import database
from models.user import User
from schemas.token import Token
from schemas.user import UserRegister


router = APIRouter()


@router.post('/register')
async def register(data: UserRegister):
    query = await database.execute(select(User).where(User.username == data.username))
    if query.scalar():
        raise HTTPException(400, 'User is exists')

    user = User(
        username=data.username,
        password=get_password_hash(data.password),
        bridge=data.bridge,
        api_key=data.api_key,
        api_secret=data.api_secret
    )
    database.add(user)
    await database.commit()
    return {}


@router.post('/token', response_model=Token)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    query = await database.execute(select(User).where(User.username == form_data.username))
    user = query.scalar()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail='Incorrect useranme or password')

    return {
        'access_token': create_access_token(user.id),
        'token_type': 'bearer',
    }