from typing import cast

from peertube.api.video_playlists.playlists import sync
from peertube.types import UNSET


class TestPlaylists:
    def test_sync(self, client, httpx_mock, sample_playlist_response_data_detailed):
        # Mock the API response
        httpx_mock.add_response(
            method="GET",
            url="https://test.peertube.example/api/v1/video-playlists?count=15",
            json=sample_playlist_response_data_detailed,
            status_code=200,
        )

        # Call the sync function
        result = sync(client=client)

        # Assert the result
        assert result is not None
        assert result.total == 2
        assert result.data is not UNSET
        data = cast("list", result.data)
        assert len(data) == 2
        assert data[0].id == 1
        assert data[0].display_name == "My Playlist 1"
        assert data[1].id == 2
        assert data[1].display_name == "My Playlist 2"
