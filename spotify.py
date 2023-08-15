import requests
import urllib.parse


def get_token():
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "5a9853fe71d74a57a8a4047fdcb90416",
        "client_secret": "5fff91519fd54a9189dd0eaa21d3ef73"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Error:", response.status_code)


def get_artist(artist_id, access_token):
    url = "https://api.spotify.com/v1/artists/" + artist_id
    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)


def get_top_tracks(artist_id, access_token):
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks?market=FR"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)


def get_albums(artist_id, access_token):
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/albums?market=FR&limit=1"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)


def format_string(string):
    url_compliant_string = urllib.parse.quote_plus(string)
    return url_compliant_string


def search(query, query_type, access_token):
    url = "https://api.spotify.com/v1/search?q=" + query + "&type=" + query_type + "&market=FR&limit=5"
    headers = {
        "Authorization": "Bearer " + access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)


def ms_to_min_sec(milliseconds):
    seconds = milliseconds / 1000
    minutes = seconds // 60
    seconds %= 60
    return f"{int(minutes)}:{int(seconds):02}"


if __name__ == "__main__":
    print("Hi!")
