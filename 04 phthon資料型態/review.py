"""
python 常用括號的用途

"""

def parentheses_example() ->None: #->None 提示字元代表沒有回傳值
    """ 小括號常用的功能在python中""" #滑鼠過去三引號會有提示字串
    #1.tuple(元組)念作 tool-pull,tub-pull
    #特性:不可變性，創建宣告後，後面程式不可以再修改
    #有序:元素放置有順序性
    #可儲存不同類型的資料
    point=(10,20)
    print(f"tuple ex: {point},型別: {type(point)}")#f f-string 格式化字串 f"...{}"
    
    empty_tuple=()
    print(f"tuple ex: {empty_tuple},型別 {type(empty_tuple)}")
    
    single_tuple=(40,)#不加逗號(40)python會認為是一個整數
    print(f"tuple ex:{single_tuple}, 型別:{type(single_tuple)}")

    others_tuple=1,2,3
    print(f"tuple ex: {others_tuple},型別:{type(others_tuple)}")
    
    multidatas_tuple=(1.2,"name",10)
    print(f"tuple ex:{multidatas_tuple},型別:{type(multidatas_tuple)}")

    #2.函式的呼叫
    print(f"函式的呼叫範例:python有{len("python")}個字元")#呼叫了len函式

    #3.函式定義
def square(x:int) ->int:
    """ 算出整數平方值 """
    return x*x
def  result11square() ->None:
    print(f"11的平方是{square(11)}")

#4.小括號可以用於計算先順序
#5.條件語句
x=10
def numberrange(x) ->None:
    if (x>5 and x<15):
        print(f"x={x}在這個5~15範圍裡面")
    else:
        print(f"x={x}不在這個5~15範圍裡面")
def generator_exam()->None:
#6 生成式表達器他的格式:(...for...in iterable)
    #for x in ranger(5): x會從0~4依序變化
    square_gen=(x**2 for x in range(5))#用for迴圈需要三行，這邊一行解決
    print(f"生成式表達器的型態:{type(square_gen)}")
    print(f"生成式表達器的內容:{list(square_gen)}")#強制轉型為list
    print(f"生成式表達器的內容:{list(square_gen)}")


generator_exam()
numberrange(10)
numberrange(20)
#parentheses_example()
#result11square()

