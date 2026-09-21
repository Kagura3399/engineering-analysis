import numpy as np
import matplotlib.pyplot as plt

# x=[1,2,3]
# y=[4,5,6]

# plt.plot(x,y)
# plt.show()

# 繪製矩形
# rect_x=[1,6,6,1]
# rect_y=[1,1,5,5]
# plt.plot(rect_x,rect_y)
# plt.show()

points=np.array([[1,1],[6,1],[6,5],[1,5]])
plt.plot(points[:,0],points[:,1])
plt.show()