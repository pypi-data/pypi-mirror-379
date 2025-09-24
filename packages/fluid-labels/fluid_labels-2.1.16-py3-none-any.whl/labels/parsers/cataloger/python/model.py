from typing import NamedTuple


class WheelEggMetadata(NamedTuple):
    dependencies: list[str] | None = None


class WheelEggPackageData(NamedTuple):
    name: str
    version: str
    metadata: WheelEggMetadata | None = None
