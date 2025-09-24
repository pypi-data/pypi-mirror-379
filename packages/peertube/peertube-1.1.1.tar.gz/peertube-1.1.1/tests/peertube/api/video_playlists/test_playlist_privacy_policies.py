"""Tests for playlist_privacy_policies function."""

from peertube.api.video_playlists.playlist_privacy_policies import sync


def test_playlist_privacy_policies_success(httpx_mock, client):
    """Test successful retrieval of playlist privacy policies."""
    # Sample response data
    sample_data = ["public", "unlisted", "private"]

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/video-playlists/privacies",
        status_code=200,
        json=sample_data,
    )

    # Test the function
    result = sync(client=client)

    assert result is not None
    assert len(result) == 3
    assert "public" in result
    assert "unlisted" in result
    assert "private" in result
