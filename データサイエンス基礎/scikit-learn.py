#データフレーム
import numpy as np
import pandas as pd


df = pd.DataFrame(
    {
    "A": [1, np.nan, 3, 4, 5],
    "B": [6, 7, 8, np.nan, 10],
    "C": [11, 12, 13, 14, 15]
    }
)
print(df)


#欠損値かどうか確かめる
df.isnull()          #True, Falseで返す


#欠損値の補完
from sklearn.impute import SimpleImputer

imp = SimpleImputer(strategy = "mean")      #平均値で欠損値を補完するインスタンスを作成
imp.fit(df)                               #デフォルトで列を指定。
imp.transform(df)


#カテゴリ変数のエンコーディング
import pandas as pd
df = pd.DataFrame(
    {"A": [1, 2, 3, 4, 5],
    "B": ["a", "b", "a", "b", "c"]
    }
)


from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer

df_ohe = df.copy()   #DataFrameをコピー
print(df_ohe)

ct = ColumnTransformer([('B_x', CountVectorizer(analyzer=lambda x: [x]), 'B')],
    remainder = 'passthrough')       # ColumnTransformerのインスタンス化
print(ct.fit_transform(df_ohe))


#分類
from sklearn.datasets import load_iris

iris = load_iris()                  #Irisデータセットを読み込む
X, y = iris.data, iris.target

print("X:")
print(X[:5, :])
print("y:")
print(y[:5])


#学習データとテストデータに分類(train_test_split関数)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)   #テストデータを30%にする
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


#サポートベクタマシン(support vector machine, SVM)
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
X0 = np.random.uniform(size=(100, 2))
y0 = np.repeat(0, 100)

X1 = np.random.uniform(-1.0, 0.0, size=(100, 2))
y1 = np.repeat(1, 100)

fig, ax = plt.subplots()
ax.scatter(X0[:, 0], X0[:, 1], marker="o", label="class 0")
ax.scatter(X1[:, 0], X1[:, 1], marker="x", label="class 1")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()


#サポートベクタマシン（決定境界、マージン、サポートベクタ）
from sklearn.svm import SVC

def plot_boundary_margin_sv(X0, y0, X1, y1, kernel, C, xmin=-1, xmax=1, ymin=-1, ymax=1):   
    svc = SVC(kernel=kernel, C=C)     #サポートベクタマシンのインスタンス化
    svc.fit(np.vstack((X0, X1)), np.hstack((y0, y1)))    #学習

    fig, ax = plt.subplots()
    ax.scatter(X0[:, 0], X0[:, 1], marker="o", label="class 0")
    ax.scatter(X1[:, 0], X1[:, 1], marker="x", label="class 1")

    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100))
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    p = svc.decision_function(xy).reshape((100, 100))

    ax.contour(xx, yy, p, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"])

    ax.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1], s=250, facecolors="none", edgecolors="black")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="best")
    plt.show()

plot_boundary_margin_sv(X0, y0, X1, y1, kernel="linear", C=1e6)















