# -*- coding: utf-8 -*-

from rest_framework.views import exception_handler
from rest_framework.response import Response

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotFound, ValidationError


def custom_exception_handler(exc, context):
    # 调用默认的异常处理器
    response = exception_handler(exc, context)

    # 如果返回的响应为 None，表示未被处理的异常
    if response is None:
        return Response({
            'error': 'Internal Server Error',
            'details': str(exc),
            'status_code': 500,
            'path': context['request'].path,
        }, status=500)

    # 处理不同类型的异常
    if isinstance(exc, ValidationError):
        return Response({
            'error': 'Validation Error',
            'details': exc.detail,
            'status_code': response.status_code,
            'path': context['request'].path,
        }, status=response.status_code)

    if isinstance(exc, NotFound):
        return Response({
            'error': 'Not Found',
            'details': str(exc),
            'status_code': response.status_code,
            'path': context['request'].path,
        }, status=response.status_code)

    if isinstance(exc, APIException):
        return Response({
            'error': exc.default_detail,
            'details': str(exc),
            'status_code': response.status_code,
            'path': context['request'].path,
        }, status=response.status_code)

    # 对于其他未处理的异常
    if response.status_code >= 400:
        return Response({
            'error': response.data.get('detail', 'Something went wrong'),
            'status_code': response.status_code,
            'path': context['request'].path,
        }, status=response.status_code)

    return response
