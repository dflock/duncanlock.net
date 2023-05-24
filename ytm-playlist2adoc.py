from ytmusicapi import YTMusic
import json
import sys

tmp = sys.stdin.read()
playlist = json.loads(tmp)

def fmt(s):
    return s.replace("|", "")

if playlist:
    print(
        f"## https://music.youtube.com/playlist?list={playlist['id']}[{playlist['title']}]\n\n"
    )
    print(f"{playlist['description']}")

    if playlist["tracks"]:

        print("[.scrollable]")
        print('[cols="3,2,2,1"]')
        print("|===")
        print("|Title|Artist|Album|Duration")
        print()

        for track in playlist["tracks"]:
            if track["thumbnails"]:
                img = (
                    f"image:{track['thumbnails'][0]['url']}[thumbnail,40,40,role=bare]"
                )
            else:
                img = ""

            print(f"|{img}{fmt(track['title'])}")
            print(f"|{track['artists'][0]['name']}")
            if track["album"] and track["album"]["name"]:
                print(f"|{track['album']['name']}")
            else:
                print("|")
            print(f"|{track['duration']}")

        print("|===")
        print()
