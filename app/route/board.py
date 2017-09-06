from app import app, db
from flask import redirect, url_for, request, render_template
from app.models.boards import BoardModel
from datetime import datetime


@app.route('/board')
def board_index():
    content_list = BoardModel.query.all()

    return render_template('show_board.html', contents=content_list)


@app.route('/board_new', methods=['GET', 'POST'])
def new_content():
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

    return render_template('new_content.html')


@app.route('/board/<content_no>')
def show_content(content_no):
    showContent = BoardModel.query.filter_by(no=content_no).one()

    return render_template('show_content.html', show_content=showContent)
