# @File: resources.py
# @Author: Kevin Huo
# @Date: 2020/9/23


from flask_restful import Resource, reqparse
from common.utils import encoding_resp_utf8
from core.logics.welcome import get_welcome_data


class Welcome(Resource):
    def get(self, **auth):
        parser = reqparse.RequestParser()
        # parser.add_argument('page', type=int, required=False, location='args')
        # parser.add_argument('pageSize', type=int, required=False, location='args')
        parser.add_argument('count', type=int, required=False, location='args')
        args = parser.parse_args()

        res = get_welcome_data(args)

        return encoding_resp_utf8(res)
