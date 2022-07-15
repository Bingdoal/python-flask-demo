from dataclasses import dataclass

from model import db


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    email: str

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def find_all(self):
        return UserModel.query.all()
