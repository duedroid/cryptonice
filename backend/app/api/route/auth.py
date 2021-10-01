from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.security import create_access_token, verify_password
from models.user import User
from schemas.token import Token
from db.session import get_session


router = APIRouter()


@router.post('/token', response_model=Token)
async def login_access_token(
    db: AsyncSession = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()
):
    query = await db.execute(select(User).where(User.username == form_data.username))
    user = query.scalar()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail='Incorrect useranme or password')

    return {
        'access_token': create_access_token(user.id),
        'token_type': 'bearer',
    }