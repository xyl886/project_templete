import datetime
from functools import wraps

import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from loguru import logger

# 时间阈值：快过期的判断标准（比如 5 分钟）
REFRESH_THRESHOLD = datetime.timedelta(minutes=5)


def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + settings.JWT_AUTH['JWT_EXPIRATION_DELTA'],
        'iat': datetime.datetime.now(datetime.timezone.utc)
    }
    token = jwt.encode(
        payload,
        settings.JWT_AUTH['JWT_SECRET_KEY'],
        algorithm=settings.JWT_AUTH['JWT_ALGORITHM'])
    return token


def validate_jwt_token(token):
    from common.response import Result

    try:
        # 解码并验证 token
        payload = jwt.decode(
            token,
            settings.JWT_AUTH['JWT_SECRET_KEY'],
            algorithms=[settings.JWT_AUTH['JWT_ALGORITHM']]
        )

        # 检查是否快过期，如果是，则自动刷新
        exp_timestamp = datetime.datetime.fromtimestamp(payload['exp'], datetime.timezone.utc)
        remaining_time = exp_timestamp - datetime.datetime.now(datetime.timezone.utc)

        if remaining_time < REFRESH_THRESHOLD:
            new_token = generate_jwt_token(payload['user_id'])
            return payload, new_token  # 返回解码的 payload 和新的 token

        return payload, None  # 没有新的 token

    except ExpiredSignatureError:
        # token 已过期
        return Result.error("Token has expired", code=401), None
    except InvalidTokenError:
        # token 无效
        return Result.error("Invalid token", code=401), None


def jwt_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        from common.response import Result
        # 获取请求头中的 Authorization 的值
        auth_header = request.headers.get('Authorization', None)
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            # 验证 token
            payload, new_token = validate_jwt_token(token)
            if isinstance(payload, Result):
                return payload  # 返回 token 错误的响应

            # 将 user_id 加入 request 供后续使用
            request.user_id = payload['user_id']

            # 如果有新 token，包含在响应头里
            response = func(request, *args, **kwargs)
            if new_token:
                response['Authorization'] = f'Bearer {new_token}'
            return response

        else:
            return Result.error('Authorization header missing or invalid', code=401)

    return wrapper


if __name__ == '__main__':
    user_id = '1'
    token = generate_jwt_token(user_id)
    print(validate_jwt_token(token))
