import sys
from pathlib import Path

from spotag import app, m4a, spotify

app.init()


def entry_point():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: smt <track_id> <file_path>")
        sys.exit(1)

    api = spotify.Api(app.config)

    track_id, filepath = args[0], Path(args[1])

    if not filepath.exists():
        print(f"File {filepath} does not exist")
        sys.exit(1)

    track = api.track(track_id)

    if filepath.suffix == ".m4a":
        m4a.set_meta(track, filepath)
    else:
        print("Unsupported file type. Feel free to submit a PR")
        sys.exit(1)


if __name__ == "__main__":
    entry_point()
