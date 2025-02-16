from flask import Flask, jsonify
from Spotify2Auth import SpotifyAuth
from dotenv import load_dotenv
import os




load_dotenv() 

print("Importing Flask")

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "59c9acad6578287b7eb7773ea11663bee64ff1733f6014f9957bfbfee197db2c")

app.register_blueprint(SpotifyAuth)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
