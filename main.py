import numpy as np
from util.camera_pose_visualizer import CameraPoseVisualizer
import json

# Opening JSON file
with open('config/transforms_train.json') as json_file:
    data = json.load(json_file)

## Where is the object center ?!?

if __name__ == '__main__':
    # argument : the minimum/maximum value of x, y, z
    visualizer = CameraPoseVisualizer([-50, 80], [-90, 50], [0, 50])
    frames = data['frames']
    print(len(frames))


    # argument : extrinsic matrix, color, scaled focal length(z-axis length of frame body of camera
    for i in range(len(frames)):
        c1 = np.array(frames[i]["transform_matrix"])
        visualizer.extrinsic2pyramid(c1, 'c', 10)
    visualizer.show()
