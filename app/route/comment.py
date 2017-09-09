from datetime import datetime

from flask import request, redirect, url_for, flash

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
                                   update_time=now)

        db.session.add(new_comment)

        update_content = DocumentModel.query.filter_by(id=doc_id).one()

        update_content.comment_count = update_content.comment_count + 1

        db.session.commit()

    return redirect(url_for('doc_view', doc_id=doc_id))

def view_comment(doc_id):
    return getCommentUSerQuery().filter_by(document_id=doc_id)


@app.route('/document/update/comment/<comment_id>', methods=['POST'])
def update_comment(comment_id):
    username = UserModel.query.filter_by(username=request.cookies.get('username')).one()
    comment = CommentModel.query.filter_by(id=comment_id).one()

    if username.id == comment.user_id:
        update_data = request.get_json()
        comment.content = update_data['comment']
        db.session.commit()

    else:
        return "해당 사용자가 아니면 수정 할 수 없습니다.", 404

    return '성공했습니다.', 200


@app.route('/document/delete/comment/<comment_id>')
def delete_comment(comment_id):
    username = UserModel.query.filter_by(username=request.cookies.get('username')).one()
    delete = getCommentUSerQuery().filter_by(id=comment_id).one()

    if username.id == delete.user_id:
        delete_content = CommentModel.query.filter_by(id=comment_id).one()

        update_content = DocumentModel.query.filter_by(id=delete_content.document_id).one()
        update_content.comment_count = update_content.comment_count - 1

        db.session.delete(delete_content)

        db.session.commit()

    else:
        flash("해당 사용자가 아니면 삭제할 수 없습니다.")

    return redirect(url_for('doc_view', doc_id=delete.document_id))
