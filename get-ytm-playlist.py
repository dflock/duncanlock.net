from ytmusicapi import YTMusic
import json
import sys

playlist_id = sys.argv[1]

if playlist_id:

    ytmusic = YTMusic()

    playlist = ytmusic.get_playlist(playlistId=playlist_id)

    if playlist:
        print(json.dumps(playlist, indent=4))
