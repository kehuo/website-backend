# @File: resource.py
# @Author: Kevin Huo
# @Date: 2020/9/24


from flask_restful import Resource, reqparse
from common.utils import encoding_resp_utf8
from core.auth.logics.current_user import get_current_user


class AboutMe(Resource):
    def get(self):
        res = get_current_user()

        return encoding_resp_utf8(res)