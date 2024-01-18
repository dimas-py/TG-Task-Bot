from sqlalchemy import create_engine, ForeignKey, String, BigInteger, Date, Time, Boolean
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/tgbot', echo=True)
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
    notify_type: Mapped[str] = mapped_column(String(255), nullable=True)
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
    notify_type: Mapped[str] = mapped_column(String(255), nullable=True)
    notify_time: Mapped[Time] = mapped_column(Time, nullable=True)



# def create_tables():
#     Base.metadata.create_all(engine)
#     engine.echo = True
#
#
# create_tables()
