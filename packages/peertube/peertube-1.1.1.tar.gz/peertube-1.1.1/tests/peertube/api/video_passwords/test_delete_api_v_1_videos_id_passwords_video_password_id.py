from peertube.api.video_passwords.delete_api_v_1_videos_id_passwords_video_password_id import (  # noqa: E501
    sync,
)


class TestDeleteApiV1VideosIdPasswordsVideoPasswordId:
    def test_sync(self, auth_client, httpx_mock):
        # Mock the API response
        httpx_mock.add_response(
            method="DELETE",
            url="https://test.peertube.example/api/v1/videos/123/passwords/456",
            status_code=204,
        )

        # Call the sync function
        result = sync(id=123, video_password_id=456, client=auth_client)

        # Assert the result
        assert result is None
