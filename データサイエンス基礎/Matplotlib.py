import matplotlib.pyplot as plt

import matplotlib.style
matplotlib.style.use('ggplot')


#MATLABスタイル
x = [1, 2, 3]
y = [2, 4, 9]

plt.plot(x, y)               #折れ線グラフを描画
plt.title("MATLAB-style")    #グラフにタイトルを設定
plt.show()


#オブジェクト指向スタイル
x = [1, 2, 3]
y = [2, 4, 9]

fig, ax = plt.subplots()    #描画オブジェクト(fig)とサブプロット(ax)を生成

ax.plot(x, y)                #折れ線グラフを描画
ax.set_title("OOP-style")    #タイトルを設定
plt.show()


#描画オブジェクトとサブプロット

fig, ax = plt.subplots(2)        #2つのサブプロットを配置
plt.show()

fig, axes = plt.subplots(2, 2)   #2行2列のサブプロットを配置
plt.show()

fig, axes = plt.subplots(ncols=2)  #1行2列のサブプロットを配置
plt.show()

fig, axes = plt.subplots(nrows=2)  #2行1列のサブプロットを配置
plt.show()


#グラフスタイル
import matplotlib.style
print(matplotlib.style.available)  #スタイルの一覧を表示

matplotlib.style.use("classic")    #classicスタイルを指定
fig, ax = plt.subplots()
ax.plot([1, 2])
plt.show()


#タイトル
fig, axes = plt.subplots(ncols=2)

axes[0].set_title("subplot title 0")    #サブプロットにタイトルに設定
axes[1].set_title("subplot title 1")
fig.suptitle("figure title")            #描画オブジェクトにタイトルを設定
plt.show()


#軸ラベル
fig, ax = plt.subplots()

ax.set_xlabel("x label")    #X軸にラベルを設定
ax.set_ylabel("y label")    #Y軸にラベルを設定
plt.show()


#凡例
fig, ax = plt.subplots()

ax.plot([1, 2, 3], [2, 4, 9], label="legend label")
ax.legend(loc="best")         #凡例を表示
plt.show()


fig, ax = plt.subplots()

ax.plot([1, 2, 3], [2, 4, 9], label="legend label")
ax.legend(loc="lower right")        #凡例を右下に表示
plt.show()        

#凡例の位置は他に"upper left", "center", "center left", "lower center", "best"がある


#ファイル出力
fig, ax = plt.subplots()
ax.set_title("subplot title")
fig.savefig("sample-figure.png")    #png形式で保存
fig.savefig("sample-figure.svg")    #svg形式で保存


#折れ線グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 1, 2]
ax.plot(x, y1)      #折れ線グラフを描画
ax.plot(x, y2)      #折れ線グラフを描画
plt.show()


#sin, cosのグラフ
import numpy as np

x = np.arange(0.0, 15.0, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

fig , ax = plt.subplots()
ax.plot(x, y1, label="sin")
ax.plot(x, y2, label="cos")
ax.legend()

plt.show()


#棒グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y = [10, 2, 3]
ax.bar(x, y)      #棒グラフを描画

plt.show()


#棒グラフのラベル
fig, ax = plt.subplots()

x = [1, 2, 3]
y = [10, 2, 3]
labels = ["spam", "ham", "egg"]
ax.bar(x, y, tick_label=labels)    #ラベルを指定
plt.show()


#横向き棒グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y = [10, 2, 3]
labels = ["spam", "ham", "egg"]
ax.barh(x, y, tick_label=labels)    #横向きの棒グラフを指定
plt.show()


#複数の棒グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [5, 3, 6]
labels = ["spam", "ham", "egg"]

width = 0.4        #棒グラフの幅を0.4にする
ax.bar(x, y1, width=width, tick_label=labels, label="y1")     #幅を指定して描画

x2 = [num + width for num in x]
ax.bar(x2, y2, width=width, label="y2")
ax.legend()
plt.show()


#積立て棒グラフ
fig, ax = plt.subplots()

x = [1, 2, 3]
y1 = [10, 2, 3]
y2 = [5, 3, 6]
labels = ["spam", "ham", "egg"]

y_total = [num1 + num2 for num1, num2 in zip(y1, y2)]

ax.bar(x, y_total, tick_label=labels, label="y1")
ax.bar(x,y2, label="y2")
ax.legend()

plt.show()

#散布図
fig, ax = plt.subplots()

np.random.seed(123)
x = np.random.rand(50)
y = np.random.rand(50)

ax.scatter(x, y)
plt.show()


#散布図（マーカー）
fig, ax = plt.subplots()

np.random.seed(123)
x = np.random.rand(50)
y = np.random.rand(50)

ax.scatter(x[0:10], y[0:10], marker="v", label="triangle down")    #下向き三角
ax.scatter(x[10:20], y[10:20], marker="^", label="triangle up")    #上向き三角
ax.scatter(x[20:30], y[20:30], marker="s", label="square")         #正方形
ax.scatter(x[30:40], y[30:40], marker="*", label="star")           #星型
ax.scatter(x[40:50], y[40:50], marker="x", label="x")              #X
ax.legend()

plt.show()


#ヒストグラム
np.random.seed(123)
mu = 100        #平均値
sigma = 15      #標準偏差
x = np.random.normal(mu, sigma, 1000)

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x)
plt.show()


