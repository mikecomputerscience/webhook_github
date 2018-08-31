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
        request_dict = request.json
        author_name = request_dict['commits'][0]['author']['name']
        request_str = json.dumps(request_dict)
        print('*****start*****')
        print(author_name)
        # print(request_str)
        print('------end------')
        return request_str


if __name__ == '__main__':
    app.run(debug=True)
