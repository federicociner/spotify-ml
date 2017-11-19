from spotipy.oauth2 import SpotifyClientCredentials
from dotenvy import load_env, read_file
import os
import numpy as np
import pandas as pd
import spotipy


def access_spotify(envfile_path):
    sp = spotipy.Spotify()
    load_env(read_file(envfile_path))
    cid = os.environ.get('SPOTIPY_CLIENT_ID')
    secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    token = client_credentials_manager.get_access_token()
    sp = spotipy.Spotify(auth=token)

    return sp


def get_song_ids(sp, username, p_playlist_id, n_playlist_id):
    p_playlist = sp.user_playlist(username, p_playlist_id)
    n_playlist = sp.user_playlist(username, n_playlist_id)

    p_tracks = p_playlist['tracks']
    p_songs = p_tracks['items']
    while p_tracks['next']:
        p_tracks = sp.next(p_tracks)
        [p_songs.append(item) for item in p_tracks['items']]

    n_tracks = n_playlist['tracks']
    n_songs = n_tracks['items']
    while n_tracks['next']:
        n_tracks = sp.next(n_tracks)
        [n_songs.append(item) for item in n_tracks['items']]

    p_ids = [p_songs[i]['track']['id'] for i in range(0, len(p_songs))]
    n_ids = [n_songs[i]['track']['id'] for i in range(0, len(n_songs))]

    return (p_ids, n_ids)


def get_features(sp, p_ids, n_ids):
    features = []

    # get JSON extract of features and label positive and negative classes
    for i in range(0, len(p_ids), 100):
        audio_features = sp.audio_features(p_ids[i:i + 100])
        for track in audio_features:
            features.append(track)
            features[-1]['class'] = 1

    for i in range(0, len(n_ids), 100):
        audio_features = sp.audio_features(n_ids[i:i + 100])
        for track in audio_features:
            features.append(track)
            features[-1]['class'] = 0

    # convert to data frame remove irrelevant features
    df = pd.DataFrame(features)
    non_features = ['analysis_url', 'id', 'track_href', 'type', 'uri']
    df.drop(labels=non_features, axis=1, inplace=True)

    # move class column to the left of the dataframe
    col_class = df['class']
    df.drop(labels=['class'], axis=1, inplace=True)
    df.insert(0, 'class', col_class)

    return df


def save_features(df, filename):
    data_dir = os.path.join(os.getcwd(), os.pardir, 'data', filename)
    df.to_csv(path_or_buf=data_dir, sep=",", header=True, index=False)
