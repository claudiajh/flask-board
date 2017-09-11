import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import ForeignKey

from app import db


class DocumentModel(db.Model):
    __tablename__ = 'document'
    __table_args__ = {
        'mysql_collate': 'utf8_general_ci'
    }

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(
        String(80),
        nullable=False
    )

    content = Column(
        String(200),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )

    comment_count = Column(
        Integer,
        default=0,
        nullable=False
    )

    create_time = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    update_time = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )
