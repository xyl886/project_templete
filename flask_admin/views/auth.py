# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request

from flask_admin.common.response import Result
from flask_admin.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return Result.error(message="User already exists").to_json()

    User.create_user(data)

    return Result.success(message="User registered successfully").to_json()


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return Result.error(message="Invalid credentials").to_json()

    return Result.success(message="Login successful").to_json()
