from flask import Flask, jsonify, request

app = Flask(__name__)

# Empty dictionary (CHECKER tələb edir ki, əvvəlcədən data olmasın!)
users = {}


# -------------------------
# ROOT ENDPOINT ("/")
# -------------------------
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# -------------------------
# /data — return all usernames
# -------------------------
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# -------------------------
# /status — return OK
# -------------------------
@app.route("/status")
def status():
    return "OK"


# -------------------------
# /users/<username> — return full user object
# -------------------------
@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


# -------------------------
# /add_user — POST
# -------------------------
@app.route("/add_user", methods=["POST"])
def add_user():
    # Try to parse JSON
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    # No JSON at all
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Username is required
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Username exists already
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add new user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


# -------------------------
# Run the server
# -------------------------
if __name__ == "__main__":
    app.run()
