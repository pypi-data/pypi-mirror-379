from pathlib import Path

import mutagen.mp4 as mp4

from spotag.spotify import Track


def set_meta(track: Track, file: Path):
    m = mp4.MP4(file)
    m["©nam"] = track.name
    m["©ART"] = track.artists
    m["aART"] = track.album_artist
    m["©alb"] = track.album_name
    m["©day"] = track.year
    m["trkn"] = [(track.track_number, track.tracks_count)]
    m["©cmt"] = ""  # TODO
    m["covr"] = [mp4.MP4Cover(data=track.cover, imageformat=mp4.MP4Cover.FORMAT_JPEG)]

    m["rtng"] = (4 if track.explicit else 2,)
    m["----:spotag:id"] = str(track.id).encode("utf-8")
    m["----:spotag:popularity"] = str(track.popularity).encode("utf-8")

    m.save()
