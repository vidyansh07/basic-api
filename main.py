from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    return jsonify({
        "user_id": user_id,
        "name": "John Doe",
        "age": 30,
        "email": "jonh@gmail.com"
    })

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

@app.route("/get-user", methods=["POST"])
def get_user_by_post():
    data = request.get_json
    return jsonify({
        "user_id": user_id,
        "name": "John Doe",
        "age": 30,
        "email": ""
        
    })

        


if __name__ == "__main__":
    app.run(debug=True)
    
    
