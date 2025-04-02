import trimesh
import numpy as np
import pyrender

# Load the GLB file
scene = trimesh.load("YOUR FILE PATH")

# Extract mesh
if isinstance(scene, trimesh.Scene):
    mesh = trimesh.util.concatenate(scene.geometry.values())
else:
    mesh = scene

# Extract XYZ coordinates
vertices = mesh.vertices

# extract vertex colors
if hasattr(mesh.visual, 'vertex_colors') and mesh.visual.vertex_colors is not None:
    colors = mesh.visual.vertex_colors[:, :3]  # Ignore alpha channel
elif hasattr(mesh.visual, 'to_color') and callable(getattr(mesh.visual, 'to_color', None)):
    colors = mesh.visual.to_color().vertex_colors[:, :3]
else:
    # Try to get material color
    print("Vertex colors not found. Attempting to get material colors...")
    try:
        pyrender_mesh = pyrender.Mesh.from_trimesh(mesh)
        material_color = np.array(pyrender_mesh.material.baseColorFactor[:3]) * 255
        colors = np.tile(material_color, (vertices.shape[0], 1))
    except Exception as e:
        print(f"Material color extraction failed: {e}")
        colors = np.full(vertices.shape, 255)  # Default white if nothing works

# Save XYZRGB format
point_cloud = np.hstack((vertices, colors))
np.savetxt("output.txt", point_cloud, fmt="%.6f %.6f %.6f %d %d %d")

print("Point cloud saved as output.txt")
