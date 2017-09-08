from app import db


class UserModel(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    no = db.Column(db.Integer, primary_key=True)  # 번호
    username = db.Column(db.String(50), nullable=False, unique=True)  # username
    password = db.Column(db.String(100), nullable=False)  # password
    email = db.Column(db.String(100), nullable=False)  # email
    create_time = db.Column(db.DATETIME)  # 가입일
