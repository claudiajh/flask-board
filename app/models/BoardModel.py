from app import db


class BoardModel(db.Model):
    __tablename__ = 'board'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    no = db.Column(db.Integer, primary_key=True)  # 번호
    title = db.Column(db.String(80), nullable=False)  # 제목
    content = db.Column(db.String(200), nullable=False)  # 내용
    id = db.Column(db.String(50), nullable=False)  # 작성자
    create_time = db.Column(db.DATETIME)  # 작성일
    modify_time = db.Column(db.DATETIME)  # 수정일
