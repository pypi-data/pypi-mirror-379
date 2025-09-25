"""Tests for GPX parsing functionality."""

import pytest
from pathlib import Path
from gpxcollection.main import GPXParser


class TestGPXParser:
    """Test cases for the GPXParser class."""

    @pytest.fixture
    def parser(self):
        """Create a GPXParser instance for testing."""
        return GPXParser()

    @pytest.fixture
    def fixtures_dir(self):
        """Get the fixtures directory path."""
        return Path(__file__).parent / "fixtures" / "input"

    def test_parse_mountain_trail_gpx(self, parser, fixtures_dir):
        """Test parsing a GPX file with tracks and waypoints."""
        gpx_file = fixtures_dir / "hiking-trails" / "mountain-trail.gpx"
        result = parser.parse_gpx(str(gpx_file))

        assert result['file_name'] == "mountain-trail.gpx"
        assert len(result['tracks']) == 1
        assert len(result['waypoints']) == 1

        # Test track data
        track = result['tracks'][0]
        assert track['name'] == "Mountain Trail Track"
        assert len(track['points']) == 4
        assert track['points'][0] == [47.6062, -122.3321]
        assert track['points'][-1] == [47.6092, -122.3351]

        # Test waypoint data
        waypoint = result['waypoints'][0]
        assert waypoint['name'] == "Viewpoint"
        assert waypoint['lat'] == 47.6087
        assert waypoint['lon'] == -122.3346

    def test_parse_lake_loop_gpx(self, parser, fixtures_dir):
        """Test parsing a GPX file with multiple waypoints."""
        gpx_file = fixtures_dir / "hiking-trails" / "lake-loop.gpx"
        result = parser.parse_gpx(str(gpx_file))

        assert result['file_name'] == "lake-loop.gpx"
        assert len(result['tracks']) == 1
        assert len(result['waypoints']) == 2

        # Test circular track (starts and ends at same point)
        track = result['tracks'][0]
        assert track['name'] == "Lake Loop Trail"
        assert len(track['points']) == 5
        assert track['points'][0] == track['points'][-1]  # Loop should close

        # Test waypoint names
        waypoint_names = [wp['name'] for wp in result['waypoints']]
        assert "Lake Center" in waypoint_names
        assert "Picnic Area" in waypoint_names

    def test_parse_city_tour_gpx(self, parser, fixtures_dir):
        """Test parsing a cycling route GPX file."""
        gpx_file = fixtures_dir / "cycling-routes" / "city-tour.gpx"
        result = parser.parse_gpx(str(gpx_file))

        assert result['file_name'] == "city-tour.gpx"
        assert len(result['tracks']) == 1
        assert len(result['waypoints']) == 1

        track = result['tracks'][0]
        assert track['name'] == "Downtown Route"
        assert len(track['points']) == 4

        waypoint = result['waypoints'][0]
        assert waypoint['name'] == "Coffee Shop"

    def test_parse_running_track_gpx(self, parser, fixtures_dir):
        """Test parsing a running track GPX file."""
        gpx_file = fixtures_dir / "running-tracks" / "morning-jog.gpx"
        result = parser.parse_gpx(str(gpx_file))

        assert result['file_name'] == "morning-jog.gpx"
        assert len(result['tracks']) == 1
        assert len(result['waypoints']) == 0  # No waypoints in this file

        track = result['tracks'][0]
        assert track['name'] == "Neighborhood Loop"
        assert len(track['points']) == 5
        # Test it's a loop
        assert track['points'][0] == track['points'][-1]

    def test_parse_nonexistent_file(self, parser):
        """Test parsing a file that doesn't exist."""
        result = parser.parse_gpx("nonexistent.gpx")

        assert result['file_name'] == "nonexistent.gpx"
        assert result['tracks'] == []
        assert result['waypoints'] == []

    def test_parse_invalid_gpx(self, parser, tmp_path):
        """Test parsing an invalid GPX file."""
        invalid_gpx = tmp_path / "invalid.gpx"
        invalid_gpx.write_text("This is not valid XML")

        result = parser.parse_gpx(str(invalid_gpx))

        assert result['file_name'] == "invalid.gpx"
        assert result['tracks'] == []
        assert result['waypoints'] == []