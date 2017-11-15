from spotipy.oauth2 import SpotifyClientCredentials
import os
import numpy as np
import pandas as pd
from dotenv import load_env, read_file

import spotipy
import spotipy.util as util
sp = spotipy.Spotify()


def access_spotify(envfile_path):
    load_env(read_file(envfile_path))
    cid = os.environ.get('SPOTIPY_CLIENT_ID')
    secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
    redirect = os.environ.get('SPOTIPY_REDIRECT_URI')
    username = os.environ.get('SPOTIPY_USERNAME')

    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    scope = 'user-library-read playlist-read-private'
    token = util.prompt_for_user_token(username, scope)


def get_song_ids(sp, username, p_playlist_id, n_playlist_id):
    p_playlist =
    n_playlist =