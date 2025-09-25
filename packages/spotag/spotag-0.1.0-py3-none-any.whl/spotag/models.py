from dataclasses import asdict, dataclass


class ValidationError(Exception):
    """
    Validation Error
    """


@dataclass
class Config:
    spotify_client_id: str
    spotify_client_secret: str

    def __post_init__(self):
        errs = []

        if self.spotify_client_id:
            if not isinstance(self.spotify_client_id, str):
                errs.append("spotify_client_id must be a string")

        if self.spotify_client_secret:
            if not isinstance(self.spotify_client_secret, str):
                errs.append("spotify_client_secret must be a string")
        if errs:
            raise ValidationError(errs)

    @property
    def dict(self) -> dict:
        return asdict(self)


class NotImplementedError(Exception):
    "Not Implemented  / TODO"
