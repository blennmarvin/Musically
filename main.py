import sys

import spotify
from spotify import ms_to_min_sec as converter
from spotify import format_string as formatting
import argparse

if len(sys.argv) == 3:
    query = sys.argv[2]
access_token = spotify.get_token()
result_choice = ""


def main():
    parser = argparse.ArgumentParser(description="A simple tool to retrieve datas about your favorite "
                                                 "artist/album/song.")

    parser.add_argument('--track', help='Search for a track')
    parser.add_argument('--album', help='Search for an album')
    parser.add_argument('--artist', help='Search for an artist')

    args = parser.parse_args()

    if args.track:
        track_info()

    if args.album:
        album_info()

    if args.artist:
        artist_info()


def track_info():
    results = spotify.search(formatting(query), 'track', access_token)
    results_tracks = results['tracks']['items']
    print("We found the following results:\n")
    for song in results_tracks:
        print(f"{song['artists'][0]['name']} - {song['name']}\t{converter(song['duration_ms'])}")


def album_info():
    results = spotify.search(formatting(query), 'album', access_token)
    albums = results['albums']['items']
    print("We found the following results:\n")
    for album in albums:
        print(f"{album['artists'][0]['name']} - {album['name']}\t{album['release_date']}")


def artist_info():
    results = spotify.search(formatting(query), 'artist', access_token)
    artist = results['artists']['items'][0]
    artist_id = results['artists']['items'][0]['id']
    artist_tracks = spotify.get_top_tracks(artist_id, access_token)
    songs = artist_tracks['tracks']

    announce = f"{artist['name']} has {artist['followers']['total']} followers "
    print(announce)
    print("Here are their top tracks:")
    print("-" * len(announce))
    print()
    for song in songs:
        print(f"{song['name']}\t{converter(song['duration_ms'])}")


if __name__ == "__main__":
    main()