#度数分布表の表示
for i, num in enumerate(n):         
    print('{:.2f} - {:.2f}: {}'.format(bins[i], bins[i + 1], num))


#ヒストグラム（ビンの数を指定)
fig, ax = plt.subplots()
ax.hist(x, bins=25)    #ビンの数を指定して描画
plt.show()


#横向きヒストグラム
fig, ax = plt.subplots()
ax.hist(x, orientation="horizontal")   
plt.show()


#複数のヒストグラム(自動的に横並びになる)
np.random.seed(123)
mu = 100

x0 = np.random.normal(mu, 20, 1000)   #異なる標準偏差でデータを生成
x1 = np.random.normal(mu, 15, 1000)    
x2 = np.random.normal(mu, 10, 1000)

fig, ax = plt.subplots()

labels = ["x0", "x1", "x2"]
ax.hist((x0, x1, x2), label=labels)
ax.legend()
plt.show()


#積み上げヒストグラム(stacked=True)
fig, ax = plt.subplots()

labels = ["x0", "x1", "x2"]
ax.hist((x0, x1, x2), label=labels, stacked=True)
ax.legend()

plt.show()


#箱ヒゲ図
np.random.seed(123)
x0 = np.random.normal(0, 10, 500)
x1 = np.random.normal(0, 15 ,500)
x2 = np.random.normal(0, 20, 500)

fig, ax = plt.subplots()
labels = ["x0", "x1", "x2"]
ax.boxplot((x0, x1, x2), labels=labels)   #箱ヒゲ図の描画

plt.show()


#横向き箱ヒゲ図(vert=False)
fig, ax = plt.subplots()

labels = ["x0", "x1", "x2"]
ax.boxplot((x0, x1, x2), labels=labels, vert=False)
plt.show()


#円グラフ(楕円形)
labels = ["spam", "ham", "egg"]
x = [10, 3, 1]

fig, ax = plt.subplots()
ax.pie(x, labels=labels)   #円グラフを描画

plt.show()


#円グラフ(アスペクト比を保持)
fig, ax = plt.subplots()

ax.pie(x, labels=labels)
ax.axis("equal")      #アスペクト比を保持
plt.show()


#円グラフ(上から時計回り)
fig, ax = plt.subplots()

ax.pie(x, labels=labels, startangle=90, counterclock=False)  #上(startangle=90)から時計回り(counterclock=False)
ax.axis("equal")

plt.show()


#円グラフ(影とパーセント表記)
fig, ax = plt.subplots()

ax.pie(x, labels=labels, startangle=90, counterclock=False, 
shadow=True, autopct="%1.2f%%")  #影(shadow=True)とパーセント表記(autopct="%1.2f%%")
ax.axis("equal")
plt.show()


#円グラフ(要素を切り出し)
fig, ax = plt.subplots()

explode = [0, 0.2, 0]   #1番目の要素を切り出す
ax.pie(x, labels=labels, startangle=90, counterclock=False,
shadow=True, autopct="%1.2f%%", explode=explode)    #explodeを指定
ax.axis("equal")

