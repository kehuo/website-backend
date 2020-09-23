# @File: app.py.py
# @Author: Kevin Huo
# @Date: 2020/9/23

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.init_route import init_route_func

# 1
app = Flask(__name__)
config_file_path = "../service.conf"
app.config.from_pyfile(config_file_path, silent=True)

# 2. api
api_version = "api/%s" % app.config['API_VERSION']
cors = CORS(app, resources={r'/{}/*'.format(api_version): {'origins': '*', 'supports_credentials': True}})
api = Api(app)

# 3. route
init_route_func(api, api_version)
