"""Tests for get_syndicated_subscription_videos function."""

import json

from peertube.api.video_feeds.get_syndicated_subscription_videos import sync
from peertube.models.get_syndicated_subscription_videos_format import (
    GetSyndicatedSubscriptionVideosFormat,
)


def test_get_syndicated_subscription_videos_success(
    httpx_mock, client, sample_video_feed_data
):
    """Test successful retrieval of syndicated subscription videos."""
    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/feeds/subscriptions.xml?accountId=test-account&token=test-token",
        status_code=200,
        text=json.dumps(sample_video_feed_data),
    )

    # Test the function
    result = sync(
        format_=GetSyndicatedSubscriptionVideosFormat.XML,
        client=client,
        account_id="test-account",
        token="test-token",  # noqa: S106
    )

    assert result is not None
    assert len(result) == 2
    assert result[0].mediatitle == "Test Video 1"
    assert result[0].guid == "123"
    assert result[1].link == "https://example.com/videos/watch/456"
