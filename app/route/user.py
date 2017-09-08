from app import app, db
from flask import render_template, flash, redirect, request, url_for
from datetime import datetime
from app.models.UserModel import UserModel


@app.route('/login', methods=['GET', 'POST'])
def login_index():
    if request.method == 'POST':
        loginUser = UserModel.query.filter_by(username=request.form['username']).filter_by(
            password=request.form['password']).one()
        if loginUser is not None:
            return redirect(url_for('board_index'))

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        nowTime = datetime.utcnow()

        if request.form['password'] == request.form['check_password']:
            newUser = UserModel(username=request.form['username'],
                                password=request.form['password'],
                                email=request.form['email'],
                                create_time=nowTime)

            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login_index'))

        else:
            # 오류 메시지 출력
            flash('pw가 잘못되었습니다. 다시 입력해주세요')

            return redirect(url_for('sign_up'))

    return render_template('signup.html')
