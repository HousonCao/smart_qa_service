# coding=utf-8
import datetime

import jwt


class TokenHelper:
    JWT_SECRET = 'smart_qa_bot'
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=7)

    @staticmethod
    def generate_token(user_id):
        payload = {
            'user_id': user_id,
            'timestamp': datetime.datetime.utcnow().timestamp(),
            'exp': datetime.datetime.utcnow() + TokenHelper.JWT_EXPIRATION_DELTA
        }
        return jwt.encode(payload, TokenHelper.JWT_SECRET, algorithm=TokenHelper.JWT_ALGORITHM)

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, TokenHelper.JWT_SECRET, algorithms=[TokenHelper.JWT_ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Token expired'
        except jwt.InvalidTokenError:
            return 'Invalid token'

    @staticmethod
    def expire_token(token):
        """TODO"""
