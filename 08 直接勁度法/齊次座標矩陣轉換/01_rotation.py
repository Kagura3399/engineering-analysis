import numpy as np
import matplotlib.pyplot as plt
import math
# 顯示視窗的大小定義
plt.figure(figsize=(9,9))

# 畫坐標軸
ax=plt.gca() #get current axes取得目前的軸物件
ax.spines['left'].set_position('zero')#設定左邊邊框到x=0
ax.spines['bottom'].set_position('zero')#設定左邊邊框到y=0
ax.spines['right'].set_color('none')#隱藏右邊框
ax.spines['top'].set_color('none')#隱藏上邊框

# 畫輔助格線
plt.grid(True,linestyle='--',alpha=0.8)

# 重新定義座標的範圍 lim->limit
plt.xlim(-5,5)
plt.ylim(-6,6)

# 加上x,y座標的文字
plt.text(5.2,-0.1,'x',fontsize=14)
plt.text(-0.2,6.2,'y',fontsize=14)


# 畫小刻度 tick
plt.xticks(range(-5,5,1))
plt.yticks(range(-6,6,1))


# 因為等一下要讓點座標旋轉,所以要用np.array來儲存點座標,方便與旋轉矩陣一同操作
rect_points= np.array([
    [-2.5,-2],
    [2.5,-2],
    [2.5,2],
    [-2.5,2],
    [-2.5,-2]
])

plt.plot(rect_points[:,0],rect_points[:,1],'k-',linewidth=2)

# 逆時針旋轉矩陣,留意sin負號位置,這個矩陣是圖旋轉,座標固定
angle_rad=30*math.pi/180
rotation_matrix=np.array([
    [np.cos(angle_rad),np.sin(angle_rad)],
    [-np.sin(angle_rad),np.cos(angle_rad)]
])

rotat_rect_points=np.dot(rect_points,rotation_matrix.T)

plt.plot(rotat_rect_points[:,0],rotat_rect_points[:,1],'r-',linewidth=2)

# 顯示視窗
plt.show()