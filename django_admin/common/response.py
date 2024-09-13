# -*- coding: utf-8 -*-
from django.http import JsonResponse


class Result(JsonResponse):
    def __init__(self, data=None, code=200, status=200, **kwargs):
        if data is None:
            data = {}
        if 'msg' not in data:
            data['msg'] = ''

        # 设置 HTTP 状态码
        kwargs['status'] = status
        super().__init__(data=data, **kwargs)

    @classmethod
    def success(cls, message='success', data=None, code=200, status=200, **kwargs):
        """
        创建成功响应，默认 HTTP 状态码为 200，业务 code 可自定义
        :param message: 成功消息
        :param data: 响应数据
        :param code: 业务逻辑中的 code
        :param status: HTTP 状态码，默认为 200
        """
        response_data = {
            'code': code,  # 业务 code
            'msg': message,
            'data': data
        }
        if data is None:
            del response_data['data']
        # 处理自定义字段
        response_data.update(kwargs)

        return cls(data=response_data, code=code, status=status)

    @classmethod
    def error(cls, message='error', data=None, code=400, status=200, **kwargs):
        """
        创建错误响应，默认 HTTP 状态码为 400，业务 code 可自定义
        :param message: 错误消息
        :param data: 错误相关数据
        :param code: 业务逻辑中的 code
        :param status: HTTP 状态码，默认为 400
        """
        response_data = {
            'code': code,  # 业务 code
            'msg': message,
            'data': data
        }
        if data is None:
            del response_data['data']
        # 处理自定义字段
        response_data.update(kwargs)

        return cls(data=response_data, code=code, status=status)
