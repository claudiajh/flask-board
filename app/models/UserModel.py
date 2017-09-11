import datetime

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
    )

    username = Column(
        String(50),
        nullable=False,
        unique=True
    )

    password = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        nullable=False
    )

    create_time = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )
