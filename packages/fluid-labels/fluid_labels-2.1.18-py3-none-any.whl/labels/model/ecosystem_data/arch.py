from datetime import datetime

from pydantic import BaseModel

from labels.model.metadata import Digest


class AlpmFileRecord(BaseModel):
    path: str
    type: str | None = None
    uid: str | None = None
    gid: str | None = None
    time: datetime | None = None
    size: str | None = None
    link: str | None = None
    digests: list[Digest] | None = None


class AlpmDBEntry(BaseModel):
    licenses: str = ""
    base_package: str = ""
    package: str = ""
    version: str = ""
    description: str = ""
    architecture: str = ""
    size: int = 0
    packager: str = ""
    url: str = ""
    validation: str = ""
    reason: int = 0
    files: list[AlpmFileRecord] | None = None
    backup: list[AlpmFileRecord] | None = None
