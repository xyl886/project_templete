# -*- coding: utf-8 -*-

from flask import jsonify


class Result:
    def __init__(self, success=True, message='', data=None, status_code=200):
        self.success = success
        self.message = message
        self.data = data
        self.status_code = status_code

    def to_dict(self):
        response = {
            'success': self.success,
            'message': self.message,
            'data': self.data
        }
        return response

    def to_json(self):
        return jsonify(self.to_dict()), self.status_code

    @classmethod
    def success(cls, message='', data=None, status_code=200):
        return cls(success=True, message=message, data=data, status_code=status_code)

    @classmethod
    def error(cls, message='', data=None, status_code=400):
        return cls(success=False, message=message, data=data, status_code=status_code)
