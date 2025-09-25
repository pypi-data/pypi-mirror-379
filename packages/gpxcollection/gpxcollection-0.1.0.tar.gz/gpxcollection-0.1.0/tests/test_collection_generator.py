"""Tests for GPX collection generation functionality."""

import pytest
from pathlib import Path
import tempfile
import shutil
from gpxcollection.main import GPXCollectionGenerator


class TestGPXCollectionGenerator:
    """Test cases for the GPXCollectionGenerator class."""

    @pytest.fixture
    def fixtures_dir(self):
        """Get the fixtures directory path."""
        return Path(__file__).parent / "fixtures" / "input"

    @pytest.fixture
    def temp_output_dir(self):
        """Create a temporary output directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def generator(self, fixtures_dir, temp_output_dir):
        """Create a GPXCollectionGenerator instance for testing."""
        return GPXCollectionGenerator(
            str(fixtures_dir),
            str(temp_output_dir)
        )

    def test_scan_collections(self, generator):
        """Test scanning input directory for GPX collections."""
        collections = generator.scan_collections()

        # Should find all three collections
        assert len(collections) == 3
        assert "hiking-trails" in collections
        assert "cycling-routes" in collections
        assert "running-tracks" in collections

        # Test hiking-trails collection
        hiking = collections["hiking-trails"]
        assert len(hiking['gpx_files']) == 2
        assert hiking['markdown_content'] is not None

        # Test cycling-routes collection
        cycling = collections["cycling-routes"]
        assert len(cycling['gpx_files']) == 1
        assert cycling['markdown_content'] is None

        # Test running-tracks collection
        running = collections["running-tracks"]
        assert len(running['gpx_files']) == 1
        assert running['markdown_content'] is None

    def test_calculate_center_single_track(self, generator, fixtures_dir):
        """Test calculating center point for a single track."""
        collections = generator.scan_collections()
        running_files = collections["running-tracks"]['gpx_files']

        center_lat, center_lon = generator.calculate_center(running_files)

        # Should be roughly in the center of the track points
        assert 47.65 <= center_lat <= 47.652
        assert -122.301 <= center_lon <= -122.299

    def test_calculate_center_multiple_tracks(self, generator):
        """Test calculating center point for multiple tracks."""
        collections = generator.scan_collections()
        hiking_files = collections["hiking-trails"]['gpx_files']

        center_lat, center_lon = generator.calculate_center(hiking_files)

        # Should be somewhere between the two trail areas
        assert 47.60 <= center_lat <= 47.63
        assert -122.35 <= center_lon <= -122.33

    def test_calculate_center_empty_collection(self, generator):
        """Test calculating center with no tracks."""
        center_lat, center_lon = generator.calculate_center([])
        assert center_lat == 0.0
        assert center_lon == 0.0

    def test_generate_creates_output_structure(self, generator, temp_output_dir):
        """Test that generate() creates the expected output structure."""
        generator.generate()

        # Check main index.html exists
        assert (temp_output_dir / "index.html").exists()

        # Check collection directories exist
        assert (temp_output_dir / "hiking-trails").is_dir()
        assert (temp_output_dir / "cycling-routes").is_dir()
        assert (temp_output_dir / "running-tracks").is_dir()

        # Check collection index files exist
        assert (temp_output_dir / "hiking-trails" / "index.html").exists()
        assert (temp_output_dir / "cycling-routes" / "index.html").exists()
        assert (temp_output_dir / "running-tracks" / "index.html").exists()

    def test_generate_copies_gpx_files(self, generator, temp_output_dir):
        """Test that GPX files are copied to output directories."""
        generator.generate()

        # Check that GPX files are copied
        hiking_dir = temp_output_dir / "hiking-trails"
        assert (hiking_dir / "mountain-trail.gpx").exists()
        assert (hiking_dir / "lake-loop.gpx").exists()

        cycling_dir = temp_output_dir / "cycling-routes"
        assert (cycling_dir / "city-tour.gpx").exists()

        running_dir = temp_output_dir / "running-tracks"
        assert (running_dir / "morning-jog.gpx").exists()

    def test_generate_overview_page_content(self, generator, temp_output_dir):
        """Test that the overview page contains expected content."""
        generator.generate()

        overview_file = temp_output_dir / "index.html"
        content = overview_file.read_text(encoding='utf-8')

        # Should contain collection names
        assert "hiking-trails" in content
        assert "cycling-routes" in content
        assert "running-tracks" in content

        # Should contain Leaflet map code
        assert "L.map" in content

    def test_generate_collection_page_content(self, generator, temp_output_dir):
        """Test that collection pages contain expected content."""
        generator.generate()

        hiking_file = temp_output_dir / "hiking-trails" / "index.html"
        content = hiking_file.read_text(encoding='utf-8')

        # Should contain GPX file names
        assert "mountain-trail.gpx" in content
        assert "lake-loop.gpx" in content

        # Should contain markdown content
        assert "Hiking Trails Collection" in content
        assert "Trail Difficulty" in content

        # Should contain map JavaScript
        assert "tracks" in content
        assert "waypoints" in content

    def test_generator_with_mapbox_tokens(self, fixtures_dir, temp_output_dir):
        """Test generator with Mapbox tokens."""
        generator = GPXCollectionGenerator(
            str(fixtures_dir),
            str(temp_output_dir),
            mapbox_outdoor_token="test_outdoor_token",
            mapbox_satellite_token="test_satellite_token"
        )

        generator.generate()

        # Check that tokens are included in HTML
        overview_file = temp_output_dir / "index.html"
        content = overview_file.read_text(encoding='utf-8')
        assert "test_outdoor_token" in content
        assert "test_satellite_token" in content