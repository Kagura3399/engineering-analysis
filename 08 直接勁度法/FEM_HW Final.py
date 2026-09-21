import numpy as np
import matplotlib.pyplot as plt

# 剛度矩陣計算函式
# 包含桿件兩端節點的 
# (x,y) 座標，分別對應於節點 1 和節點 2
# E：材料的楊氏模數（Elastic modulus）
# A：桿件的截面面積（Cross-sectional area）

# K矩陣有這樣的條件
# 平衡條件
# 協調條件(這個例子 結構變形後連結部分必須仍然連在一起 其他結構有其他條件 )
# 邊界條件
def truss_elem_stiff_2d(coords, properties):
    (x1, y1), (x2, y2) = coords
    Em, A = properties
    
    dx = x2 - x1
    dy = y2 - y1
    L = np.sqrt(dx**2 + dy**2)
    c = dx / L
    s = dy / L
    
    Ke = (Em * A / L) * np.array([
        [ c**2,  c*s, -c**2, -c*s],
        [ c*s,  s**2, -c*s, -s**2],
        [-c**2, -c*s,  c**2,  c*s],
        [-c*s, -s**2,  c*s,  s**2]
    ])
    
    return Ke

# 合併元件剛度矩陣到主剛度矩陣的函式
# 用pdf的範例說明
# Ke:4x4 matrix(truss)
# eftab: element freedom mapping table(local->global control)
# node1 ->全域矩陣的index 0,1
# node2 ->全域矩陣的index 2,3
# node3 ->全域矩陣的index 4,5
# truss1 ->node1,node2 ->0,1,2,3 (eftab)
# truss1 ->node2,node3 ->2,3,4,5 (eftab)
# truss1 ->node1,node3 ->0,1,4,5 (eftab)
def merge_local_elem_into_global_stiff(Ke, eftab, Kin):
    K = Kin.copy()
    for i in range(4):#i=0~3 i控制row
        ii = eftab[i]
        for j in range(i, 4):#j=i~3 j控制column
            jj = eftab[j]
            K[ii, jj] += Ke[i, j] #原本位置有值就疊加
            K[jj, ii] = K[ii, jj] #矩陣對稱,so算一半三角形
    return K

# 修改主剛度矩陣以施加位移邊界條件
# 第i row：表示第i個DOF的力平衡方程
# 第j column：表示第j個DOF的位移對所有其他DOF產生的影響
# 移除固定點的力平衡方程，改為直接約束 u = 0

# 如果只清row 不清column 我用下面3x3的矩陣給你們看
# 修改前： [K00 K01 K02][u0]   [f0] 
#         [K10 K11 K12][u1] = [f1]
#         [K20 K21 K22][u2]   [f2]
# 只清row 不清 column：
#           [1    0   0 ][u0]   [0 ] 
#           [K10 K11 K12][u1] = [f1]  <- 這裡還有K10項！
#           [K20 K21 K22][u2]   [f2]  <- 這裡還有K20項！

# 約束和耦合之間產生矛盾

# 以下正確的做法
#           [1    0   0 ][u0]   [0 ]  <- 這一row變成了約束方程，不是力平衡方程
#           [0   K11 K12][u1] = [f1]  <- 自由方程(真正的力平衡方程)
#           [0   K21 K22][u2]   [f2]  <- 自由方程(真正的力平衡方程)
# 獨立的子系統 u0被排除囉 所以不影響求解 

# 我們要強制 u0= 0
# 所以右邊必須是 0
# 因此 f0 被設為 0

# 這只是一個數學技巧來強制邊界條件(f=0)
# 修改後的 f0 = 0 不是真實的反力
# 真實反力要用原始K矩陣重新計算

# 這個方法就有降維的味道在裡面
# 等一下要做的這個例題:原始6維空間 -> 3維子空間

# "清零+設1"方法：

# 不是真正的降維（仍然求解6×6系統）
# 但等效於降維（3個DOF被直接固定）
# 保持矩陣結構（便於程式處理）

