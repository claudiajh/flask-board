from app import app, db
from flask import redirect, url_for, request, render_template
from app.models.DocumentModel import DocumentModel
from datetime import datetime


@app.route('/board')
def document_index():
    content_list = DocumentModel.query.all()

    return render_template('document_list.html', contents=content_list)


@app.route('/board_add', methods=['GET', 'POST'])
def document_add():
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
        return redirect(url_for('document_index'))

    return render_template('document_add.html')


@app.route('/board_show/<content_no>')
def document_view(content_no):
    showContent = DocumentModel.query.filter_by(no=content_no).one()

    return render_template('document_view.html', document_view=showContent)


@app.route('/board_modify/<content_no>', methods=['GET', 'POST'])
def document_update(content_no):
    modifyContent = DocumentModel.query.filter_by(no=content_no).one()

    if request.method == 'POST':
        nowTime = datetime.utcnow()

        modifyContent.username = request.form['username']
        modifyContent.title = request.form['title']
        modifyContent.content = request.form['content']
        modifyContent.modify_time = nowTime

        db.session.commit()

        return redirect(url_for('document_index', content_no=modifyContent.no))

    return render_template('document_update.html', document_update=modifyContent)


@app.route('/board_del/<content_no>')
def document_delete(content_no):
    delContent = DocumentModel.query.filter_by(no=content_no).one()

    db.session.delete(delContent)
    db.session.commit()

    return redirect(url_for('document_index'))