plt.show()


#複数のグラフを組み合わせる(棒グラフと折れ線グラフ)
fig, ax = plt.subplots()

x1 = [1, 2, 3]
y1 = [5, 2, 3]
x2 = [1, 2, 3, 4]
y2 = [8, 5, 4, 6]
ax.bar(x1, y1, label="y1")     #棒グラフを描画
ax.plot(x2, y2, label="y2")    #折れ線グラフを描画
ax.legend()

plt.show()


#複数のグラフを組み合わせる(ヒストグラムと折れ線グラフ)
np.random.seed(123)
x = np.random.randn(1000)      #正規乱数を生成

fig, ax = plt.subplots()

counts, edges, patches = ax.hist(x, bins=25)    #ヒストグラムを描画

x_fit = (edges[:-1] + edges[1:]) / 2

y = 1000 * np.diff(edges) * np.exp(-x_fit**2 / 2) / np.sqrt(2 * np.pi)
ax.plot(x_fit, y)

plt.show()


#色の設定
fig , ax = plt.subplots()

ax.plot([1, 3], [3, 1], label="aqua", color="aqua")         #線の色を名前で指定
ax.plot([1, 3], [1, 3], label="#0000FF", color="#0000FF")   #16進数のRGBで指定
ax.plot([1, 3], [2, 2], label="(0.1, 0.2, 0.5, 0.3)", color=(0.1, 0.2, 0.5, 0.3) )  #RGBAをfloatで指定

ax.legend()
plt.show()


#塗りつぶしと枠線
fig, ax = plt.subplots()

ax.bar([1], [3], color="aqua")   #塗りつぶし色を指定
ax.bar([2], [4], color="aqua", edgecolor="black")    #塗りつぶしと枠線を指定
plt.show()


#線のスタイル
fig, ax = plt.subplots()

ax.plot([1, 3], [3, 1], linewidth=5.5, label="5.5")     #5.5ポイントの幅の線で描画
ax.plot([1, 3], [1, 3], linewidth=10, label="10")     #10ポイントの幅の線で描画
ax.legend()
plt.show()


#線の種類
fig, ax = plt.subplots()

ax.plot([1, 3], [3, 1], linestyle="--", label="dashed")     #破線で描画
ax.plot([1, 3], [3, 1], linestyle="-.", label="dashbot")    #一点鎖線で描画
ax.plot([1, 3], [2, 2], linestyle=":", label="dotted")      #点線で描画

ax.legend()
plt.show()


#フォント
fig, ax = plt.subplots()

#size=フォントサイズ, weight引数=フォントの太さ, family引数=フォントの種類
ax.set_xlabel("xlabel", family="fantasy", size=20, weight="bold")
ax.set_ylabel("ylabel", family="cursive", size=40, weight="light")
ax.set_title("graph title", family="monospace", size=25, weight="heavy")

plt.show()


#フォントの種類を辞書で定義
fontdict = {
    "family": "fantasy",
    "size": 20,
    "weight": "normal",
}

fig, ax = plt.subplots()

ax.set_xlabel("xlabel", fontdict=fontdict)
ax.set_ylabel("ylabel", fontdict=fontdict)
ax.set_title("graph title", fontdict=fontdict, size=40)    #sizeだけ変更

plt.show()


#テキスト描画
fig, ax = plt.subplots()

ax.text(0.2, 0.4, "Text", size=20)    #Textを描画

plt.show()


#Pandasのオブジェクトから折れ線グラフ描画
import pandas as pd
import matplotlib.style
import matplotlib.pyplot as plt

matplotlib.style.use("ggplot")       #スタイルを指定

df = pd.DataFrame({"A": [1, 2, 3], "B": [3, 1, 2]})
df.plot()     #折れ線グラフを描画
plt.show()


#Pandasのオブジェクトから棒グラフ描画
import numpy as np

np.random.seed(123)
df2 = pd.DataFrame(np.random.rand(3, 2), columns=["y1", "y2"])

df2.plot.bar()     #棒グラフ
plt.show()


df2.plot.bar(stacked=True)    #積み上げ棒グラフ
plt.show()




