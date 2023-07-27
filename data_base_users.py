
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'SearchResults2.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class VKUser(Base):

    # Класс, представляющий пользователя ВК

     __tablename__ = 'vk_user'
     vk_id = sa.Column(sa.Integer, primary_key=True)
     first_name = sa.Column(sa.String(80), nullable=False)
     last_name = sa.Column(sa.String(80))
     user_age = sa.Column(sa.Integer)
     sex = sa.Column(sa.Integer)
     city = sa.Column(sa.String(60))
     city_id = sa.Column(sa.Integer)

 class DatingUser(Base):

     #Класс, представляющий пользователя для знакомств

     __tablename__ = 'dating_user'
     vk_id = sa.Column(sa.Integer, primary_key=True)
     user_id = sa.Column(sa.Integer, sa.ForeignKey('vk_user.vk_id'))

 class BlackList(Base):

     #Класс, представляющий черный список.

     __tablename__ = 'blacklist'
     vk_id = sa.Column(sa.Integer, primary_key=True)
     user_id = sa.Column(sa.Integer, sa.ForeignKey('vk_user.vk_id'))


 #Создать все таблицы в движке - эквивалентно "Создать таблицу"
 Base.metadata.create_all(engine)
