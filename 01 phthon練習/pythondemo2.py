#  prefix underscore 前至下底線
import random

for _ in range(5):
    #下底線 佔位符,原本for結構那個位置應該要填東西我用下底線取代
    print(random.random())
print("迴圈結束")

#前面一開始就代下底線
_demo_data: dict={}#一開始就有一個下底線代表的是私有(private)變數或函式
#但是你還是可以使用他,不強制讓你無法使用但是提醒你他是私有變數

class Democlass:
    __deom_member_parameter=2 #強制私有變數 前面下底線式兩條