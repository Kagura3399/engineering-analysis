from sympy import symbols, Matrix, simplify

# 定義符號
c,s=symbols('c s') #c:cos s:sin
EA_L=symbols('EA_L')

# local的一維bar的stiffness matrix 先把EA/L提出去 剩下的矩陣
K_local=Matrix([
    [ 1, 0, -1, 0],
    [ 0, 0,  0, 0],
    [-1, 0,  1, 0],
    [0,  0,  0, 0]
])

# 轉換矩陣
TT=Matrix([
    [ c, s, 0, 0],
    [-s, c, 0, 0],
    [0,  0, c, s],
    [0,  0,-s, c]
])

# TT轉置transpose
TT_transpose=TT.transpose()
print(TT_transpose)

# (TT的transpose x K_local) * TT
k_global=(TT.transpose() *K_local)*TT
print(k_global)