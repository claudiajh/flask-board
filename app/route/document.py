from datetime import datetime

from flask import redirect, url_for, flash, request, render_template

from app import app, db
from app.models.DocumentModel import DocumentModel
from app.route.user import login_required
from app.util.query.query import getDocumentUserQuery, getCommentUserQuery


@app.route('/document')
@login_required
def doc_index(user):
    content_list = getDocumentUserQuery().all()
    return render_template('document/list.html', contents=content_list)

@app.route('/document/add', methods=['GET', 'POST'])
@login_required
def doc_add(user):
    if request.method == 'POST':
        new_content = DocumentModel(title=request.form['title'],
                                    content=request.form['content'],
                                    user_id=user.id)

        db.session.add(new_content)
        db.session.commit()

        return redirect(url_for('doc_index'))

    return render_template('document/add.html')


@app.route('/document/view/<doc_id>')
@login_required
def doc_view(user, doc_id):
    view_content = DocumentModel.query.filter_by(id=doc_id).one()
    if view_content.comment_count > 0:
        comment_content = getCommentUserQuery().filter_by(document_id=doc_id).all()
        return render_template('document/view.html', doc_view=view_content, comment_view=comment_content)

    return render_template('document/view.html', doc_view=view_content, comment_view=0)


@app.route('/document/update/<doc_id>', methods=['GET', 'POST'])
@login_required
def doc_update(user, doc_id):
    update_content = DocumentModel.query.filter_by(id=doc_id).one()

    if user.id == update_content.user_id:
        if request.method == 'POST':
            update_content.title = request.form['title']
            update_content.content = request.form['content']
            update_content.update_time = datetime.utcnow()

            db.session.commit()

            flash('글을 수정하였습니다.')
            return redirect(url_for('doc_index', doc_id=update_content.id))

        return render_template('document/update.html', doc_update=update_content)

    else:
        flash('자신이 작성한 글이 아니면 수정할 수 없습니다.')
        return redirect(url_for('doc_index'))


@app.route('/document/delete/<doc_id>')
@login_required
def doc_delete(user, doc_id):
    delete_content = DocumentModel.query.filter_by(id=doc_id).one()

    if user.id == delete_content.user_id:
        db.session.delete(delete_content)
        db.session.commit()

        flash('글이 삭제되었습니다.')
        return redirect(url_for('doc_index'))

    else:
        flash('자신이 작성한 글이 아니면 삭제할 수 없습니다.')
        return redirect(url_for('doc_index'))
