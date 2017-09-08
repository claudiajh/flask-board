from app import app, db
from flask import make_response, render_template, flash, redirect, request, url_for
from datetime import datetime
from app.models.UserModel import UserModel


@app.route('/signin', methods=['GET', 'POST'])
def signin_index():
    if request.method == 'POST':
        loginUser = UserModel.query.filter_by(username=request.form['username']).filter_by(
            password=request.form['password']).first()  # one -> 첫 번째꺼가 없으면 오류, first -> 첫 번째꺼가 없으면 None

        if loginUser is None:
            flash('id, pw를 확인해주세요.')
            return redirect(url_for('signin_index'))

        else:
            resp = make_response(redirect(url_for('doc_index')))
            resp.set_cookie('username', loginUser.username)
            return resp

    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        now = datetime.utcnow()

        if request.form['password'] == request.form['check_password']:
            newUser = UserModel(username=request.form['username'],
                                password=request.form['password'],
                                email=request.form['email'],
                                create_time=now)

            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('signin_index'))

        else:
            # 오류 메시지 출력
            flash('pw가 잘못되었습니다. 다시 입력해주세요')

            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/singout')
def signout():
    resp = redirect(url_for('index'))
    resp.set_cookie('username', expires=0)

    return resp
