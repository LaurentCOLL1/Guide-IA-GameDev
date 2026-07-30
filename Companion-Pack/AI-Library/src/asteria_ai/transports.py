from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Mapping
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .cancellation import CancellationToken
from .errors import ProtocolError, TransportError


@dataclass(frozen=True)
class HttpResult:
    status_code: int
    headers: dict[str, str]
    payload: dict


class HttpJsonTransport:
    def post_json(
        self,
        *,
        url: str,
        payload: dict,
        headers: Mapping[str, str],
        timeout_seconds: float,
        max_response_bytes: int,
        cancellation: CancellationToken,
    ) -> HttpResult:
        cancellation.raise_if_cancelled()
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        request = Request(
            url,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json", "Accept": "application/json", **dict(headers)},
        )
        try:
            with urlopen(request, timeout=timeout_seconds) as response:
                raw = response.read(max_response_bytes + 1)
                status = int(response.status)
                response_headers = {key: value for key, value in response.headers.items()}
        except HTTPError as exc:
            raw = exc.read(max_response_bytes + 1)
            status = int(exc.code)
            if len(raw) > max_response_bytes:
                raise TransportError("Réponse d’erreur trop volumineuse.", status_code=status)
            retryable = status in {408, 425, 429, 500, 502, 503, 504}
            raise TransportError(
                f"Erreur HTTP {status}.", status_code=status, retryable=retryable
            ) from exc
        except URLError as exc:
            raise TransportError("Service local inaccessible.", retryable=True) from exc
        cancellation.raise_if_cancelled()
        if len(raw) > max_response_bytes:
            raise TransportError("Réponse trop volumineuse.", status_code=status)
        try:
            decoded = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ProtocolError("Réponse JSON invalide.") from exc
        if not isinstance(decoded, dict):
            raise ProtocolError("La réponse JSON doit être un objet.")
        return HttpResult(status, response_headers, decoded)
