import numpy as np

def least_square_manual(A,b):
    #解線性系統 Ax=b 的解，利用最小平方法
    #公式 x=(A^T A)^(-1) A^T b
    #A:係數矩陣
    #b:常數矩陣
    #X:未知數的矩陣
    
    #A^T
    A_transpose=np.transpose(A)

    #(A^T A)
    ATA= np.dot(A_transpose,A)

    #(A^T A)^(-1)
    ATA_inv=np.linalg.inv(ATA)

    #(A^T A)^(-1) A^T
    ATA_inv_AT=np.dot(ATA_inv,A_transpose)

    #最終解 X=(A^T A)^(-1) A^T b
    X=np.dot(ATA_inv_AT,b)

    return X
#範例
matrix_a=np.array([[5,10],[1,1]])
matrix_b=np.array([50,8])
matrix_x=least_square_manual(matrix_a,matrix_b)
print("手動計算的結果:",matrix_x)

#練習
matrix_a=np.array([[2,3],[4,6],[5,8]])
matrix_b=np.array([5,10,13])
matrix_x=least_square_manual(matrix_a,matrix_b)
print("手動計算的結果:",matrix_x)

#Numpy的lstsq函式
x_lstsq=np.linalg.lstsq(matrix_a,matrix_b,rcond=None)[0]
print("np.linalg.lstsq的解為:",x_lstsq)

#np.linalg.lstsq()函式輸出說明
output_x, out_residuals, rank, s =np.linalg.lstsq(matrix_a,matrix_b,rcond=None)
print("輸出結果為:",output_x)
print("輸出殘差(||Ax-b||^2值)為:",out_residuals)
print("輸出A的rank:",rank)
print("輸出singular value奇異值",s)

#example
matrix_a=np.array([[2,3],[4,6],[5,8]])
matrix_b=np.array([5,10,13])
output_x,out_residuals,rank,s=np.linalg.lstsq(matrix_a,matrix_b,rcond=None)
print("輸出結果為:",output_x)
print("輸出殘差(||(Ax-b)||^2值)為:",out_residuals)
print("輸出A的rank:",rank)
print("輸出singular value奇異值",s)

