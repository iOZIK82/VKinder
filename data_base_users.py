from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'SearchResults2.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class VKUser(Base):
    __tablename__ = 'vk_user'
    vk_id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80))
    user_age = Column(Integer)
    sex = Column(Integer)
    city = Column(String(60))
    city_id = Column(Integer)


class DatingUser(Base):
    # Класс, представляющий пользователя для знакомств

    __tablename__ = 'dating_user'
    vk_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('vk_user.vk_id'))


class BlackList(Base):
    # Класс, представляющий черный список.
    __tablename__ = 'blacklist'
    vk_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('vk_user.vk_id'))


# Создать все таблицы в проекте - эквивалентно "Создать таблицу"
Base.metadata.create_all(engine)
