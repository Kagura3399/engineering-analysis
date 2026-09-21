from truss_analysis import truss_external_reactions

#定義桁架結構中所有節點
node_coordinates ={
    'A':(0,0),
    'B':(0,1),
    'C':(1,1),
    'H':(1,0),
    'D':(2,1),
    'G':(2,0),
    'F':(3,0),
    'E':(3,1)
}

#定義外力
external_forces ={

    'C':(0,-80), #()這邊代表分力單位:kN
    'D':(0,-80)

}

#定義拘束的名稱
hinge='A'
roller='C'

reactions= truss_external_reactions(node_coordinates,external_forces,hinge,roller)

print("=============truss system analysis=============")
print("節點座標")
for node,(x,y) in node_coordinates.items():
    print(f"節點{node}:({x},{y}) m")

print("\n外力")
for node,(fx,fy) in external_forces.items():
    print(f"節點{node}:(Fx={fx} kN,Fy={fy} kN)")

print("\n拘束力")
for node,(rx,ry) in reactions.items():
    print(f"節點{node}:(Rx={rx:3f} kN, Ry={ry:.3f} kN)")

print("\n double check")
total_forces_xdirection= sum(fx for _,(fx,_) in external_forces.items())+sum(rx for _,(rx,_) in reactions.items())
total_forces_ydirection= sum(fy for _,(_,fy) in external_forces.items())+sum(ry for _,(_,ry) in reactions.items())

print(f"Sum_forces_x={total_forces_xdirection}<===算出來要為0")
print(f"Sum_forces_y={total_forces_ydirection}<===算出來要為0")

