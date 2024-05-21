from fastapi import APIRouter
from sqlalchemy.orm import scoped_session, sessionmaker

from schemas import SignUpModel
from models import User,Product,Order
from database import session,Base,engine
from fastapi import HTTPException,status
from werkzeug.security import generate_password_hash,check_password_hash


session = scoped_session(sessionmaker(bind=engine))


auth_router=APIRouter(
    prefix="/auth"
)


@auth_router.post("/signup",status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel):
    db_email=session.query(User).filter(user.email==User.email).first()
    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with this email already exists")
    db_username=session.query(User).filter(user.username==User.username).first()
    if db_username is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with this username already exists")


    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active,
    )

    session.add(new_user)
    session.commit()

    data={
        "id":new_user.id,
        "usernmae":new_user.username,
        "email":new_user.email,
        "is_staff":new_user.is_staff,
        "is_active":new_user.is_active,
    }

    response_model={
        "message":"Created successfully new user",
        "status":201,
        "data":data
    }
    return response_model




