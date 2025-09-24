"""Tests for del_mirrored_video function."""

from peertube.api.video_mirroring.del_mirrored_video import sync


def test_del_mirrored_video_success(httpx_mock, auth_client):
    """Test successful deletion of mirrored video."""
    # Mock HTTP response
    httpx_mock.add_response(
        method="DELETE",
        url="https://test.peertube.example/api/v1/server/redundancy/videos/test-redundancy-id",
        status_code=204,
    )

    # Test the function
    result = sync(redundancy_id="test-redundancy-id", client=auth_client)

    assert result is None
