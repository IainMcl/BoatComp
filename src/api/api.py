from flask import Flask

app = Flask(__name__)


@app.route('/graphql')
def hello_world():
    return 'Hello world'
