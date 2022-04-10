
import numpy as np

#1次元配列
a = np.array([1,2,3])
print(a)

type(a) #オブジェクト確認
a.shape #形を確認


#2次元配列
b = np.array([[1,2,3], [4,5,6]])
print(b)
b.shape


#変形
c1 = np.array([0,1,2,3,4,5])
print(c1)

c2 = c1.reshape((2,3)) #２行3列に変形
print(c2)

c3 = c2.ravel() #1次元配列に変換（参照）
c4 = c2.flatten() #1次元配列に変換（コピー）


#データ配列
a.dtype

d = np.array([1,2], dtype=np.int16) #int16を宣言
print(d)
d.dtype

d.astype(np.float16) #float16に変換


#インデックスとスライス
a = np.array([1,2,3])

print(a[0])
print(a[1:])
print(a[-1])

b = np.array([[1,2,3],[4,5,6]])

print(b[0])
print(b[1,0])
print(b[:,2])
print(b[1,:])
print(b[0,1:])
print(b[:, [0,2]])


#データ再代入
a = np.array([1,2,3])

a[2] = 4
print(a)

b = np.array([[1,2,3], [4,5,6]])
b[1,2] = 7
print(b)

b[:,2] = 8
print(b)


#浅いコピー(参照)
a1 = a
print(a1)          #array([1,2,4])

a1[1] = 5
print(a1)          #array([1,5,4])  

print(a)           #array([1,5,4])


#深いコピー（コピー）
a2 = a.copy()
print(a2)              #array([1,5,4])

a2[0] = 6
print(a2)              #array([6,5,4])

print(a)               #array([1,5,4])


#Pythonのlistはコピーを渡す
p = [0,1]
p2 = p[:]
p2[0] = 2
print(p)
print(p2)


#数列
print(np.arange(10))
print(np.arange(1,11))
print(np.arange(1,11,2))


#乱数
f = np.random.random((3,2))   #0〜1間のランダムな要素の行列を作成
print(f)

np.random.seed(123)   #シード値
np.random.random((3,2))     #randomは行と列のタプルを渡す
np.random.rand(4,2)         #randは二つの引数を渡す

np.random.seed(123)
np.random.randint(1,10)    #１以上１０未満の整数の中から１つの整数が出力

np.random.seed(123)
np.random.randint(1,10,(3,3))  #１以上１０未満の整数の3行３列

np.random.seed(123)
np.random.uniform(0.0, 5.0, size=(2,3))  #0以上5未満の小数値の２行３列

np.random.seed(123)
np.random.uniform(size=(4,3)) #0以上１未満の小数値の４行3列

np.random.seed(123)
np.random.randn(4,2) #平均0,分散１の４行２列


#同じ要素の数列
np.zeros(3)         #引数で指定した要素数の0.0の配列
np.zeros((2,3))     #0.0の２行３列の配列

np.ones(2)          #引数で指定した要素数の1.0の配列
np.ones((3,4))      #1.0の３行４列の配列


#単位行列
np.eye(3)        #対角要素を持った単位行列


#指定値で埋める
np.full(3, 3.14)          #3.14の３つの要素の配列
np.full((2, 4), np.pi)    #3.14の２行４列の配列

np.nan
np.array([1, 2, np.nan])   #nan派float型で計算可能


#均等割データ
np.linspace(0, 1, 5)          #0から1までを等間隔に分割した５つの要素
np.linspace(0, np.pi, 21)     #sin関数のグラフを作成するのに利用する


#要素間の差分
l = np.array([2, 2, 6, 1, 3])
np.diff(l)                     #要素間の前後の差分の配列


#連結
a = np.array([1, 2, 5])
a1 = np.array([1, 2, 5])
np.concatenate([a, a1])      #１次元配列の連結

b = np.array([[1, 2, 8],[4, 5, 8]])
b1 = np.array([[10],[20]])
np.concatenate([b,b1], axis=1)  #列方向に連結

np.hstack([b, b1])   #列方向に連結

