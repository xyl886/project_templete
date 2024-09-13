import json

from auth2.utils import generate_jwt_token
from common.response import Result
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from loguru import logger


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if User.objects.filter(username=username).exists():
                return Result.error("用户已存在", code=400)

            user = User.objects.create_user(username=username, password=password)
            user.save()

            return Result.success("注册成功", code=200)

        except json.JSONDecodeError:
            return Result.error("Invalid JSON", code=400)

    return Result.error("Method not allowed", code=405)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # 检查用户是否存在
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Result.error("用户不存在", code=404)
            # 获取用户信息
            user_info = User.objects.filter(username=username).values('id', 'username', 'email')[0]
            # 验证密码是否正确
            if not user.check_password(password):
                return Result.error("密码错误", code=401)

            token = generate_jwt_token(user.id)
            response = Result.success("登录成功", userinfo=user_info, code=200)
            response['Authorization'] = f'Bearer {token}'
            logger.info(f"token: {token}")
            return response

        except json.JSONDecodeError:
            return Result.error("Invalid JSON", code=400)

    return Result.error("Method not allowed", code=405)
