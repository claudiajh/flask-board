from app import app, db
from flask import render_template, redirect, request, url_for
from datetime import datetime
from app.models.UserModel import UserModel


@app.route('/login')
def login_index():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        nowTime = datetime.utcnow()
        newUser = UserModel(id=request.form['id'],
                            pw=request.form['pw'],
                            email=request.form['email'],
                            signup_time=nowTime)

        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('login_index'))

    return render_template('signup.html')
