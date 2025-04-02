# GLB to Point Cloud Converter

## Overview
This Python script converts a GLB 3D model file into a text file containing point cloud data with both position and color information.

## Installation
Before running the script, you'll need to install the required libraries using pip:

```bash
pip install trimesh pyrender numpy
```

## Functionality
The script performs the following operations:

1. Loads a GLB file using the trimesh library
2. Extracts the 3D mesh data from the loaded file
3. Obtains the XYZ coordinates (vertices) of the mesh
4. Attempts to extract RGB color information through multiple fallback methods:
   - Directly accessing vertex colors
   - Converting visual data to colors
   - Extracting material colors via pyrender
   - Defaulting to white if all else fails
5. Combines the XYZ coordinates with RGB color values
6. Saves the data to "output.txt" with a formatted structure (floating point coordinates and integer colors)

## Output Format
The resulting file contains rows where each row represents a point in the format:

X Y Z R G B

## Applications
This conversion is useful for applications that work with point cloud data rather than mesh data, such as:
- 3D scanning software
- Point cloud visualization tools
- Point-based analysis programs
- Processing pipelines that require raw point data
