import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey, String, BigInteger, Date, Time, Boolean
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

load_dotenv()
engine = create_engine(f'mysql+mysqlconnector://{os.getenv("MYSQL_USER")}:'
                       f'{os.getenv("MYSQL_PASSWORD")}@127.0.0.1:'
                       f'3306/{os.getenv("MYSQL_DATABASE")}', echo=True)
# engine = create_engine(f'mysql+mysqlconnector://{os.getenv("MYSQL_USER")}:'
#                        f'{os.getenv("MYSQL_PASSWORD")}@localhost:'
#                        f'3306/{os.getenv("MYSQL_DATABASE")}', echo=True)
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
    task_user_id: Mapped[int] = mapped_column(BigInteger)
    task_name: Mapped[str] = mapped_column(String(255))
    task_description: Mapped[str] = mapped_column(String(255))
    date_term: Mapped[Date] = mapped_column(Date)
    task_priority: Mapped[str] = mapped_column(String(255))
    notification: Mapped[bool] = mapped_column(Boolean)
    notify_time: Mapped[Time] = mapped_column(Time, nullable=True)


class DoneTask(Base):
    __tablename__ = 'done_tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    task_user_id: Mapped[int] = mapped_column(BigInteger)
    task_name: Mapped[str] = mapped_column(String(255))
    task_description: Mapped[str] = mapped_column(String(255))
    date_term: Mapped[Date] = mapped_column(Date)
    task_priority: Mapped[str] = mapped_column(String(255))
    notification: Mapped[bool] = mapped_column(Boolean)
    notify_time: Mapped[Time] = mapped_column(Time, nullable=True)



# def create_tables():
#     Base.metadata.create_all(engine)
#     engine.echo = True
#
#
# create_tables()
