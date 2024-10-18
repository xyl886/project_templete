# -*- coding: utf-8 -*-

from rest_framework import serializers


class AuthRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, help_text="用户名")
    password = serializers.CharField(required=True, help_text="密码")


class TokenizeRequestSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, help_text="待分词文本")
    coarse = serializers.BooleanField(required=False, default=False, help_text="是否使用粗分词")
    auth = serializers.CharField(required=False, default='66180068eaf668ab781f17fe', help_text="hanlp认证码")
    language = serializers.CharField(required=False, default='zh', help_text="语言")
    is_stopword = serializers.BooleanField(required=False, default=False, help_text="是否使用数据库停用词过滤")
    error_correct = serializers.BooleanField(required=False, default=False, help_text="是否使用纠错")
    api_key = serializers.CharField(required=False, default='sk-0cb9d59b17c343768e50fde8a9c4b9a8', help_text="API Key")


class TokenizeResponseSerializer(serializers.Serializer):
    tokens = serializers.ListField(child=serializers.CharField())
    pos_tags = serializers.ListField(child=serializers.CharField())
