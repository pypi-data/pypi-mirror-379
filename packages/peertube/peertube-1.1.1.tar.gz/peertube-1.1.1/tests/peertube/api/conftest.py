"""Shared fixtures for API tests."""

import pytest


@pytest.fixture
def sample_playlist_data():
    """Sample playlist data used across playlist tests."""
    return {
        "id": 123,
        "displayName": "Test Playlist",
        "description": "A test playlist",
        "privacy": {"id": 1, "label": "Public"},
        "type": {"id": 1, "label": "Regular"},
        "createdAt": "2023-01-01T00:00:00.000Z",
        "updatedAt": "2023-01-01T00:00:00.000Z",
    }


@pytest.fixture
def sample_playlist_response_data(sample_playlist_data):
    """Sample playlist response data with total and data array."""
    return {
        "total": 1,
        "data": [sample_playlist_data],
    }


@pytest.fixture
def sample_detailed_playlist_data():
    """Detailed playlist data with all fields for comprehensive tests."""
    return {
        "id": 1,
        "uuid": "12345678-1234-5678-1234-567812345678",
        "url": "https://example.com/playlists/playlist-uuid-1",
        "displayName": "My Playlist 1",
        "shortDescription": "A short description",
        "description": "A longer description",
        "isLocal": True,
        "ownerAccount": {
            "id": 1,
            "name": "@user@example.com",
            "displayName": "User",
            "url": "https://example.com/accounts/user",
            "host": "example.com",
            "avatar": None,
        },
        "createdAt": "2023-01-01T00:00:00.000Z",
        "updatedAt": "2023-01-01T00:00:00.000Z",
        "type": {"id": 1, "label": "Regular"},
        "privacy": {"id": 1, "label": "Public"},
        "videosLength": 5,
        "thumbnailPath": "/static/thumbnails/playlists/playlist-uuid-1.jpg",
    }


@pytest.fixture
def sample_playlist_response_data_detailed(sample_detailed_playlist_data):
    """Sample detailed playlist response data with multiple playlists."""
    return {
        "total": 2,
        "data": [
            sample_detailed_playlist_data,
            {
                **sample_detailed_playlist_data,
                "id": 2,
                "uuid": "87654321-4321-8765-4321-876543218765",
                "url": "https://example.com/playlists/playlist-uuid-2",
                "displayName": "My Playlist 2",
                "shortDescription": "Another short description",
                "description": "Another longer description",
                "videosLength": 3,
                "thumbnailPath": "/static/thumbnails/playlists/playlist-uuid-2.jpg",
            },
        ],
    }


@pytest.fixture
def sample_video_feed_data():
    """Sample video feed data for syndicated subscription videos."""
    return [
        {
            "media:title": "Test Video 1",
            "link": "https://example.com/videos/watch/123",
            "guid": "123",
            "pubDate": "2023-01-01T12:00:00Z",
            "description": "A test video description",
        },
        {
            "media:title": "Test Video 2",
            "link": "https://example.com/videos/watch/456",
            "guid": "456",
            "pubDate": "2023-01-02T12:00:00Z",
            "description": "Another test video description",
        },
    ]


@pytest.fixture
def sample_mirrored_video_data():
    """Sample mirrored video data."""
    return [
        {
            "id": 1,
            "name": "Test Video 1",
            "url": "https://example.com/video1",
            "uuid": "9c9de5e8-0a1e-484a-b099-e80766180a6d",
        },
        {
            "id": 2,
            "name": "Test Video 2",
            "url": "https://example.com/video2",
            "uuid": "8b8ce5e7-0a1e-484a-b099-e80766180a6c",
        },
    ]


@pytest.fixture
def sample_owner_account_data():
    """Sample owner account data used in playlist and video objects."""
    return {
        "id": 1,
        "name": "@user@example.com",
        "displayName": "User",
        "url": "https://example.com/accounts/user",
        "host": "example.com",
        "avatar": None,
    }


@pytest.fixture
def sample_privacy_data():
    """Sample privacy data."""
    return {"id": 1, "label": "Public"}


@pytest.fixture
def sample_playlist_type_data():
    """Sample playlist type data."""
    return {"id": 1, "label": "Regular"}