# pdof 是用來標記哪些自由度DoF被固定約束(Prescribed Degrees of Freedom)
#
def modified_global_stiff_for_dbc(pdof, K):
    Kmod = K.copy()         # 複製原始剛性矩陣,不會去改到原始矩陣
    nk = len(K)             # 總自由度數（矩陣大小）
    
    for i in pdof:          # 對每個要施加位移條件的自由度
        for j in range(nk):
            Kmod[i, j] = 0  # 清除該row
            Kmod[j, i] = 0  # 清除該column（對稱）
        Kmod[i, i] = 1      # 對角設為 1，強迫位移為 1×u = 0
    return Kmod

# 修改力向量以施加位移邊界條件
def modified_global_forces_for_dbc(pdof, f):
    fmod = f.copy()         # 複製原始力向量
    for i in pdof:          # 對每個要施加位移條件的自由度
        fmod[i] = 0         # 設為 0（齊次邊界條件)->故意的 跟力平衡無關了 要把其他方程式獨立出來
    return fmod


    # 繪製桁架變形圖的函式
def plot_truss_deformation(node_coords, elements, u, scale_factor=2):
    """
    繪製桁架變形前後的比較圖
    
    參數:
    node_coords: 節點座標陣列 [[x1,y1], [x2,y2], ...]
    elements: 桿件連接關係 [[node1,node2], ...]
    u: 節點位移向量
    scale_factor: 變形放大倍數，預設為2
    """
    
    # 計算變形後的節點座標
    num_nodes = len(node_coords)#計算節點數量,以這個範例3個nodes 結果 = 3

    #forloop i=0~2 
    # i = 0:
    #[u[2*0], u[2*0+1]] = [u[0], u[1]]   # 節點1的位移 (dx1, dy1)
    # i = 1: 
    #[u[2*1], u[2*1+1]] = [u[2], u[3]]   # 節點2的位移 (dx2, dy2)
    # i = 2:
    #[u[2*2], u[2*2+1]] = [u[4], u[5]]   # 節點3的位移 (dx3, dy3)
    # displacement = [[u[0], u[1]],    # 節點1位移
    #                 [u[2], u[3]],    # 節點2位移  
    #                 [u[4], u[5]]     # 節點3位移     
    #                              ]    
    displacement = np.array([[u[2*i], u[2*i+1]] for i in range(num_nodes)])
    
    # node_coords 是 3×2 的陣列（3個節點，每個節點2個座標）
    deformed_nodes = node_coords + scale_factor * displacement
    
    # 創建圖形
    # 第一個 1：子圖的row數
    # 第二個 1：子圖的columns數
    # figsize=(10, 8)：圖形尺寸，單位是英吋
    # 寬度 = 10 英吋
    # 高度 = 8 英吋
    # 第一個return->(fig): 控制整體設定：標題、大小、儲存...
    # 第二個return->(ax): 繪製線條、點、設定軸標籤...

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # 繪製原始結構（藍色實線）
    ## elements = [[0, 1], [1, 2], [0, 2]]
    # i=0, element=[0, 1]  (第1個桿件)
    # i=1, element=[1, 2]  (第2個桿件) 
    # i=2, element=[0, 2]  (第3個桿件)
    for i, element in enumerate(elements):
        # node1=0
        # node_coords[0] = [0, 0]   <- node_coords[0, 0] = 0,   node_coords[0, 1] = 0
        # node2=1
        # node_coords[1] = [10, 0]  <- node_coords[1, 0] = 10,  node_coords[1, 1] = 0
        node1, node2 = element
        x_coords = [node_coords[node1, 0], node_coords[node2, 0]]
        y_coords = [node_coords[node1, 1], node_coords[node2, 1]]
        #ex:畫出 (0,0) 到 (10,0) 的線 然後依序
        ax.plot(x_coords, y_coords, 'b-', linewidth=2)
    
    # 繪製變形後結構（紅色虛線）
    for i, element in enumerate(elements):
        node1, node2 = element
        x_coords = [deformed_nodes[node1, 0], deformed_nodes[node2, 0]]
        y_coords = [deformed_nodes[node1, 1], deformed_nodes[node2, 1]]
        ax.plot(x_coords, y_coords, 'r--', linewidth=2)
    
    # 設定圖形屬性 - 根據變形後的座標調整顯示範圍
    #收集所有座標
    all_x = np.concatenate([node_coords[:, 0], deformed_nodes[:, 0]])
    all_y = np.concatenate([node_coords[:, 1], deformed_nodes[:, 1]])
    #最大減最小*0.15當作邊距
    x_margin = (all_x.max() - all_x.min()) * 0.15
    y_margin = (all_y.max() - all_y.min()) * 0.15
    
    #(左邊界,右邊界)
    ax.set_xlim(all_x.min() - x_margin, all_x.max() + x_margin)
    #(下邊界,上邊界)
    ax.set_ylim(all_y.min() - y_margin, all_y.max() + y_margin)
    ax.set_aspect('equal') #等比例
    ax.grid(True, alpha=0.3)
    
    # 添加圖例
    
    plt.tight_layout()#自動調整圖形版面配置，避免重疊或被裁切
    plt.show()
    
