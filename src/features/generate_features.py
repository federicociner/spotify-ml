from spotipy.oauth2 import SpotifyClientCredentials
from dotenvy import load_env, read_file
import os
import pandas as pd
import numpy as np
import spotipy


def access_spotify(filepath):
    sp = spotipy.Spotify()
    load_env(read_file(filepath))
    cid = os.environ.get("SPOTIPY_CLIENT_ID")
    secret = os.environ.get("SPOTIPY_CLIENT_SECRET")

    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    token = client_credentials_manager.get_access_token()
    sp = spotipy.Spotify(auth=token)

    return sp


def get_song_ids(sp, username, playlist_id):
    playlist = sp.user_playlist(username, playlist_id)

    tracks = playlist["tracks"]
    songs = tracks["items"]
    while tracks["next"]:
        tracks = sp.next(tracks)
        [songs.append(item) for item in tracks["items"]]

    # get song IDs from the track list
    song_ids = [songs[i]["track"]["id"] for i in range(0, len(songs))]

    # remove songs that have no ID (where ID == None) and return list
    song_ids = filter(lambda x: x is not None, song_ids)
    return song_ids


def get_features(sp, song_ids, label_value=0, as_array=False):
    features = []

    # get dictionaries of features for a list of song IDs
    for i in range(0, len(song_ids), 50):
        audio_features = sp.audio_features(song_ids[i : i + 50])
        for track in audio_features:
            if track is not None:
                features.append(track)
                features[len(features) - 1]["class"] = label_value

    # convert to data frame remove irrelevant features
    df = pd.DataFrame(features)
    non_features = ["analysis_url", "id", "track_href", "type", "uri"]
    df.drop(labels=non_features, axis=1, inplace=True)

    # move class column to the left of the dataframe
    col_class = df["class"]
    df.drop(labels=["class"], axis=1, inplace=True)
    df.insert(0, "class", col_class)

    if as_array:
        return df.as_matrix()

    return df


def get_new_features(sp, username, playlist_id):
    playlist = sp.user_playlist(username, playlist_id)

    # get track and song data
    tracks = playlist["tracks"]
    songs = tracks["items"]
    song_ids = get_song_ids(sp, username, playlist_id)
    features = []
    j = 0

    # get dictionaries of features for a list of song IDs
    for i in range(0, len(song_ids), 50):
        audio_features = sp.audio_features(song_ids[i : i + 50])
        for track in audio_features:
            if track is not None:
                track["song_title"] = songs[j]["track"]["name"]
                track["artist"] = songs[j]["track"]["artists"][0]["name"]
                j = j + 1
                features.append(track)

    return pd.DataFrame(features)


def combine_features(datasets, type="ndarray"):
    if type == "ndarray":
        return np.concatenate(datasets, axis=0)
    elif type == "dataframe":
        return pd.concat(datasets)


def save_features(df, filename):
    data_dir = os.path.join(os.getcwd(), os.pardir, "data", filename)
    df.to_csv(path_or_buf=data_dir, sep=",", header=True, index=False)
