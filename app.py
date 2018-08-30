from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! Changed~'


@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        github_info = json.dumps(request.json)
        print(github_info)
        return github_info


if __name__ == '__main__':
    app.run(debug=True)
