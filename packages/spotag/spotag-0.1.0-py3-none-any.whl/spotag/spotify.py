import datetime
import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from typing import List, Optional

from spotag import app, models


class SpotifyApiError(Exception):
    """
    Base class for all exceptions related to Spotify Api.
    """


class TrackError(SpotifyApiError):
    """
    Base class for all exceptions related to track.
    """


@dataclass
class Token:
    access_token: str = ""
    token_type: str = ""
    expires_in: int = 0
    expires_in_abs: float = 0.0

    def __post_init__(self):
        buffer = 10
        if self.expires_in_abs == 0:
            expires_in_abs = datetime.datetime.now() + datetime.timedelta(
                seconds=self.expires_in - buffer
            )
            self.expires_in_abs = expires_in_abs.timestamp()

    def read(self):
        try:
            with open(app.CONFIG_DIR.joinpath("token.json"), "r") as f:
                data = f.read()
                self.__init__(**json.loads(data))
        except (FileNotFoundError, json.JSONDecodeError):
            self.write()
            return None

    def write(self):
        with open(app.CONFIG_DIR.joinpath("token.json"), "w") as f:
            f.write(json.dumps(self.dict, indent=4))

    def is_valid(self) -> bool:
        return datetime.datetime.now().timestamp() < self.expires_in_abs

    @property
    def dict(self) -> dict:
        return asdict(self)


@dataclass
class Credits:
    performers: List[str]
    writers: List[str]
    producers: List[str]
    source_names: List[str]


@dataclass
class Track:
    id: str
    name: str
    artists: List[str]
    artists_id: List[str]
    album_name: str
    album_artist: str
    album_type: str
    cover_url: str
    duration: int
    year: int
    date: str
    track_number: int
    tracks_count: int
    album_id: str
    explicit: bool
    popularity: int
    url: str
    isrc: Optional[str]

    @property
    def cover(self):
        if not self.cover_url:
            return b""
        try:
            with urllib.request.urlopen(self.cover_url) as res:
                return res.read()
        except Exception as e:
            raise TrackError(e)


@dataclass
class Album:
    album_type: str
    total_tracks: int
    id: str
    cover_url: str
    name: str
    artists: List[str]
    artists_id: List[str]
    popularity: int

    label: str
    copyright: List[str]

    year: int
    date: str

    @property
    def cover(self):
        if not self.cover_url:
            return b""
        try:
            with urllib.request.urlopen(self.cover_url) as res:
                return res.read()
        except Exception as e:
            raise TrackError(e)


@dataclass
class Api:
    def __init__(self, c: models.Config):
        self._t = Token()
        self._c = c
        self.init()

    def init(self):
        self._t.read()
        if self._t.is_valid():
            return
        try:
            url = "https://accounts.spotify.com/api/token"
            body = urllib.parse.urlencode(
                {
                    "grant_type": "client_credentials",
                    "client_id": self._c.spotify_client_id,
                    "client_secret": self._c.spotify_client_secret,
                }
            ).encode()
            req_headers = {"Content-Type": "application/x-www-form-urlencoded"}

            req = urllib.request.Request(url, data=body, headers=req_headers)

            with urllib.request.urlopen(req) as res:
                data_str = res.read().decode("utf-8")
                data = json.loads(data_str)
                self._t = Token(**data)
                self._t.write()
        except urllib.error.HTTPError as e:
            if e.code == 400:
                raise SpotifyApiError("Invalid client id or secret, please check your config")
            raise SpotifyApiError(e)

    def track(self, track_id: str):
        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"Bearer {self._t.access_token}")
        with urllib.request.urlopen(req) as res:
            data_str = res.read().decode("utf-8")
            d = json.loads(data_str)
            return Track(
                id=d["id"],
                name=d["name"],
                artists=[a["name"] for a in d["artists"]],
                album_name=d["album"]["name"],
                album_artist=d["album"]["artists"][0]["name"],
                duration=d["duration_ms"],
                year=d["album"]["release_date"].split("-")[0],
                date=d["album"]["release_date"],
                track_number=d["track_number"],
                tracks_count=d["album"]["total_tracks"],
                explicit=d["explicit"],
                url=d["external_urls"]["spotify"],
                cover_url=d["album"]["images"][0]["url"],
                album_id=d["album"]["id"],
                artists_id=[a["id"] for a in d["artists"]],
                album_type=d["album"]["album_type"],
                popularity=d["popularity"],
                isrc=d.get("external_ids", {}).get("isrc", None),
            )

    def album(self, album_id: str):
        url = f"https://api.spotify.com/v1/albums/{album_id}"
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"Bearer {self._t.access_token}")
        with urllib.request.urlopen(req) as res:
            data_str = res.read().decode("utf-8")
            d = json.loads(data_str)
            return Album(
                album_type=d["album_type"],
                total_tracks=d["total_tracks"],
                id=d["id"],
                cover_url=d["images"][0]["url"],
                name=d["name"],
                artists=[a["name"] for a in d["artists"]],
                artists_id=[a["id"] for a in d["artists"]],
                popularity=d["popularity"],
                label=d["label"],
                copyright=[x["text"] for x in d["copyrights"]],
                year=d["release_date"].split("-")[0],
                date=d["release_date"],
            )
