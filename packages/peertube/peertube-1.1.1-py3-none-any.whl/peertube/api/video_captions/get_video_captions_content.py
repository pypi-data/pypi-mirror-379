"""Get video captions content as text."""

from __future__ import annotations

from typing import Any
from urllib.parse import urljoin
from uuid import UUID

from pydantic import BaseModel, ConfigDict, validate_call

from peertube.api.video_captions.get_video_captions import (
    sync as get_video_captions_sync,
)
from peertube.client import AuthenticatedClient, Client
from peertube.types import UNSET


class CaptionNormalized(BaseModel):
    """Normalized caption data."""

    lang: str | None = None
    url: str

    @classmethod
    def from_raw(cls, cap: Any, base_url: str) -> CaptionNormalized | None:
        """Convert raw caption to normalized form."""
        # Extract language safely, coalescing UNSET to None
        lang_obj = getattr(cap, "language", UNSET)
        lang = None if lang_obj is UNSET else getattr(lang_obj, "id", None)
        if lang is UNSET:
            lang = None

        # Prefer explicit fileUrl, fallback to caption_path
        file_url = getattr(cap, "additional_properties", {}).get("fileUrl")
        if not file_url:
            caption_path = getattr(cap, "caption_path", UNSET)
            if caption_path is UNSET or caption_path is None:
                return None
            # Robustly join base URL and possibly-relative path
            file_url = urljoin(str(base_url).rstrip("/") + "/", str(caption_path))

        return cls(lang=lang, url=file_url)


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def get_video_captions_content(
    client: AuthenticatedClient | Client,
    id: UUID | int | str,
    language_filter: str | None = "en",
    *,
    x_peertube_video_password: str | None = None,
) -> str:
    """Get the content of video captions as a string.

    This function wraps get_video_captions to retrieve caption metadata,
    then downloads the VTT file content for the specified language.

    Args:
        client: PeerTube client instance
        id: Video identifier
        language_filter: Language code to filter captions (default: "en")
        x_peertube_video_password: Video-related parameter

    Returns:
        The VTT file content as a string

    Raises:
        ValueError: If no captions are available or specified language not found
        httpx.HTTPError: For network-related issues when downloading captions
        UnicodeDecodeError: If VTT content cannot be decoded as UTF-8
    """
    captions_response = get_video_captions_sync(
        client=client,
        id=id,
        x_peertube_video_password=UNSET
        if x_peertube_video_password is None
        else x_peertube_video_password,
    )

    data = getattr(captions_response, "data", None) or []
    normalized = [
        c for c in (CaptionNormalized.from_raw(c, client.base_url) for c in data) if c
    ]
    if not normalized:
        msg = "No captions available for this video."
        raise ValueError(msg)

    if language_filter:
        selected = next((c for c in normalized if c.lang == language_filter), None)
        if not selected:
            available = sorted({c.lang for c in normalized if c.lang})
            msg = f"Caption language '{language_filter}' not found. Available: {available}"
            raise ValueError(msg)
    else:
        selected = normalized[0]

    r = client.get_httpx_client().get(selected.url)
    r.raise_for_status()
    try:
        return r.content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise UnicodeDecodeError(
            exc.encoding,
            exc.object,
            exc.start,
            exc.end,
            "Failed to decode caption content as UTF-8",
        ) from exc
