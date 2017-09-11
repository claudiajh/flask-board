import datetime

from sqlalchemy import Column, String, Integer, DateTime

from app import db


class BoardModel(db.Model):
    __tablename__ = 'board'
    __table_args__ = {
        'mysql_collate': 'utf8_general_ci'
    }

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(
        String(50),
        nullable=False,
        unique=True
    )  # board english name

    name = Column(
        String(50),
        nullable=False
    )  # board korean name

    create_time = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )
