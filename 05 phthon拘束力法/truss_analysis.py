import numpy as np

#以目前的範例來說
#我需要定義四個節點的座標方便我計算(單位是米)
#為了簡化各位理解題目 我把左下角定義為原點座標(0,0)向右為正 向上為正 滿足右手定則
#為了簡化程式 本函式的truss系統左側約束為Hinge 右側為Roller

#定義資料格式
# 1.定義接點座標(桁架系統的約束和受力只能在接點上,才不會破壞二力構件的組成)
#key-value資料結構
#node_coords = {
#  'A':(0,0),
#  'B':(4,3), 
#  'C':(8,0),
#  'D':(4,0)
# }

#2.外力定義
#external_forces={
#   'B':(12,20)  #()邊代表分力單位:kN
# }

def truss_external_reactions(node_coords,external_force,hinge_node,roller_node):
    #求所有外力和
    total_fx=sum(fx for _,(fx,_) in external_force.items())
    total_fy=sum(fy for _,(_,fy) in external_force.items())

    #求過座標原點的等效力偶
    #node_coords[node][0]像是 A的第一個位置值0,B的第一個位置值為4
    total_moment = sum(node_coords[node][0]*fy -node_coords[node][1]*fx for node,(fx,fy) in external_force.items())

    #獲取支撐的座標位置
    xHingeCoor, yHingeCoor =node_coords[hinge_node] #hinge座標抓取
    xRollerCoor, yRollerCoor =node_coords[roller_node] #roller座標抓取

    #等效力系過原點(0,0)的力矩平衡求解< --黑板推導
    Ry_roller= -total_moment/xRollerCoor

    #垂直方向合力和=0
    Ry_hinge= -total_fy-Ry_roller

    #水平方向合力和=0
    Rx_hinge=-total_fx

    reaction_forces ={
        hinge_node :(Rx_hinge,Ry_hinge),
        roller_node:(0,Ry_roller)
    }
    return reaction_forces
