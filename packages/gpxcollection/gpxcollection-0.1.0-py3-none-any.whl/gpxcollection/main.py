#!/usr/bin/env python3
"""
GPX Collection Viewer
Generates static HTML pages with Leaflet maps for GPX file collections.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
import markdown


class GPXParser:
    """Parse GPX files and extract track data."""
    
    def __init__(self):
        self.ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}
    
    def parse_gpx(self, file_path: str) -> Dict:
        """Parse a GPX file and return track data."""
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            tracks = []
            waypoints = []
            
            # Extract tracks
            for trk in root.findall('.//gpx:trk', self.ns):
                track_name = trk.find('gpx:name', self.ns)
                track_name = track_name.text if track_name is not None else "Unnamed Track"
                
                track_points = []
                for trkpt in trk.findall('.//gpx:trkpt', self.ns):
                    lat = float(trkpt.get('lat'))
                    lon = float(trkpt.get('lon'))
                    track_points.append([lat, lon])
                
                if track_points:
                    tracks.append({
                        'name': track_name,
                        'points': track_points
                    })
            
            # Extract waypoints
            for wpt in root.findall('.//gpx:wpt', self.ns):
                lat = float(wpt.get('lat'))
                lon = float(wpt.get('lon'))
                name = wpt.find('gpx:name', self.ns)
                name = name.text if name is not None else "Waypoint"
                waypoints.append({
                    'name': name,
                    'lat': lat,
                    'lon': lon
                })
            
            return {
                'tracks': tracks,
                'waypoints': waypoints,
                'file_name': os.path.basename(file_path)
            }
            
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return {'tracks': [], 'waypoints': [], 'file_name': os.path.basename(file_path)}


class GPXCollectionGenerator:
    """Generate static HTML pages for GPX collections."""
    
    def __init__(self, input_dir: str, output_dir: str, mapbox_outdoor_token: str = None, mapbox_satellite_token: str = None):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.mapbox_outdoor_token = mapbox_outdoor_token
        self.mapbox_satellite_token = mapbox_satellite_token
        self.parser = GPXParser()
        
        # Setup Jinja2 template environment
        template_dir = Path(__file__).parent / "templates"
        self.env = Environment(loader=FileSystemLoader(template_dir))
        
    def scan_collections(self) -> Dict[str, Dict]:
        """Scan input directory for GPX collections."""
        collections = {}

        for subdir in self.input_dir.iterdir():
            if subdir.is_dir():
                collection_name = subdir.name
                gpx_files = []

                for gpx_file in sorted(subdir.glob("*.gpx")):
                    gpx_data = self.parser.parse_gpx(str(gpx_file))
                    if gpx_data['tracks'] or gpx_data['waypoints']:
                        gpx_data['source_path'] = str(gpx_file)
                        gpx_files.append(gpx_data)

                # Check for index.md file
                markdown_content = None
                index_md_path = subdir / "index.md"
                if index_md_path.exists():
                    with open(index_md_path, 'r', encoding='utf-8') as f:
                        markdown_content = f.read()

                if gpx_files:
                    collections[collection_name] = {
                        'gpx_files': gpx_files,
                        'markdown_content': markdown_content
                    }

        return collections
    
    def calculate_center(self, gpx_files: List[Dict]) -> Tuple[float, float]:
        """Calculate the center point of all tracks in a collection using bounding box center."""
        all_lats = []
        all_lons = []
        
        for gpx_file in gpx_files:
            for track in gpx_file['tracks']:
                for point in track['points']:
                    all_lats.append(point[0])
                    all_lons.append(point[1])
            for waypoint in gpx_file['waypoints']:
                all_lats.append(waypoint['lat'])
                all_lons.append(waypoint['lon'])
        
        if not all_lats:
            return (0.0, 0.0)
        
        # Use bounding box center instead of simple average for better results
        min_lat, max_lat = min(all_lats), max(all_lats)
        min_lon, max_lon = min(all_lons), max(all_lons)
        
        center_lat = (min_lat + max_lat) / 2.0
        center_lon = (min_lon + max_lon) / 2.0
        
        return (center_lat, center_lon)
    
    def generate_overview_page(self, collections: Dict[str, Dict]):
        """Generate the main overview page with collection markers."""
        collection_markers = []
        collections_data = []

        for collection_name, collection_data in collections.items():
            gpx_files = collection_data['gpx_files']
            center_lat, center_lon = self.calculate_center(gpx_files)
            track_count = sum(len(gpx['tracks']) for gpx in gpx_files)
            waypoint_count = sum(len(gpx['waypoints']) for gpx in gpx_files)
            
            collection_markers.append({
                'name': collection_name,
                'lat': center_lat,
                'lon': center_lon,
                'count': len(gpx_files)
            })
            
            collections_data.append({
                'name': collection_name,
                'gpx_count': len(gpx_files),
                'track_count': track_count,
                'waypoint_count': waypoint_count
            })
        
        template = self.env.get_template('overview.html')
        html_content = template.render(
            collections=collections_data,
            collection_markers=collection_markers,
            mapbox_outdoor_token=self.mapbox_outdoor_token,
            mapbox_satellite_token=self.mapbox_satellite_token
        )
        
        output_file = self.output_dir / "index.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def generate_collection_page(self, collection_name: str, collection_data: Dict):
        """Generate a detailed page for a single collection."""
        gpx_files = collection_data['gpx_files']
        markdown_content = collection_data['markdown_content']

        tracks_data = []
        waypoints_data = []

        for gpx_file in gpx_files:
            for track in gpx_file['tracks']:
                tracks_data.append({
                    'name': f"{gpx_file['file_name']} - {track['name']}",
                    'points': track['points'],
                    'file_name': gpx_file['file_name']
                })
            for waypoint in gpx_file['waypoints']:
                waypoints_data.append({
                    'name': f"{gpx_file['file_name']} - {waypoint['name']}",
                    'lat': waypoint['lat'],
                    'lon': waypoint['lon'],
                    'file_name': gpx_file['file_name']
                })

        # Render markdown content to HTML if available
        markdown_html = None
        if markdown_content:
            md = markdown.Markdown(extensions=['extra', 'codehilite'])
            markdown_html = md.convert(markdown_content)

        template = self.env.get_template('collection.html')
        html_content = template.render(
            collection_name=collection_name,
            gpx_files=gpx_files,
            tracks=tracks_data,
            waypoints=waypoints_data,
            markdown_content=markdown_html,
            mapbox_outdoor_token=self.mapbox_outdoor_token,
            mapbox_satellite_token=self.mapbox_satellite_token
        )
        
        # Create collection folder and place index.html inside it
        collection_dir = self.output_dir / collection_name
        collection_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy GPX files to the collection directory
        for gpx_file in gpx_files:
            if 'source_path' in gpx_file:
                source_path = Path(gpx_file['source_path'])
                dest_path = collection_dir / gpx_file['file_name']
                shutil.copy2(source_path, dest_path)
        
        output_file = collection_dir / "index.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def generate(self):
        """Generate all HTML pages."""
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Scan for collections
        print(f"Scanning {self.input_dir} for GPX collections...")
        collections = self.scan_collections()
        
        if not collections:
            print("No GPX collections found!")
            return
        
        print(f"Found {len(collections)} collections:")
        for name, collection_data in collections.items():
            gpx_count = len(collection_data['gpx_files'])
            has_markdown = collection_data['markdown_content'] is not None
            print(f"  - {name}: {gpx_count} GPX files{' (with content)' if has_markdown else ''}")

        # Generate overview page
        print("Generating overview page...")
        self.generate_overview_page(collections)

        # Generate collection pages
        for collection_name, collection_data in collections.items():
            print(f"Generating page for collection: {collection_name}")
            self.generate_collection_page(collection_name, collection_data)
        
        print(f"Generated static pages in {self.output_dir}")
        print(f"Open {self.output_dir}/index.html in your browser to view")


def main():
    parser = argparse.ArgumentParser(
        description="Generate static HTML pages with Leaflet maps for GPX file collections"
    )
    parser.add_argument(
        "input_dir",
        help="Input directory containing subdirectories with GPX files"
    )
    parser.add_argument(
        "output_dir",
        help="Output directory for generated HTML pages"
    )
    parser.add_argument(
        "--mapbox_outdoor_token",
        help="Mapbox access token for outdoor map layer"
    )
    parser.add_argument(
        "--mapbox_satellite_token",
        help="Mapbox access token for satellite map layer"
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input_dir)
    if not input_path.exists():
        print(f"Error: Input directory '{input_path}' does not exist!")
        sys.exit(1)
    
    if not input_path.is_dir():
        print(f"Error: '{input_path}' is not a directory!")
        sys.exit(1)
    
    generator = GPXCollectionGenerator(args.input_dir, args.output_dir, args.mapbox_outdoor_token, args.mapbox_satellite_token)
    generator.generate()

