from app import app
from flask import render_template


@app.route('/login')
def login_index():
    return render_template('login.html')
