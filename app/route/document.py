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
        usrname = request.cookies.get('username')
        nowTime = datetime.utcnow()
        newContent = DocumentModel(title=request.form['title'],
                                   content=request.form['content'],
                                   username=usrname,
                                   create_time=nowTime,
                                   modify_time=nowTime,
                                   coment_count=0)

        db.session.add(newContent)
        db.session.commit()
        return redirect(url_for('doc_index'))

    return render_template('document/add.html')


@app.route('/document/view/<content_no>')
def doc_view(content_no):
    showContent = DocumentModel.query.filter_by(no=content_no).one()

    return render_template('document/view.html', doc_view=showContent)


@app.route('/document/update/<content_no>', methods=['GET', 'POST'])
def doc_update(content_no):
    modifyContent = DocumentModel.query.filter_by(no=content_no).one()

    if request.method == 'POST':
        nowTime = datetime.utcnow()

        modifyContent.username = request.form['username']
        modifyContent.title = request.form['title']
        modifyContent.content = request.form['content']
        modifyContent.modify_time = nowTime

        db.session.commit()

        return redirect(url_for('doc_index', content_no=modifyContent.no))

    return render_template('document/update.html', doc_update=modifyContent)


@app.route('/document/delete/<content_no>')
def doc_delete(content_no):
    delContent = DocumentModel.query.filter_by(no=content_no).one()

    db.session.delete(delContent)
    db.session.commit()

    return redirect(url_for('doc_index'))
