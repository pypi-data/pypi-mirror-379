"""Tests for get_api_videos_id_stats_user_agent function."""

from peertube.api.video_stats.get_api_videos_id_stats_user_agent import sync


def test_get_api_videos_id_stats_user_agent_success(httpx_mock, auth_client):
    """Test successful retrieval of video stats by user agent."""
    # Sample response data
    sample_data = {
        "clients": [
            {"name": "Chrome", "viewers": 150.5},
            {"name": "Firefox", "viewers": 75.2},
        ],
        "devices": [
            {"name": "desktop", "viewers": 200.0},
            {"name": "mobile", "viewers": 25.7},
        ],
        "operatingSystem": [
            {"name": "Windows", "viewers": 120.3},
            {"name": "macOS", "viewers": 80.2},
        ],
    }

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/videos/123/stats/user-agent",
        status_code=200,
        json=sample_data,
    )

    # Test the function
    result = sync(id=123, client=auth_client)

    assert result is not None
    assert result.clients is not None
    assert len(result.clients) == 2  # type: ignore[arg-type]
    assert result.clients[0].name == "Chrome"  # type: ignore[attr-defined]
    assert result.clients[0].viewers == 150.5  # type: ignore[attr-defined]
    assert result.devices is not None
    assert len(result.devices) == 2  # type: ignore[arg-type]
    assert result.devices[0].name.value == "desktop"  # type: ignore[attr-defined]
    assert result.operating_system is not None
    assert len(result.operating_system) == 2  # type: ignore[arg-type]
    assert result.operating_system[1].name == "macOS"  # type: ignore[attr-defined]
