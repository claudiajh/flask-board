from datetime import datetime

from flask import request, redirect, url_for

from app import app, db
from app.models.CommentModel import CommentModel
from app.models.DocumentModel import DocumentModel
from app.models.UserModel import UserModel
from app.util.query.query import getCommentUSerQuery


@app.route('/document/add/comment/<doc_id>', methods=['GET', 'POST'])
def add_comment(doc_id):
    if request.method == 'POST':
        username = UserModel.query.filter_by(username=request.cookies.get('username')).one()

        now = datetime.utcnow()
        new_comment = CommentModel(document_id=doc_id,
                                   user_id=username.id,
                                   content=request.form['comment'],
                                   create_time=now)

        db.session.add(new_comment)

        update_content = DocumentModel.query.filter_by(id=doc_id).one()

        update_content.comment_count = update_content.comment_count + 1

        db.session.commit()

    return redirect(url_for('doc_view', doc_id=doc_id))


def view_comment(doc_id):
    return getCommentUSerQuery().filter_by(document_id=doc_id)
