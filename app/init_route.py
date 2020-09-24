# @File: init_route.py
# @Author: Kevin Huo
# @Date: 2020/9/23


from common.utils import app_url
from core.welcome.resource import Welcome
from core.auth.resource import CurrentUser
from core.misc.resource import AboutMe


def init_route_func(api, api_version):
    """
    :param api: flask api object
    :param api_version: "v1"
    """
    api.add_resource(Welcome, app_url(api_version, "welcome", "/get_welcome_data"))

    api.add_resource(CurrentUser, app_url(api_version, "auth", "/current_user"))

    api.add_resource(AboutMe, app_url(api_version, "misc", "/about_me"))
