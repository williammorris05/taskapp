from flask import Flask

app = Flask(__name__)


@app.route('/post_test', methods=['POST'])
def post_test():
    '''This is just to show how a POST request looks like; no functionality'''

    return '', 201


@app.route('/get_test', methods=['GET'])
def get_test():
    '''This is just a test to show how a GET request looks like'''
    return 'Hello World', 200


@app.route('/login', methods=['POST'])
def login():
    '''Put in a better docstring'''
    return '', 201


@app.route('/register', methods=['POST'])
def register():
    '''Put in a better docstring'''
    return '', 201


# Unsure of what route we'll have and the method used
@app.route('/???', methods=['PUT'])
def invite_to_project():
    '''Put in a better docstring'''
    return '', 201


@app.route('/task', methods=['POST'])
def create_task():
    '''Put in a better docstring'''
    return '', 201


@app.route('/project', methods=['POST'])
def create_project():
    '''Put in a better docstring'''
    return '', 201
