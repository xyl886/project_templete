import json
from datetime import datetime

from auth2.models import UserConfig
from auth2.utils import generate_jwt_token, jwt_required
from common.response import Result
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt


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
            user_info = User.objects.filter(username=username).values('username', 'email')[0]
            # 验证密码是否正确
            if not user.check_password(password):
                return Result.error("密码错误", code=401)

            token = generate_jwt_token(user.id)
            response = Result.success("登录成功", userinfo=user_info, code=200)
            response['Authorization'] = f'Bearer {token}'
            return response

        except json.JSONDecodeError:
            return Result.error("Invalid JSON", code=400)

    return Result.error("Method not allowed", code=405)


# 获取用户fish配置
@csrf_exempt
@jwt_required
def get_user_config(request):
    # 获取请求头中的 Authorization 的值
    if request.method == 'GET':
        # 使用 request.user_id 来获取用户 ID
        user_id = request.user_id
        config = UserConfig.objects.filter(user_id=user_id).values(
            'daily_income', 'pay_day', 'work_days', 'work_end_time', 'work_start_time'
        ).first()
        if not config:
            return Result.error("用户配置不存在", code=404)
        return Result.success("获取用户配置成功", config=config, code=200)
    else:
        return Result.error("Method not allowed", code=405)


@csrf_exempt
@jwt_required
def update_user_config(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Result.error("Invalid JSON", code=400)

        # 校验必需的字段
        required_fields = ['work_days', 'work_start_time', 'work_end_time', 'pay_day', 'daily_income']
        for field in required_fields:
            if field not in data:
                return Result.error(f"Missing field: {field}", code=400)

        # 获取或创建用户配置
        config = UserConfig.objects.filter(user_id=request.user_id).first()
        if not config:
            config = UserConfig(user_id=request.user_id)
        # 更新配置字段
        config.work_days = data['work_days']
        config.work_start_time = data['work_start_time']
        config.work_end_time = data['work_end_time']
        config.pay_day = data['pay_day']
        config.daily_income = data['daily_income']
        # 转换工作时间格式
        try:
            config.work_start_time = datetime.strptime(data['work_start_time'], '%H:%M').time()
            config.work_end_time = datetime.strptime(data['work_end_time'], '%H:%M').time()
        except ValueError:
            return Result.error("Invalid time format, use HH:MM", code=400)

        try:
            config.full_clean()  # 验证模型
            config.save()  # 保存配置
        except ValidationError as e:
            return Result.error(f"Validation error: {e.message_dict}", code=400)
        # 手动构建返回的配置字典
        config_data = {
            'work_days': config.work_days,
            'work_start_time': str(config.work_start_time),  # 转换为字符串
            'work_end_time': str(config.work_end_time),      # 转换为字符串
            'pay_day': config.pay_day,
            'daily_income': str(config.daily_income)          # 转换为字符串
        }
        return Result.success("更新用户配置成功", code=200, config=config_data)
    else:
        return Result.error("Method not allowed", code=405)
