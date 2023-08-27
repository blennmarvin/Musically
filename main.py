import spotify
from spotify import ms_to_min_sec as converter
from spotify import format_string as formatting
import argparse
import getpass
import sys

access_token = spotify.get_token()


def main():
    try:
        parser = argparse.ArgumentParser(description="A simple tool to retrieve datas about your favorite "
                                                     "artist/album/song.")

        parser.add_argument('--track', help='Search for a track')
        parser.add_argument('--album', help='Search for an album')
        parser.add_argument('--artist', help='Search for an artist')

        args = parser.parse_args()

        if args.track:
            track_info(args.track)

        elif args.album:
            album_info(args.album)

        elif args.artist:
            artist_info(args.artist)
        else:
            print("Please enter an option. Try --help to see how to use this tool")
    except TypeError:
        print("Options can not be null.")
    except KeyboardInterrupt:
        print("\nExiting the program.")
        sys.exit()


def track_info(query):
    results = spotify.search(formatting(query), 'track', access_token)
    results_tracks = results['tracks']['items']
    print("We found the following results:\n")
    for song in results_tracks:
        print(f"{song['artists'][0]['name']} - {song['name']}\t{converter(song['duration_ms'])}\
        \t{song['album']['release_date']}")


def album_info(query):
    results = spotify.search(formatting(query), 'album', access_token)
    albums = results['albums']['items']
    ids = [album['id'] for album in albums]

    print("We found the following results:\n")
    for album in albums:
        print(f"{album['artists'][0]['name']} - {album['name']}")

    print()
    while True:
        choice = getpass.getpass('Press a number [0-4] to retrieve info on an album...\n')
        try:
            for num in ids:
                if int(choice) == ids.index(num):
                    print()
                    spotify.tracklist(num, access_token)
            if int(choice) >= 4:
                print("Enter a valid choice")
                continue
            break
        except ValueError:
            print("Enter a valid choice")
            continue


def artist_info(query):
    results = spotify.search(formatting(query), 'artist', access_token)
    artist = results['artists']['items'][0]
    artist_id = results['artists']['items'][0]['id']
    artist_tracks = spotify.get_top_tracks(artist_id, access_token)
    songs = artist_tracks['tracks']

    # Calculate the maximum lengths of the columns
    max_name_length = max(len(song['name']) for song in songs)
    max_duration_length = max(len(converter(song['duration_ms'])) for song in songs)

    # Print the header
    announce = f"{artist['name']} has {artist['followers']['total']} followers "
    print(announce)
    print("Here are their top tracks:")
    # print("-" * (len(announce)-1))
    print()

    # Print each song
    for song in songs:
        name = song['name'].ljust(max_name_length)
        duration = converter(song['duration_ms']).ljust(max_duration_length)
        release_date = song['album']['release_date']
        print(f"{name} {duration} {release_date}")


if __name__ == "__main__":
    main()
