from flask import Flask, send_from_directory, make_response, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api

app = Flask(__name__)
CORS(app)


@app.route('/swagger_data/<path:path>')
def send_swagger(path):
    print('Okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(send_from_directory('static', path))
    return send_from_directory('static', path)


SWAGGER_URL = '/swagger'
API_URL = '/swagger_data/user.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "flask_swagger_hamed"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(request_api.get_blueprint())


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
