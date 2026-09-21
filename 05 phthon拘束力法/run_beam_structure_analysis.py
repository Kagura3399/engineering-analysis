#匯入function
from beam_structure_analysis import simple_support_beam
    
#簡支樑分析
beam_length= 10 #10公尺
loads =[(2,-5),(4,-10)] #座標,外力kN

#計算
RA, RB = simple_support_beam(beam_length,loads)

print("================簡支樑Simple Support Beam拘束力計算================")
print(f"簡支樑長度:{beam_length} m")
print(f"負載:{loads}")
print(f"左邊拘束力為:{RA} kN")
print(f"右邊拘束力為:{RB} kN")
print(f"檢查用(外力與拘束力和要為0):{RA+RB+sum(force for _, force in loads)}")


from beam_structure_analysis import cantilever_beam
    
#懸臂樑分析
length= 10 #10公尺
loads =[(10,-10)] #座標,外力kN

#計算
R, M = cantilever_beam(length, loads)

print("================懸臂樑Cantilever Beam拘束力計算================")
print(f"懸臂樑長度:{length} m")
print(f"負載:{loads}")
print(f"左邊拘束力為:{R} kN")
print(f"左邊拘束力為:{M} kN")
print(f"檢查用(外力與拘束力和要為0):{R+sum(force for _, force in loads)}")


from beam_structure_analysis import overhanging_beam
    
#外伸樑分析
span_length= 10 #10公尺
overhand_length= 4
loads =[(14,10)] #座標,外力kN

#計算
RA, RB = overhanging_beam(span_length,overhand_length, loads)

print("================外伸樑Overhanging Beam拘束力計算================")
print(f"外伸樑長度:{span_length+overhand_length} m")
print(f"負載:{loads}")
print(f"左邊拘束力為:{RA} kN")
print(f"右邊拘束力為:{RB} kN")
print(f"檢查用(外力與拘束力和要為0):{RA-RB+sum(force for _, force in loads)}")