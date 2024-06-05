from sqlalchemy.orm import Session

from src.models.schemas import UserModel
from src.models.models import User


def get_user_by_user_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.user_id == user_id).first()


def create_user(db : Session) -> int:
    db_user = User()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.user_id


def update_user_data(db: Session, user_id: int, new_data: UserModel) -> User:
    user = get_user_by_user_id(db, user_id)
    if not user:
        return None
    for field, value in new_data.model_dump().items():
        setattr(user, field, value)     
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> User:
    client = get_user_by_user_id(user_id)
    db.delete(client)
    db.commit()
    db.close()
    return client