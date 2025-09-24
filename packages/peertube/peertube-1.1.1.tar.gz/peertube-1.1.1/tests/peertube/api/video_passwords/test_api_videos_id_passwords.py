"""Tests for api_videos_id_passwords function."""

from peertube.api.video_passwords.api_videos_id_passwords import sync
from peertube.models.video_password_list import VideoPasswordList
from peertube.types import UNSET


def test_api_videos_id_passwords_success(httpx_mock, auth_client):
    """Test successful retrieval of video passwords."""
    # Mock response data
    response_data = {
        "total": 1,
        "data": [
            {
                "id": 123,
                "label": "Test Password",
                "createdAt": "2023-01-01T00:00:00.000Z",
            }
        ],
    }

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/videos/123/passwords?count=15",
        json=response_data,
        status_code=200,
    )

    # Test the function
    result = sync(
        id=123,
        client=auth_client,
        start=UNSET,
        count=15,
        sort=UNSET,
    )

    # Assert result is the expected model
    expected = VideoPasswordList.from_dict(response_data)
    assert result == expected
