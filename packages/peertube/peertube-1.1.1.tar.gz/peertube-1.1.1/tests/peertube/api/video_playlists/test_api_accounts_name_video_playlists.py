"""Tests for api_accounts_name_video_playlists function."""

from peertube.api.video_playlists.api_accounts_name_video_playlists import sync
from peertube.models.get_api_v1_accounts_name_video_playlists_response_200 import (
    GetApiV1AccountsNameVideoPlaylistsResponse200,
)
from peertube.types import UNSET


def test_api_accounts_name_video_playlists_success(
    httpx_mock, client, sample_playlist_response_data
):
    """Test successful retrieval of account playlists."""
    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/accounts/test-account/video-playlists?count=15",
        json=sample_playlist_response_data,
        status_code=200,
    )

    # Test the function
    result = sync(
        name="test-account",
        client=client,
        start=UNSET,
        count=15,
        sort=UNSET,
        search=UNSET,
        playlist_type=UNSET,
    )

    # Assert result is the expected model
    expected = GetApiV1AccountsNameVideoPlaylistsResponse200.from_dict(
        sample_playlist_response_data
    )
    assert result == expected
