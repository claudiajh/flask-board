from datetime import datetime

from flask import make_response, render_template, flash, redirect, request, url_for
from functools import wraps

from app import app, db
from app.models.UserModel import UserModel


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = request.cookies.get('username')
        if username is None:
            flash('로그인이 필요한 서비스입니다.')
            return redirect(url_for('signin', next=request.url))

        else:
            user = UserModel.query.filter_by(username=username).first()
            if user is None:
                flash('알 수 없는 회원정보입니다.')
                return redirect(url_for('signin', next=request.url))

            else:
                return f(user, *args, **kwargs)

    return decorated_function


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        signin_user = UserModel.query.filter_by(username=request.form['username']).filter_by(
            password=request.form['password']).first()  # one -> 첫 번째꺼가 없으면 오류, first -> 첫 번째꺼가 없으면 None

        if signin_user is None:
            flash('id, pw를 확인해주세요.')
            return redirect(url_for('signin'))

        else:
            resp = make_response(redirect(url_for('doc_index')))
            resp.set_cookie('username', signin_user.username)
            return resp

    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        now = datetime.utcnow()

        if request.form['password'] == request.form['check_password']:
            signup_user = UserModel(username=request.form['username'],
                                    password=request.form['password'],
                                    email=request.form['email'],
                                    create_time=now)

            db.session.add(signup_user)
            db.session.commit()
            return redirect(url_for('signin'))

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
