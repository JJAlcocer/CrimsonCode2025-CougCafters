from flask import Flask, jsonify

print("Importing Flask")

app = Flask(__name__)

print("test print for debugging")

@app.route("/")
def home():
    return jsonify({"message": "Flask backend should work"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
