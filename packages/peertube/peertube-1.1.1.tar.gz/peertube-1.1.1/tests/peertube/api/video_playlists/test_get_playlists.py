"""Tests for get_playlists function."""

from peertube.api.video_playlists.get_playlists import sync


def test_get_playlists_success(httpx_mock, client):
    """Test successful retrieval of video playlists."""
    # Sample response data
    sample_data = {
        "total": 2,
        "data": [
            {
                "id": 1,
                "uuid": "9c9de5e8-0a1e-484a-b099-e80766180a6d",
                "displayName": "My Playlist 1",
                "description": "A test playlist",
            },
            {
                "id": 2,
                "uuid": "8b8ce5e7-0a1e-484a-b099-e80766180a6c",
                "displayName": "My Playlist 2",
                "description": "Another test playlist",
            },
        ],
    }

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/video-playlists?count=15",
        status_code=200,
        json=sample_data,
    )

    # Test the function
    result = sync(client=client)

    assert result is not None
    assert result.total == 2
    assert result.data is not None
    assert len(result.data) == 2  # type: ignore[arg-type]
    assert result.data[0].id == 1  # type: ignore[attr-defined]
    assert result.data[0].display_name == "My Playlist 1"  # type: ignore[attr-defined]
    assert result.data[1].id == 2  # type: ignore[attr-defined]
    assert result.data[1].display_name == "My Playlist 2"  # type: ignore[attr-defined]
