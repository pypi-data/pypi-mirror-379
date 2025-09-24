"""Tests for get_syndicated_comments function."""

import json

from peertube.api.video_feeds.get_syndicated_comments import sync
from peertube.models.get_syndicated_comments_format import GetSyndicatedCommentsFormat


def test_get_syndicated_comments_success(httpx_mock, client):
    """Test successful retrieval of syndicated comments."""
    # Sample response data
    sample_data = [
        {
            "link": "https://example.com/video/123#comment-1",
            "guid": "comment-1",
            "pubDate": "2023-01-01T12:00:00Z",
            "content:encoded": "This is a test comment",
            "dc:creator": "testuser",
        },
        {
            "link": "https://example.com/video/123#comment-2",
            "guid": "comment-2",
            "pubDate": "2023-01-02T12:00:00Z",
            "content:encoded": "This is another test comment",
            "dc:creator": "anotheruser",
        },
    ]

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/feeds/video-comments.xml",
        status_code=200,
        text=json.dumps(sample_data),
    )

    # Test the function
    result = sync(format_=GetSyndicatedCommentsFormat.XML, client=client)

    assert result is not None
    assert len(result) == 2
    assert result[0].link == "https://example.com/video/123#comment-1"
    assert result[0].guid == "comment-1"
    assert result[1].dccreator == "anotheruser"
