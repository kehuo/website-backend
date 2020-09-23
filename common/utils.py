# @File: utils.py
# @Author: Kevin Huo
# @Date: 2020/9/23

import json
from flask import Response


def app_url(version, model, name):
    """
    /v1/welcome/get_welcome_data
    """
    name = "/%s/%s%s" % (version, model, name)
    # name = '/{}/{}{}'.format(version, model, name)
    return name


def encoding_resp_utf8(data):
    json_response = json.dumps(data, ensure_ascii=False)
    response = Response(json_response, content_type="application/json; charset=utf-8")
    return response
