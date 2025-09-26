#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 09:56:44 2025

@author: bacetiner
"""

import geopandas as gpd
from shapely.geometry import box


def filter_geojson_by_bbox(input_file, output_file, minx, miny, maxx, maxy):
    """
    Filters features from a GeoJSON file that fall within a bounding box.

    Parameters:
        input_file (str): Path to the input GeoJSON file.
        output_file (str): Path to save the filtered GeoJSON.
        minx, miny, maxx, maxy (float): Bounding box coordinates.
    """
    # Read the input GeoJSON
    gdf = gpd.read_file(input_file)

    # Create bounding box polygon
    bbox = box(minx, miny, maxx, maxy)

    # Filter features that intersect with the bbox
    filtered_gdf = gdf[gdf.intersects(bbox)]

    # Save the filtered features to a new GeoJSON
    filtered_gdf.to_file(output_file, driver="GeoJSON")

    print(f"Filtered GeoJSON written to: {output_file}")


# Example usage
if __name__ == "__main__":
    # Define input/output and bounding box
    input_geojson = "BayAreaInventory_EQ.geojson"
    output_geojson = "FilteredBayAreaBuildings.geojson"

    # Bounding box coordinates: (minx, miny, maxx, maxy)
    # Example: San Francisco area
    bbox_coords = (-122.448, 37.761, -122.279, 37.854)

    filter_geojson_by_bbox(input_geojson, output_geojson, *bbox_coords)
