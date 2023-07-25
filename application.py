from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@application.route('/status')
def status():
    return {'status': 'OK', 'code': 200}

if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0')
