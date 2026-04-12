from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserService:
    @staticmethod
    def register(data):
        if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
            return {"message": "Username atau Email sudah terdaftar"}, 409
        
        new_user = User(
            username=data['username'],
            password=generate_password_hash(data['password']),
            email=data['email'],
            nama=data['nama']
        )
        db.session.add(new_user)
        db.session.commit()
        return {"message": "Registrasi berhasil"}, 201

    @staticmethod
    def login(data):
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            token = create_access_token(identity=str(user.id))
            return {"message": "Login berhasil", "token": token}, 200
        return {"message": "Username atau password salah"}, 401

    @staticmethod
    def get_all():
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    @staticmethod
    def update(user_id, data):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User tidak ditemukan"}, 404
        
        if 'username' in data: user.username = data['username']
        if 'email' in data: user.email = data['email']
        if 'nama' in data: user.nama = data['nama']
        
        db.session.commit()
        return {"message": "Data user berhasil diperbarui"}, 200

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User tidak ditemukan"}, 404
        
        db.session.delete(user)
        db.session.commit()
        return {"message": "User berhasil dihapus"}, 200