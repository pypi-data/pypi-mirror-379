"""Tests for get_mirrored_videos function."""

from peertube.api.video_mirroring.get_mirrored_videos import sync
from peertube.models.get_mirrored_videos_target import GetMirroredVideosTarget


def test_get_mirrored_videos_success(
    httpx_mock, auth_client, sample_mirrored_video_data
):
    """Test successful retrieval of mirrored videos."""
    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/server/redundancy/videos?target=my-videos&count=15",
        status_code=200,
        json=sample_mirrored_video_data,
    )

    # Test the function
    result = sync(client=auth_client, target=GetMirroredVideosTarget.MY_VIDEOS)

    assert result is not None
    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].name == "Test Video 1"
    assert result[1].id == 2
    assert result[1].name == "Test Video 2"
