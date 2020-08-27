import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans


# Linear regression
def Linear_regression():
    x = np.linspace(-6, 3, 100)
    y = 1.2 * x + 0.8 + 0.5 * np.random.randn(100)
    plt.scatter(x, y)
    # 0.2 就是 80% 的訓練資料,20% 的測試資料,random_state 為隨機的種子
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=999)
    # 接著透過 shape 來輸出訓練、測試的形狀
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    x_train = x_train.reshape(80, 1)
    x_test = x_test.reshape(20, 1)
    y_train = y_train.reshape(80, 1)
    y_test = y_test.reshape(20, 1)
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    # 在開始使用之前，必須實體化 LinearRegression
    regr = LinearRegression()
    # 可以使用 x_train, y_train 執行訓練，由於資料量小，訓練時間近乎一執行就馬上完成了
    regr.fit(x_train, y_train)
    # 接著對 x_test 進行預測，並將預測結果存至變數 predict_result 中。
    predict_result = regr.predict(x_test)
    plt.scatter(x, y)
    plt.plot(x, 1.2 * x + 0.8, "b-")
    plt.plot(x_test, predict_result, "r-")

# SVM (Support Vector Machine)
def SVM():
    x = np.array([[-3, 2], [-6, 5], [3, -4], [2, -8]])
    y = np.array([1, 1, 2, 2])
    clf = SVC()
    clf.fit(x, y)
    clf.predict(x)
    clf.predict([[2.5,3]])
    X, Y = np.meshgrid(np.linspace(-6, 3, 10), np.linspace(-8, 8, 10))
    X = X.ravel()
    Y = Y.ravel()
    plt.scatter(X, Y)
    Z = clf.predict(list(zip(X, Y)))
    plt.scatter(X, Y, c=Z)

# K-Means
def K_Means():
    X = np.random.rand(100, 2)
    plt.scatter(X[:,0], X[:,1], s=50)
    clf = KMeans(n_clusters=3)
    clf.fit(X)
    clf.labels_
    plt.scatter(X[:,0], X[:,1], s=50, c=clf.labels_)
    