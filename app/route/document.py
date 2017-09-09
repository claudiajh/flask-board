from app import app, db
from flask import redirect, url_for, request, render_template
from app.models.DocumentModel import DocumentModel
from datetime import datetime


@app.route('/document')
def doc_index():
    content_list = DocumentModel.query.all()

    return render_template('document/list.html', contents=content_list)


@app.route('/document/add', methods=['GET', 'POST'])
def doc_add():
    if request.method == 'POST':
        username = request.cookies.get('username')
        now = datetime.utcnow()
        new_content = DocumentModel(title=request.form['title'],
                                    content=request.form['content'],
                                    username=username,
                                    create_time=now,
                                    modify_time=now,
                                    coment_count=0)

        db.session.add(new_content)
        db.session.commit()
        return redirect(url_for('doc_index'))

    return render_template('document/add.html')


@app.route('/document/view/<content_no>')
def doc_view(content_no):
    view_content = DocumentModel.query.filter_by(no=content_no).one()

    return render_template('document/view.html', doc_view=view_content)


@app.route('/document/update/<content_no>', methods=['GET', 'POST'])
def doc_update(content_no):
    update_content = DocumentModel.query.filter_by(no=content_no).one()

    if request.method == 'POST':
        now = datetime.utcnow()

        update_content.username = request.form['username']
        update_content.title = request.form['title']
        update_content.content = request.form['content']
        update_content.modify_time = now

        db.session.commit()

        return redirect(url_for('doc_index', content_no=update_content.no))

    return render_template('document/update.html', doc_update=update_content)


@app.route('/document/delete/<content_no>')
def doc_delete(content_no):
    delete_content = DocumentModel.query.filter_by(no=content_no).one()

    db.session.delete(delete_content)
    db.session.commit()

    return redirect(url_for('doc_index'))
