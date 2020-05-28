from flask import Flask, send_from_directory, make_response, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api

app = Flask(__name__)
CORS(app)


@app.route('/static/<path:path>')
def send_statis(path):
    return send_from_directory('static', path)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "flask_swagger"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(request_api.get_blueprint())


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
