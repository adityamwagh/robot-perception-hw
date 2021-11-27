import numpy as np
import open3d as o3d


pcd = o3d.io.read_point_cloud("hw2/record_00348.pcd", format='pcd')
print(f"Data : {repr(np.asarray(pcd.points))}")


def ransac():
    pass
