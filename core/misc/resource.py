# @File: resource.py
# @Author: Kevin Huo
# @Date: 2020/9/24


from flask_restful import Resource, reqparse
from common.utils import encoding_resp_utf8
from core.misc.logics.about_me import get_about_me_data


class AboutMe(Resource):
    def get(self):
        res = get_about_me_data()

        return encoding_resp_utf8(res)