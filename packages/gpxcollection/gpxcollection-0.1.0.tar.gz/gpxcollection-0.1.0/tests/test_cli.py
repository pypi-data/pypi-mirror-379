"""Tests for command line interface."""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch
from gpxcollection.main import main


class TestCLI:
    """Test cases for the command line interface."""

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

    def test_main_with_valid_arguments(self, fixtures_dir, temp_output_dir):
        """Test main function with valid input and output directories."""
        test_args = [
            "gpxcollection",
            str(fixtures_dir),
            str(temp_output_dir)
        ]

        with patch('sys.argv', test_args):
            main()

        # Check that output was generated
        assert (temp_output_dir / "index.html").exists()
        assert (temp_output_dir / "hiking-trails").is_dir()

    def test_main_with_mapbox_tokens(self, fixtures_dir, temp_output_dir):
        """Test main function with Mapbox tokens."""
        test_args = [
            "gpxcollection",
            str(fixtures_dir),
            str(temp_output_dir),
            "--mapbox_outdoor_token", "test_outdoor",
            "--mapbox_satellite_token", "test_satellite"
        ]

        with patch('sys.argv', test_args):
            main()

        # Check that tokens are in the output
        overview_file = temp_output_dir / "index.html"
        content = overview_file.read_text(encoding='utf-8')
        assert "test_outdoor" in content
        assert "test_satellite" in content

    def test_main_with_nonexistent_input_dir(self, temp_output_dir, capsys):
        """Test main function with non-existent input directory."""
        test_args = [
            "gpxcollection",
            "/nonexistent/path",
            str(temp_output_dir)
        ]

        with patch('sys.argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1

        # Check error message
        captured = capsys.readouterr()
        assert "does not exist" in captured.out

    def test_main_with_file_as_input_dir(self, temp_output_dir, capsys):
        """Test main function with file instead of directory as input."""
        # Create a temporary file
        temp_file = temp_output_dir / "not_a_directory.txt"
        temp_file.write_text("test")

        test_args = [
            "gpxcollection",
            str(temp_file),
            str(temp_output_dir)
        ]

        with patch('sys.argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1

        # Check error message
        captured = capsys.readouterr()
        assert "is not a directory" in captured.out

    def test_main_creates_output_directory(self, fixtures_dir):
        """Test that main function creates output directory if it doesn't exist."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "new_output_dir"

            test_args = [
                "gpxcollection",
                str(fixtures_dir),
                str(output_dir)
            ]

            with patch('sys.argv', test_args):
                main()

            # Check that output directory was created and contains files
            assert output_dir.exists()
            assert output_dir.is_dir()
            assert (output_dir / "index.html").exists()