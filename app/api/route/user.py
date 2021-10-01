from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.auth import get_current_user
from core.security import get_password_hash
from db.session import get_session
from models.user import User
from schemas.user import UserLogin


router = APIRouter()


@router.post('/')
async def create_user(data: UserLogin, db: AsyncSession = Depends(get_session)):
    query = await db.execute(select(User).where(User.username == data.username))
    if query.scalar():
        raise HTTPException(400, 'User is exists')

    user = User(username=data.username, password=get_password_hash(data.password))
    db.add(user)
    await db.commit()
    return {}


@router.get('/profile')
async def get_profile(
    current_user: User = Depends(get_current_user)
):
    return {'username': current_user.username}