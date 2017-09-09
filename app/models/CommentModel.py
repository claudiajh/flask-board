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
    )  # comment id

    document_id = Column(
        Integer,
        ForeignKey('document.id')
    )  # comment's document id

    content = Column(
        String(200),
        nullable=False
    )  # document content

    create_time = Column(
        DateTime
    )  # comment create date
