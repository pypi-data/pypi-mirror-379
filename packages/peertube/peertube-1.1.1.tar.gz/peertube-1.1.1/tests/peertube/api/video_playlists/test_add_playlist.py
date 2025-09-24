"""Tests for add_playlist function."""

from peertube.api.video_playlists.add_playlist import sync
from peertube.models.add_playlist_body import AddPlaylistBody
from peertube.models.video_playlist_privacy_set import VideoPlaylistPrivacySet


def test_add_playlist_success(httpx_mock, auth_client):
    """Test successful playlist creation."""
    # Create request body
    body = AddPlaylistBody(
        display_name="Test Playlist",
        privacy=VideoPlaylistPrivacySet(1),  # Public
        description="A test playlist",
        video_channel_id=42,
    )

    # Mock response data
    response_data = {
        "id": 123,
        "displayName": "Test Playlist",
        "description": "A test playlist",
        "privacy": {"id": 1, "label": "Public"},
        "videoChannelId": 42,
        "createdAt": "2023-01-01T00:00:00.000Z",
        "updatedAt": "2023-01-01T00:00:00.000Z",
    }

    # Mock HTTP response
    httpx_mock.add_response(
        method="POST",
        url="https://test.peertube.example/api/v1/video-playlists",
        json=response_data,
        status_code=201,
    )

    # Test the function
    result = sync(client=auth_client, body=body)

    assert result == response_data
