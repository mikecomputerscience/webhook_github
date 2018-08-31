from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return 'hello world, 123'


@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        info_dict = request.json
        info_str = json.dumps(request.json)
        print('*****start*****')
        print(info_dict['commits'][0]['author']['name'])
        print(info_str)
        print('------end------')
        return info_str


if __name__ == '__main__':
    app.run(debug=True)
