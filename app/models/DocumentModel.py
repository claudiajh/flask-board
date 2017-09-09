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
    )  # document id

    title = Column(
        String(80),
        nullable=False
    )  # document title

    content = Column(
        String(200),
        nullable=False
    )  # document content

    board_id = Column(
        Integer,
        ForeignKey('board.id')
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )  # document write user

    create_time = Column(
        DateTime
    )  # document create date

    update_time = Column(
        DateTime
    )  # document update date

    comment_count = Column(
        Integer,
        nullable=False
    )  # comment count
