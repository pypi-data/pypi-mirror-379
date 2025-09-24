"""Tests for mirrored_videos function."""

from peertube.api.video_mirroring.mirrored_videos import sync
from peertube.models.get_mirrored_videos_target import GetMirroredVideosTarget


def test_mirrored_videos_success(httpx_mock, auth_client):
    """Test successful retrieval of mirrored videos."""
    # Sample response data
    sample_data = [
        {
            "id": 3,
            "name": "Mirrored Video 1",
            "url": "https://example.com/mirrored1",
            "uuid": "7a7ae5e6-0a1e-484a-b099-e80766180a6b",
        },
    ]

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/server/redundancy/videos?target=remote-videos&count=15",
        status_code=200,
        json=sample_data,
    )

    # Test the function
    result = sync(client=auth_client, target=GetMirroredVideosTarget.REMOTE_VIDEOS)

    assert result is not None
    assert len(result) == 1
    assert result[0].id == 3
    assert result[0].name == "Mirrored Video 1"
