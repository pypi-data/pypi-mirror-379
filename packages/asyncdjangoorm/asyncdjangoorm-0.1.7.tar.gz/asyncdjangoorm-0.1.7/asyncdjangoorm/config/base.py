from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from asyncdjangoorm._internal.manager import AsyncManager


class Base(DeclarativeBase):
    pass





class TimeStampedModel(Base):
    __abstract__ = True
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


AsyncManager = AsyncManager