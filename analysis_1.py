import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# -----------------------------------------------------------------------------
# 1.matplotlib
# plt.plot([x軸],[y軸])
plt.plot([1,2,3,4,5,6,7,8],[4,8,2,9,3,7,6,0])

# 2.numPy
# 2-1 sum()
# np.array([List])  np.array((Tuple))
grades_1 = np.array([85,72,82])
weights_1 = np.array((0.6,0.7,0.5))
grades_2 = np.array([[85,72,82],[83,55,78]])
weights_2 = np.array((0.3,0.4,0.7))
# 計算加權
g = grades_1 * weights_1
print(g.sum())
# 2-2 dot()
# np.dot(list,list) 將兩個list相乘，後加總。和上述加總一樣，若是多維振烈就無法直加相乘加總
print(np.dot(grades_2,weights_2))
# 2-3 random
# 產生0~1的亂數 
# np.random.randn(n)  n為個數
np.random.rand()
# np.random.randint(x, y, size=n) x為亂數開頭，y為亂數結尾不會隨機到y這個數，n需要幾個亂數，亂數為整數
np.random.randint(1,10,size=2)
# np.random.randint(x, y, size=(a,b)) a需要幾組,b為一組需要幾個
np.random.randint(1,10,size=(2,5))
# 2-4 linspace(Start, End, Size) 產生Size個從Start到End的點
x = np.linspace(1, 2, 5)
plt.plot(x)
# 2-5 np.sin()、np.cos()、np.tan()、np.sinc()
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.plot(x, np.sin(x) + x)
plt.plot(x, np.cos(x))
# 2-6 Array 篩選法
L = np.array([50,10,20,30,40,45,31,21])
L < 35
L[L < 35]
x = np.linspace(-10, 10,10000)
y = np.sinc(x)
# 第一次畫圖全部，第二次畫圖畫大於0的
# 為甚麼要找y>0的，x也需補上[y>0]。原因plot() 函數，如果同時使用 x 與 y，點的位置必須相等，因此如果挑出>0的，則小於0的x軸將不會對到y軸
# plt.plot(x,y,marker)
# marker相關內容:https://matplotlib.org/3.1.1/api/markers_api.html
plt.plot(x,y)
plt.plot(x[y>0], y[y>0], 'ro-')
# 2-7 scstter  與 plot相似但只能畫"點"
# s大小、c顏色
X = np.random.rand(6)
Y = np.random.rand(6)
plt.scatter(X,Y,s = 100,c="g")



