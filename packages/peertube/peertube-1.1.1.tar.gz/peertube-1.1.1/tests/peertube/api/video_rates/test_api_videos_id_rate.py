"""Tests for api_videos_id_rate function."""

from peertube.api.video_rates.api_videos_id_rate import sync
from peertube.models.put_api_v1_videos_id_rate_body import PutApiV1VideosIdRateBody
from peertube.models.put_api_v1_videos_id_rate_body_rating import (
    PutApiV1VideosIdRateBodyRating,
)


def test_api_videos_id_rate_success(httpx_mock, auth_client):
    """Test successful video rating."""
    # Create request body
    body = PutApiV1VideosIdRateBody(rating=PutApiV1VideosIdRateBodyRating.LIKE)

    # Mock HTTP response
    httpx_mock.add_response(
        method="PUT",
        url="https://test.peertube.example/api/v1/videos/123/rate",
        status_code=204,
    )

    # Test the function
    result = sync(id=123, client=auth_client, body=body)

    assert result is None