#實作PDF範例
def analysis_pdf_truss_system():
    #####1.主裝全域矩陣####
    #依照範例長出一個6x6矩陣
    K=np.zeros((8,8))
    print(K)
    #Element 1:node1->node2 ->(0,0) to (4,3)
    #global stiffness matrix
    Ke=truss_elem_stiff_2d([(0,0),(4,3)],(200,1))
    K=merge_local_elem_into_global_stiff(Ke,[0,1,2,3],K)
    print(K)

    #Element 2:node2 to node3 ->(10,0) to (10,10)
    Ke=truss_elem_stiff_2d([(4,3),(8,0)],(200,1))
    K=merge_local_elem_into_global_stiff(Ke,[2,3,6,7],K)
    print(K)

    #Element 3:node2 to node3 ->(0,0) to (10,10)
    Ke=truss_elem_stiff_2d([(0,0),(8,0)],(200,1))
    K=merge_local_elem_into_global_stiff(Ke,[0,1,6,7],K)
    print(K)
    Ke=truss_elem_stiff_2d([(4,3),(4,0)],(200,1))
    K=merge_local_elem_into_global_stiff(Ke,[2,3,4,5],K)
    print(K)
    Ke=truss_elem_stiff_2d([(4,0),(8,0)],(200,1))
    K=merge_local_elem_into_global_stiff(Ke,[4,5,6,7],K)
    print(K)

    ####2.初始化力向量####
    f=np.array([0,0,12,20,0,0,0,0]) 

    ####3.施加位移的邊界條件####
    #node1 x y 被固定,node2 y被固定 所以 DoF 0,1,3 要為0
    pdof=[0,1,7]
    K_dbc=modified_global_stiff_for_dbc(pdof,K)#被改寫過後的K矩陣
    print(K_dbc)
    f_dbc=modified_global_forces_for_dbc(pdof,f)#被改寫的f向量
    print(f_dbc)

    ####4.解位移####
    u=np.linalg.solve(K_dbc,f_dbc)
    print(u)
    ##### 5.繪製變形圖 #####
    # 定義節點座標 (根據PDF範例)
    node_coords = np.array([
        [0, 0],      # 節點A
        [4, 3],    # 節點D (DOF 0,1)
        [4, 0],   # 節點C (DOF 2,3)
        [8, 0]   # 節點B (DOF 4,5)
    ])
    
    # 定義桿件連接關係 (節點編號從0開始)
    elements = np.array([
        [0, 1],   # Element 1: 節點A-節點D
        [1, 3],   # Element 2: 節點D-節點B
        [0, 2],   # Element 2: 節點A-節點B
        [2, 3],   # Element 2: 節點C-節點B
        [1, 2]    # Element 3: 節點D-節點C
    ])
    
    print("=== 繪製變形圖 ===")
    plot_truss_deformation(node_coords, elements, u, scale_factor=1.5)
    
analysis_pdf_truss_system()
