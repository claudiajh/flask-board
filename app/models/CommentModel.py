import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import ForeignKey

from app import db


class CommentModel(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {
        'mysql_collate': 'utf8_general_ci'
    }

    id = Column(
        Integer,
        primary_key=True
    )

    document_id = Column(
        Integer,
        ForeignKey('document.id')
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )

    content = Column(
        String(200),
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
