import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Blueprint, redirect, request, session, url_for, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Set up Spotify OAuth authentication
sp = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private playlist-read-private"
                        )

# Define Flask Blueprint
SpotifyAuth = Blueprint("SpotifyAuth", __name__)

# Route 1 Redirect user to Spotify login
@SpotifyAuth.route("/login")
def login():
        spotify_url = sp.get_authorize_url()
        return redirect(spotify_url)

        # Route 2: Handle Spotify callback and get access token
@SpotifyAuth.route("/callback")
def callback():
    code = request.args.get("code")

    if not code:
        return jsonify({"error": "Authorization failed"}), 400

    token_info = sp.get_access_token(code)
    session["access_token"] = token_info["access_token"]

    return redirect(url_for("SpotifyAuth.get_playlists"))  # Redirect to playlist route



#route 3 type sht

@SpotifyAuth.route("/playlists")
def get_playlists():
    
    access_token = session.get("access_token")
    print("Debugging")
    if not access_token:
    #redirect back to login 
        print("No accesstoken, redirecting to login")
        return redirect(url_for("SpotifyAuth.login")) 
    try:    
    #make access token to make a request to Spotify API 
        sp_api = spotipy.Spotipy(auth=access_token)
        user_playlists = sp_api.current_user_playlists()
        print("API Response: ", user_playlists)

    #were extracting names from files. Making a for loop  
        playlists = [{"name": pl["name"], "id": pl["id"]} for pl in user_playlists.get("items", [])]
        return jsonify(playlists)

    except Exception as e:
        print("Error fetching playlists:", str(e))
        return jsonify({"error": "Failed to fetch playlists"}), 500  
    






























