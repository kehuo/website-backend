# @File: resource.py
# @Author: Kevin Huo
# @Date: 2020/9/24

from flask_restful import Resource, reqparse
from common.utils import encoding_resp_utf8
from core.auth.logics.current_user import get_current_user


class CurrentUser(Resource):
    def get(self):
        # try:
        #     verify_jwt_in_request()
        #
        # except Exception as e:
        #     return {'errorCode': 'Unauthorized Access Token', 'errorMessage': '无效的access token'}, 401
        # current_user = get_jwt_identity()
        # db = global_var['db']
        # res = get_current_user(global_var['db'], current_user)

        res = get_current_user()

        return encoding_resp_utf8(res)