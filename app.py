import glob

import flask
from flask import Flask

app = Flask(__name__)


@app.route('/helloworld')
def hello_world():  # put application's code here
    return ['Hello World!']


@app.route('/byeworld')
def bye_world():  # put application's code here
    return ['Bye World!']


@app.route('/bye/<name>', methods=['GET'])
def bye_name(name):  # put application's code here
    cookies = flask.Request.cookies
    print(cookies)
    response = flask.make_response([f"Bye {name}"])
    response.set_cookie('subscribed', 'true')
    return response


@app.route('/image/<number>')
def images(number):

    return flask.send_file(f"images\\{number}_img.png")


if __name__ == '__main__':
    app.run()
