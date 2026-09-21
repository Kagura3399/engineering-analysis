import numpy as np
import math

#物理的結構空間->>>轉為矩陣索引空間

#1.邊界定義

#節點座標格式 >A矩陣的row方向
#ex:A節點->(索引值為0列 x方向分力) (索引值為1列 y方向分力)
#B節點->(索引值為2列 x方向分力) (索引值為3列 y方向分力)
node_coords={
  'A':(0,0),
  'B':(0,3),
  'C':(3,3),
  'D':(6,3),
  'E':(9,3),
  'F':(9,0),
  'G':(6,0),
  'H':(3,0)
 }

#桿方向定義 >A矩陣的column方向
#ex:AB桿 索引值為0 column
#AD桿 索引值為1 coulumn
members =[
 ('A','B'),
 ('A','H'),
 ('B','C'),
 ('B','H'),
 ('C','H'),
 ('C','G'),
 ('C','D'),
 ('D','G'),
 ('D','F'),
 ('D','E'),
 ('E','F'),
 ('F','G'),
 ('G','H')
 ]
#節點編號順序
nodes=['A','B','C','D','E','F','G','H']

#2.外力定義
external_force={
 'C':(0,-80),
 'D':(0,-80)  #向右12kN 向上20kN
 }


#3.計算方向餘弦 
member_cosines={}
    
for (node1,node2) in members:
    x1, y1=node_coords[node1]
    x2, y2=node_coords[node2]

    #1->2的方向餘弦
    #x方向分量
    dx=x2-x1
    #y方向分量
    dy=y2-y1
    #向量長度
    length=math.sqrt(dx**2+dy**2)

    cos_x=dx/length
    cos_y=dy/length

    member_cosines[(node1,node2)]=(cos_x,cos_y)

    #2->1的方向餘弦
    member_cosines[(node2,node1)]=(-cos_x,-cos_y)

#4. 填充矩陣[A]係數
#[A]{x}={b},矩陣和向量大小宣告
n_equations=16 #四個節點->8個方程式
n_unknowns=16 #13根桿件的力+3個拘束力
A=np.zeros((n_equations,n_unknowns))
b=np.zeros(n_equations)

for m_idx ,(node1,node2) in enumerate(members):
    #對任意桿件的第一點編號
    node_idx=nodes.index(node1)#抓取node1所在的編號存進去node_idx ex:桿件AB node1是A 所以在nodes的index是0 把0放進去node_idx
    result_cos_x,result_cos_y=member_cosines[(node1,node2)]
    A[2*node_idx,m_idx]=result_cos_x #<--整個程式的核心
    A[2*node_idx+1,m_idx]=result_cos_y #<--整個程式的核心

    #對任意桿件的第二點標號
    node_idx=nodes.index(node2)
    result_cos_x,result_cos_y=member_cosines[(node2,node1)]
    A[2*node_idx,m_idx]=result_cos_x #<--整個程式的核心
    A[2*node_idx+1,m_idx]=result_cos_y #<--整個程式的核心

#剩下的手動填充比較簡單
#先填充拘束力的係數
A[0,13]=1 #Rax
A[1,14]=1 #Ray
A[11,15]=1 #Rcy

#5.填充外力向量{b}
for node,(fx,fy) in external_force.items():
    node_idx=nodes.index(node) #目前範例力是作用在B點 所以node_idx=1
    b[2*node_idx]=-fx #因為靜力平衡方程式外力往等號右邊移動 所以出現負號
    b[2*node_idx+1]=-fy #因為靜力平衡方程式外力往等號右邊移動 所以出現負號

#6.計算
x=np.linalg.solve(A,b)
#7.結果
print("\n向量x:")
print(x)

print("\桿件的軸向力")
for i,(node1,node2) in enumerate(members):
    force_type="拉力" if x[i] > 0 else "壓力"
    print(f"{node1}{node2}桿: {abs(x[i]):.3f} kN ({force_type})")


#def truss(members,node_coords):
    #1.檢查系統是否為靜力系統
    #2.建立桿件的方向餘弦
    #member_cosines={}

    #return
# convert_supports(node_coords,[A],[C])
#def convert_supports(node_coords,hinge_node,roller_node):
    #support={}
    #for node in node_coords:
        #if  node in hinge_node:
            #supports=[node]=(True,True) #代表x和y方向都有拘束
        #elif node in roller_node:
            #supports[node]=(False,True) #只有y方向有拘束
        #else:
            #supports[node]=(False,False)
    #return supports