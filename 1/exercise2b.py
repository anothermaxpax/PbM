import pybullet as p
import time
import pybullet_data
import math
# constants
m = 0.04593
g = 9.81
v_0 = 50
angle = math.pi / 4
vy_0 = 50 * math.sin(angle)
vx_0 = 50 * math.sin(angle)
x_0 = 0
y_0 = 0
ro = 1.2
A = 0.427
c_D = 0.3
physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -1*g)
planeId = p.loadURDF("plane.urdf")
golf_ball_start_pos = [0, 0, 1]
golf_ball_start_orientation = p.getQuaternionFromEuler([0, 0, 0])
p.createCollisionShape(shapeType=p.GEOM_MESH, fileName="duck_vhacd.obj")

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)
# cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
# print(cubePos, cubeOrn)
p.disconnect()
