# Spotify playlist

## run
- create a playlists.csv file with a playlist id on each line
- set env variable `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` to your spotify application credentials
- run `python spotify_playlist/get_tracks.py`
- run `python spotify_playlist/get_artists.py`

## test
before running tests for the first time run
```sh
poetry install
```

### execute tests
to run test you must set your spotify credential in environment variable like below

```sh
export SPOTIFY_CLIENT_ID_TEST=xxxxxxxxxx
export SPOTIFY_CLIENT_SECRET_TEST=xxxxxxxxxxx
poetry run pytest
```

### calculate coverage
```sh
export SPOTIFY_CLIENT_ID_TEST=xxxxxxxxxx
export SPOTIFY_CLIENT_SECRET_TEST=xxxxxxxxxxx
coverage run -m pytest && coverage report -m
```

