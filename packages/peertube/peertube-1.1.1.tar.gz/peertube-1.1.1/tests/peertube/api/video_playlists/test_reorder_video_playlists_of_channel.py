"""Tests for reorder_video_playlists_of_channel function."""

from peertube.api.video_playlists.reorder_video_playlists_of_channel import sync
from peertube.models.reorder_video_playlists_of_channel_body import (
    ReorderVideoPlaylistsOfChannelBody,
)


def test_reorder_video_playlists_of_channel_success(httpx_mock, auth_client):
    """Test successful reordering of channel playlists."""
    # Create request body
    body = ReorderVideoPlaylistsOfChannelBody(
        start_position=1,
        insert_after_position=2,
    )

    # Mock HTTP response
    httpx_mock.add_response(
        method="POST",
        url="https://test.peertube.example/api/v1/video-channels/test-channel/video-playlists/reorder",
        status_code=204,
    )

    # Test the function
    result = sync(channel_handle="test-channel", client=auth_client, body=body)

    assert result is None
