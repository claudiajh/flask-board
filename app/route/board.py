from app import app, db
from flask import redirect, url_for, request, render_template
from app.models.boards import BoardModel
from datetime import datetime


@app.route('/board')
def board_index():
    content_list = BoardModel.query.all()

    return render_template('show_board.html', contents=content_list)
