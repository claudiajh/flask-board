from app import db


class UserModel(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    no = db.Column(db.Integer, primary_key=True)  # 번호
    id = db.Column(db.String(50), nullable=False)  # id
    pw = db.Column(db.String(100), nullable=False)  # pw
    email = db.Column(db.String(100), nullable=False)  # email
    signup_time = db.Column(db.DATETIME)  # 가입일
