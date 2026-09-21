 #變量命名
lower_underscore_define_name=0 #小寫下引線
UPPER_UNDERSCORE_DEFINE_NAME=1 #大寫下引線
Came1CaseName=3 #大駝峰命名
came1casename=4 #小駝峰命名
#變數命名要有意義

#Python 大家默認的規則
import demo_module #模組定義 小寫下引線

demo_var=0 #變數定義 小寫下引線
def demo_function(): #小寫下引線
    pass
    #屬於這個函式的內容要縮排

class DemoClass: #類別定義採用大駝峰
    CONSTANT_VAULE=3.1415926 #常數採用大寫下引線
    def demo_method(self):#採用小寫下引線
        pass