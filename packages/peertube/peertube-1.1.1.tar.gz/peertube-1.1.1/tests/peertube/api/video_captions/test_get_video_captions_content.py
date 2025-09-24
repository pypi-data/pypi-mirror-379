"""Tests for get_video_captions_content function."""

from peertube.api.video_captions.get_video_captions_content import (
    get_video_captions_content,
)
from peertube.client import Client
from peertube.models.get_video_captions_response_200 import GetVideoCaptionsResponse200
from peertube.models.video_caption import VideoCaption
from peertube.models.video_constant_string_language import VideoConstantStringLanguage


def test_get_captions_content_success(httpx_mock):
    """Test successful caption content retrieval."""
    # Create client
    client = Client(base_url="https://peertube.example.com")

    # Mock caption data
    language = VideoConstantStringLanguage(id="en", label="English")
    caption = VideoCaption(
        language=language, caption_path="/api/v1/videos/test-video/captions/en"
    )
    caption.additional_properties = {
        "fileUrl": "https://peertube.example.com/caption/en.vtt"
    }
    captions_response = GetVideoCaptionsResponse200(total=1, data=[caption])

    # Mock HTTP response for captions list
    httpx_mock.add_response(
        method="GET",
        url="https://peertube.example.com/api/v1/videos/test-video/captions",
        json=captions_response.to_dict(),
        status_code=200,
    )

    # Mock HTTP response for VTT content
    sample_vtt_content = """WEBVTT

00:00:00.000 --> 00:00:02.000
Hello world!

00:00:02.000 --> 00:00:04.000
This is a test caption.
"""
    httpx_mock.add_response(
        method="GET",
        url="https://peertube.example.com/caption/en.vtt",
        content=sample_vtt_content.encode("utf-8"),
        status_code=200,
    )

    # Test the function
    result = get_video_captions_content(client=client, id="test-video")

    assert result == sample_vtt_content