b2 = np.array([30, 60, 45])
b3 = np.vstack([b, b2])   #行方向に連結


#分割
b3 = np.array([[1, 2, 8], [4, 5, 8], [30, 60, 45]])

first, second = np.hsplit(b3, [2])      #列方向に分割
print(first)                            #[2]を指定しているので、1つ目の配列が２列となる
print(second)

first1, second1 = np.vsplit(b3, [2])    #行方向に分割
print(first1)                           #[2]を指定しているので、1つ目の配列が２列となる
print(second1)


#転置
b = np.array([[1, 2, 8], [4, 5, 8]])
b.T                                     #行と列を入れ変える


#次元追加
a = np.array([1, 5, 4])

a[np.newaxis, :]          #列方向に次元を追加
a[:, np.newaxis]          #行方向に次元を追加


#グリッドデータの生成
m = np.arange(0, 4)        #array([0, 1, 2, 3])
n = np.arange(4, 7)        #array([4, 5, 6])

xx, yy = np.meshgrid(m, n)
print(xx)                  #array([[0, 1, 2, 3],
                           #      [0, 1, 2, 3],
                           #      [0, 1, 2, 3]])

print(yy)                  #array([[4, 4, 4, 4],
                           #       [5, 5, 5, 5],
                           #       [6, 6, 6, 6]])


#ユニバーサルファンクション
b = np.arange(-3, 3).reshape((2,3))
print(np.abs(b))               #絶対値

e = np.linspace(-1, 1, 10)
print(np.sin(e))               #sin関数
print(np.cos(e))               #cos関数

a = np.arange(3)
print(np.log(a))               #log関数
print(np.exp(a))               #exp関数

c = np.arange(1, 7).reshape((2, 3))
print(np.log10(c))             #log10関数


#ブロードキャスト
a = np.array([0, 1, 2])
print(a + 10)

b = np.array([[-3, -2, -1], [0, 1, 2]])
print(a + b)

a1 = a[:, np.newaxis]
print(a + a1)          #array([[0, 1, 2],
                       #       [1, 2, 3],
                       #       [2, 3, 4]])

c = np.array([[1, 2, 3],[4, 5, 6]])
c - np.mean(c)

b = np.array([[-3, -2, -1], [0, 1, 2]])
print(b*2)
print(b ** 3)
print(b - a)
print(a * b)

print(c / a)             #要素に0があるとinfが出力される
print(c / (a+1e-6))      #微小な数値をたして要素が０にならないようにする


#ドット積
a = np.array([0, 1, 2])
b = np.array([[-3, -2, -1], [0, 1, 2]])
d = np.array([[0, 1], [2, 3], [4, 5]])

np.dot(b, a)        #二次元配列と一次元配列のドット積　　array([-4,5])
print(b@a)          #array([-4, 5])

b@d                 #array([[-8, -14], [10, 13]])
d@b                 #array([[0, 1, 2], [-6, -1, 4], [-12, -3, 6]])


#判定・理論値
a = np.array([0, 1, 2])
b = np.array([[-3, -2, -1], [0, 1, 2]])
c = np.array([[1, 2, 3],[4, 5, 6]])

print(a > 1)         #TrueかFalseで返す
print(b > 0)

np.count_nonzero(b > 0)       #0ではない要素数を出力(Falseを0として扱う)   #2
np.sum(b > 0)                 #Trueの数の合計を出力
np.any(b > 0)                 #要素にTrueが含まれているか判定
np.all(b > 0)                 #要素がすべてTrueか判定

b[b > 0]                      #条件に合致した要素だけ配列に残る

b == c                        #同じ形状の比較
a == b                        #一次元配列と二次元配列の比較

(b == c) | (a == b)           #array([[False, False, False], [True, True, True]])
b[(b == c) | (a == b)]        #array([0, 1, 2])

np.allclose(b, c)             #すべての要素が合致しているか判定    False
np.allclose(b, c, atol=10)    #すべての要素が誤差10以内か判定     True


#関数とメソッド
a = np.array([0, 1, 2])

np.sum(a)          #3
a.sum()            #3
