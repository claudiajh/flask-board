from sqlalchemy import Column, String, Integer, DateTime

from app import db


class UserModel(db.Model):
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_collate': 'utf8_general_ci'
    }
    id = Column(
        Integer,
        primary_key=True
    )  # user id

    username = Column(
        String(50),
        nullable=False,
        unique=True
    )  # username

    password = Column(
        String(100),
        nullable=False
    )  # password

    email = Column(
        String(100),
        nullable=False
    )  # email

    create_time = Column(
        DateTime
    )  # sign in date
