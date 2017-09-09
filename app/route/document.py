from datetime import datetime

from flask import redirect, url_for, flash, request, render_template

from app import app, db
from app.models.DocumentModel import DocumentModel
from app.models.UserModel import UserModel
from app.route.comment import view_comment
from app.util.query.query import getDocumentUserQuery


@app.route('/document')
def doc_index():
    content_list = getDocumentUserQuery()

    return render_template('document/list.html', contents=content_list)


@app.route('/document/add', methods=['GET', 'POST'])
def doc_add():
    if request.method == 'POST':
        username = request.cookies.get('username')
        user = UserModel.query.filter_by(username=username).one()

        now = datetime.utcnow()
        new_content = DocumentModel(title=request.form['title'],
                                    content=request.form['content'],
                                    user_id=user.id,
                                    create_time=now,
                                    update_time=now,
                                    comment_count=0)

        db.session.add(new_content)
        db.session.commit()

        return redirect(url_for('doc_index'))

    return render_template('document/add.html')


@app.route('/document/view/<doc_id>')
def doc_view(doc_id):
    view_content = DocumentModel.query.filter_by(id=doc_id).one()
    if view_content.comment_count > 0:
        comment_content = view_comment(doc_id)
        return render_template('document/view.html', doc_view=view_content, comment_view=comment_content)

    return render_template('document/view.html', doc_view=view_content, comment_view=0)


@app.route('/document/update/<doc_id>', methods=['GET', 'POST'])
def doc_update(doc_id):
    username = UserModel.query.filter_by(username=request.cookies.get('username')).one()
    update_content = DocumentModel.query.filter_by(id=doc_id).one()

    if username.id == update_content.user_id:
        if request.method == 'POST':
            now = datetime.utcnow()

            update_content.title = request.form['title']
            update_content.content = request.form['content']
            update_content.update_time = now

            db.session.commit()

            flash('글을 수정하였습니다.')

            return redirect(url_for('doc_index', doc_id=update_content.id))

        return render_template('document/update.html', doc_update=update_content)

    else:
        flash('자신이 작성한 글이 아니면 수정할 수 없습니다.')
        return redirect(url_for('doc_index'))


@app.route('/document/delete/<doc_id>')
def doc_delete(doc_id):
    username = UserModel.query.filter_by(username=request.cookies.get('username')).one()
    delete_content = DocumentModel.query.filter_by(id=doc_id).one()

    if username.id == delete_content.user_id:

        db.session.delete(delete_content)
        db.session.commit()

        flash('글이 삭제되었습니다.')
        return redirect(url_for('d'))


    else:
        flash('자신이 작성한 글이 아니면 삭제할 수 없습니다.')
        return redirect(url_for('doc_index'))
