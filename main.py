from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'location': 'New York'
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        'age': 25,
        'location': 'San Francisco'
    }
]

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

# Endpoint to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'age': data['age'],
        'location': data['location']
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
