import numpy as up

#簡支樑
def simple_support_beam(length, loads):
    """
    計算簡支樑的拘束力
    限定外力只能在垂直方向在這個範例
    左邊為hinge支撐
    右邊為roller支撐
    力的方向,向下為負,向上為正
    力偶的方向逆時針為正

    輸入:
    length (樑的長度)單位假設為 m
    loads (外力)單位假設為 kN

    輸出
    RA 左邊的垂直拘束力
    RB 右邊的垂直拘束力

    """
    #假設座標系統的原點在最左邊

    #求外力和
    #loads(外力) 定義為 tuple (pos,force)
    # ex: loads=[(2,-10),(4,-15)]
    #下面的這個sum會掃過一遍loads這個容器提取 force的資料 -10 -15,累加起來
    total_force=sum(force for _, force in loads)

    #等效力系與左邊那點(A)的力偶和
    couple_moment_A=sum(pos*force for pos,force in loads)

    #解RB
    RB=-couple_moment_A/length
    
    #解RA
    RA=-total_force-RB

    return RA,RB

def cantilever_beam(length, loads):
    R=-sum(force for _, force in loads)

    M=-sum(pos*force for pos,force in loads)

    return R,M

def overhanging_beam(span_length,overhand_length, loads):

    total_force=sum(force for _, force in loads)
    couple_moment=sum(pos*force for pos,force in loads)
    RB=couple_moment/(span_length+overhand_length)
    RA=total_force-RB
    return RA,RB