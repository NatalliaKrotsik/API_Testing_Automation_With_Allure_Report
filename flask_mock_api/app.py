from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulate a user database
users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

# Authentication endpoint
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('email') == 'eve.holt@reqres.in' and data.get('password') == 'pistol':
        return jsonify(token='QpwL5tke4Pnpja7X4'), 200
    return jsonify(error='Invalid credentials'), 400

# User fetch endpoint
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify(error="User not found"), 404

# User creation (simulated)
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('email') or not data.get('password'):
        return jsonify(error="Missing email or password"), 400
    return jsonify(id=3, token="fake-token-123"), 201

# User deletion (simulated)
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        return jsonify(message=f"User {user_id} deleted"), 200
    return jsonify(error="User not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
