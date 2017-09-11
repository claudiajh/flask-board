from flask import request, redirect, url_for, jsonify

from app import app, db
from app.models.CommentModel import CommentModel
from app.models.DocumentModel import DocumentModel
from app.route.user import login_required
from flask import request, redirect, url_for, jsonify

from app import app, db
from app.models.CommentModel import CommentModel
from app.models.DocumentModel import DocumentModel
from app.route.user import login_required


@app.route('/document/add/comment/<doc_id>', methods=['GET', 'POST'])
@login_required
def add_comment(user, doc_id):
    if request.method == 'POST':
        new_comment = CommentModel(document_id=doc_id,
                                   user_id=user.id,
                                   content=request.form['comment'])

        db.session.add(new_comment)

        update_content = DocumentModel.query.filter_by(id=doc_id).one()
        update_content.comment_count = update_content.comment_count + 1

        db.session.commit()

    return redirect(url_for('doc_view', doc_id=doc_id))


@app.route('/document/update/comment/<comment_id>', methods=['POST'])
@login_required
def update_comment(user, comment_id):
    comment = CommentModel.query.filter_by(id=comment_id).one()

    if user.id == comment.user_id:
        update_data = request.get_json()
        comment.content = update_data['comment']
        db.session.commit()

    else:
        return jsonify({'result': "해당 사용자가 아니면 수정 할 수 없습니다."}), 404

    return jsonify({'result': '성공했습니다.'}), 200


@app.route('/document/delete/comment/<comment_id>')
@login_required
def delete_comment(user, comment_id):
    comment = CommentModel.query.filter_by(id=comment_id).one()

    if user.id == comment.user_id:
        document = DocumentModel.query.filter_by(id=comment.document_id).one()
        document.comment_count = document.comment_count - 1

        db.session.delete(comment)
        db.session.commit()

    else:
        return jsonify({'result': "해당 사용자가 아니면 수정 할 수 없습니다."}), 404

    return jsonify({'result': '성공했습니다.'}), 200
