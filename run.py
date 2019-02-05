from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

user_list = []
@app.route('/get_hello', methods=['GET'])
def hello():
    return 'This is a python'

@app.route('/adduser', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    new_user = {
        "name": name,
        "email": email
    }

    user_list.append(new_user)
    return make_response(jsonify({
        "Message": "User added succesfully",
        "user name": new_user['name']
    }), 201)

@app.route('/users', methods=['GET'])
def users():
    return make_response(jsonify({
        "users": user_list,
        "status": "Ok"
    }), 200)

if __name__ == '__main__':
    app.run()