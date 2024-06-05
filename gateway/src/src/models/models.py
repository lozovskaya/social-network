from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from .database import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    birthday = Column(DateTime)
    phone_number = Column(String)
    
    credentials = relationship("Credentials", back_populates="user")
    
    
class Credentials(Base):
    __tablename__ = 'credentials'

    credentials_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    login = Column(String)
    password_hash = Column(String)
    
    user = relationship("User", back_populates="credentials")