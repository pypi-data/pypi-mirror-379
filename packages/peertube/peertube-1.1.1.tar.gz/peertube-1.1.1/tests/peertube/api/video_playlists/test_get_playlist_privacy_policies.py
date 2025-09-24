from peertube.api.video_playlists.get_playlist_privacy_policies import sync


class TestGetPlaylistPrivacyPolicies:
    def test_sync(self, client, httpx_mock):
        # Mock the API response
        httpx_mock.add_response(
            method="GET",
            url="https://test.peertube.example/api/v1/video-playlists/privacies",
            json=["public", "private", "unlisted"],
            status_code=200,
        )

        # Call the sync function
        result = sync(client=client)

        # Assert the result
        assert result == ["public", "private", "unlisted"]
