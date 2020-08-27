import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#⚠ 欄位名 與 資料不一定對齊 ⚠
#功能說明
# describe() 列書欄位的詳細資料
# count() 資料數
# mean() 平均值
# std() 標準差
# min() 最小值
# 25% 25% 資料比例落在
# 50% 50% 資料比例落在
# 75% 75% 資料比例落在
# max() 最大值
# corr() 關聯性
# sum() 總和
# -----------------------------------------------------------------------------
#使用pandas獲取cvs內容
index = "https://raw.githubusercontent.com/yenlung/Python-3-Data-Analysis-Basics/master/grades.csv"
df = pd.read_csv(index)
#欄位名 與 前五筆資料 (n)輸入n，即可獲得n筆資料 在Spyder最多僅可列出60筆資料
df.head()
#列出前五筆資料 到 後五筆資料如若想要取得特定筆資料，需用 [n] n填入該值，也可以把[]去掉 df.欄位名
df["國文"]
#列出所有欄位名為國文的所有資料
df["國文"].values
# 對df產生平均數
df.mean()
# 對df產生標準差
df.std()
# 對欄位產生折線圖
df["國文"].plot()
# 對欄位產生直方圖 bins為直方圖寬度
df["國文"].hist(bins=10)
#生成主科欄位，將數學成績與英文成績做運算並放入主科欄位
df["主科"] = df.數學 * 1.4 + df.英文 * 1.2
# 生成總級分欄位  計算成績總和 sum(0)行列加總 sum(1)欄位加總
df["總級分"] = df[["國文","英文","數學","社會","自然"]].sum(1)
# 以主科為第一排序，遇到主科分數相同，以總級分做第二排序，並列出前10筆資料
# by 可以是List 會從index[0]開始排序
# ascending為排序依據 True為小到大(ASC) False為大到小(DESC)
df.sort_values(by=["主科","總級分"], ascending=False).head(10)
# -----------------------------------------------------------------------------
# Loc定位法
# loc[index,"欄位"]，也可以利用此種方式給予該欄位的數值
df.loc[2,"主科"]
# 也可透過此方式將想要的數值變為指定的數值
# 先取出df[i](欄位) 並檢測其中是否含有小於等於10的，如果有將該值更改為0
# 在判斷是否有大於10的，如果有更改為1
# ⚠放置順序重要⚠ ，如果先將大於10的放在前，那更改為1後，所有數值必將小於等於10，因此將被更改為0
# for i in ["國文","英文","數學","社會","自然"]:
#     df.loc[df[i] <= 10, i] = 0
#     df.loc[df[i] > 10, i] = 1
# -----------------------------------------------------------------------------
# 首先用亂數產生新的 DataFrame random.rand(筆數,欄位)
df1 = pd.DataFrame(np.random.rand(5,3),columns=list("ABC"))
# pd.DataFrame(np.random.rand(筆數,欄位),columns=list("ABC")) columns=list("ABC") list內的文字將每一字元當欄位名
df2 = pd.DataFrame(np.random.rand(5,3),columns=list("ABC"))
# 將df1,df2做合併  axis=1為行列合併(左右) axis=0為垂直合併(上下)
# 垂直合併如若df1,df2的欄位名不一樣將會變成| df1   NaN| 
#                                        | NaN   df2|
df3 = pd.concat([df1,df2],axis=1)
df4 = pd.concat([df1,df2],axis=0)
# 將df4的index重新排列，依照df4的長度重新排列
df4.index = range(len(df4.index))
