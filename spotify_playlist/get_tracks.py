from spotify_playlist.api.spotify import Spotify
from spotify_playlist.datasets.tracks import Tracks
import datetime

def parse_tracks(extract_date, playlist_id, tracks, result):
  for item in tracks.get("items", []):
    for artist in item.get("track", {}).get("artists", []):
      row = {
        Tracks.PLAYLIST_ID: playlist_id,
        Tracks.TRACK_ID: item.get("track").get("id"),
        Tracks.ARTIST_ID: artist.get("id"),
        Tracks.DATE: extract_date
      }
      result.append(row)


def main(current_date = datetime.datetime.now().date()):
  spotify_client = Spotify()
  spotify_client.authenticate()

  filename = "playlist.csv"
  with open(filename) as f:
    playlists = f.readlines()

    result = []
    for playlist_id in playlists:
        tracks = spotify_client.playlist_tracks(playlist_id)
        parse_tracks(current_date, playlist_id, tracks, result)
        Tracks.write(result, f"tracks_{current_date.isoformat()}.csv")

if __name__ == "__main__":
  main()
