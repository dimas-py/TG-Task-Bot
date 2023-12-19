from sqlalchemy import create_engine, String, BigInteger
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test', echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str] = mapped_column(String(255))
    task_description: Mapped[str] = mapped_column(String(255))
    task_user_id: Mapped[int] = mapped_column(BigInteger)


# def create_tables():
#     Base.metadata.create_all(engine)
#     engine.echo = True
#
#
# create_tables()