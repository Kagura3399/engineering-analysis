#中括號
def square_brackets_examples():
    #1.list
    numbers=[1,2,3,4,5]
    print(f"list ex: {numbers},型別:{type(numbers)}")

    #empty list
    empty_list =[]
    print(f"空列表:{empty_list}")

    #索引操作 從0開始
    first_number=numbers[4]
    print(f"fifth number of numbers:{first_number},型式:{type(first_number)}")

    ##tuple跟list容器的比較
    #tuple式定義好就不可以改變,但是list後續還可以變
    #tuple可以儲存不同資料型態,list通常為同一種資料型態
    #tuple因為不可變,所以效能比list高
    #tuple可以當作dict的key(鍵),list不行

    message="我愛python"
    first_char=message[1]
    print(f"fifth number of numbers: {first_char},型別:{type(first_char)}")

    #切片操作
    subset=numbers[1:4]
    print(f"subset numbers: {subset},型別:{type(subset)}")

    #反轉list
    reversed_list=numbers[::-1]
    print(f"numbers:{reversed_list},型別{type(reversed_list)}")

    #修改list元素
    numbers[0]=99
    print(f"numbers:{numbers},型別:{type(numbers)}")

    #槽狀list
    matrix=[[1,2,3],[4,5,6],[7,8,9]]#3x3矩陣
    #matrix[1]
    print(f"matrix(1):{matrix[1]},型別:{type(matrix[1])}")
    #matrix[1][2]
    print(f"matrix(1):{matrix[1][2]},型別:{type(matrix[1][2])}")
    

square_brackets_examples()