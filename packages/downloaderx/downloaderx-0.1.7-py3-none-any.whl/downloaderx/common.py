from typing import Mapping, MutableMapping
from dataclasses import dataclass

from .retry import Retry


@dataclass
class HTTPOptions:
  url: str
  timeout: float
  retry: Retry
  headers: Mapping[str, str | bytes | None] | None
  cookies: MutableMapping[str, str] | None