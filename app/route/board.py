from app import app, db
from flask import redirect, url_for, request, render_template
from app.models.boards import BoardModel
from datetime import datetime


@app.route('/board')
def board_index():
    content_list = BoardModel.query.all()

    return render_template('show_board.html', contents=content_list)


@app.route('/board_add', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        nowTime = datetime.utcnow()
        newContent = BoardModel(title=request.form['title'],
                                content=request.form['content'],
                                user=request.form['user'],
                                create_time=nowTime,
                                modify_time=nowTime)

        db.session.add(newContent)
        db.session.commit()
        return redirect(url_for('board_index'))

    return render_template('add_content.html')


@app.route('/board_show/<content_no>')
def show_content(content_no):
    showContent = BoardModel.query.filter_by(no=content_no).one()

    return render_template('show_content.html', show_content=showContent)


@app.route('/board_modify/<content_no>', methods=['GET', 'POST'])
def modify_content(content_no):
    modifyContent = BoardModel.query.filter_by(no=content_no).one()

    if request.method == 'POST':
        nowTime = datetime.utcnow()

        modifyContent.user = request.form['user']
        modifyContent.title = request.form['title']
        modifyContent.content = request.form['content']
        modifyContent.modify_time = nowTime

        db.session.commit()

        return redirect(url_for('board_index', content_no=modifyContent.no))

    return render_template('modify_content.html', modify_content=modifyContent)
