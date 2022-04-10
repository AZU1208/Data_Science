import pandas as pd
import numpy as np

#Series(1次元データ)
ser = pd.Series([10, 20, 30, 40])
print(ser)


#DataFrame(2次元データ)
df = pd.DataFrame([[10, "a", True],
                    [20, "b", False],
                    [30, "c", False],
                    [40, "d", True]])
print(df)


#DataFrame概要
df = pd.DataFrame(np.arange(100).reshape((25, 4)))

df.head()     #先頭５行表示
df.tail()     #末尾５行表示
df.shape    #行列の確認


#インデックス名、カラム名
df = pd.DataFrame(np.arange(6).reshape((3, 2)))
df.index = ["01", "02", "03"]
df.columns = ["A", "B"]
print(df)

named_df = pd.DataFrame(np.arange(6).reshape((3, 2)), 
           columns=["A列", "B列"], 
           index=["1行目", "2行目", "3行目"]) 
print(named_df)

df = pd.DataFrame({"A列": [0, 2, 4], "B列": [1, 3, 5]})
print(df)


#データ抽出
df = pd.DataFrame(np.arange(12).reshape((4, 3)),
                  index = ["1行目", "2行目", "3行目", "4行目"],
                  columns = ["A", "B", "C"])
print(df)
print(df["A"])
print(df[["A", "B"]])
print(df[:2])


#データの抽出(locメソッド)
df = pd.DataFrame(np.arange(12).reshape((4, 3)),
                  index = ["1行目", "2行目", "3行目", "4行目"],
                  columns = ["A", "B", "C"])

#locメソッドは参照
df.loc[:, :]                   #すべて出力
df.loc[:, "A"]                 #A列を出力
df.loc[:, ["A", "B"]]          #A,B列を出力
df.loc["1行目", :]              #１行目の行を出力
df.loc[["1行目", "3行目"], :]    #1行目と3行目の行を出力
df.loc[["1行目"], ["A", "C"]]   #1行目のA,C列を出力

#ilocメソッドはインデックス番号、カラム番号で出力
df.iloc[1,1]
df.iloc[1:, 1]
df.iloc[1:, :2]


#データの読み込み・書き込み
df = pd.read_csv("201704health.csv", encoding = "utf-8")     #csvファイルの読み込み
print(df)

df = pd.read_excel("201704health.xlsx")     #excelファイルの読み込み
print(df)


#データ読み込み: WebサイトのHTMLから表を取得
import pandas as pd

url = "https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%83%E3%83%97%E3%83%AC%E3%83%99%E3%83%AB%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E4%B8%80%E8%A6%A7"
tables = pd.read_html(url)
print(len(tables))

df = tables[4]
print(df)


#データの書き込み
df.to_csv("write_data.csv")        #csvファイルの書き出し
df.to_excel("write_data.xlsx")     #excelファイルの書き出し


#データの再利用
df.to_pickle("write_df.pickle")          #pickleメソッドで書き出し
df = pd.read_pickle("write_df.pickle")   #pickle形式のファイルを読み込み


#データの整形
df = pd.read_excel("201704health.xlsx")
print(df)

df["歩数"] >= 10000                     #True,Falseで返す

df_selected = df[df["歩数"] >= 10000]   #歩数10000以上のデータだけ
print(df_selected)
print(df_selected.shape)

df.query('歩数 >= 10000 and 摂取カロリー <= 1800')  #queryメソッドを使ってデータ抽出


#データ型変換
df.dtypes        #カラムデータの確認

df.loc[:, 'date'] = df.loc[:, '日付'].apply(pd.to_datetime)
df.loc[:, "date"]
print(df)

df.loc[:, "摂取カロリー"] = df.loc[:, "摂取カロリー"].astype(np.float32)
df = df.set_index("date")
df.head()


#並び替え
df.sort_values(by="歩数")     #歩数が少ない順に並び替え
df.sort_values(by="歩数", ascending=False)    #歩数の多い順に並び替え


#不要なカラムの削除
df = df.drop("日付", axis=1)       #日付カラムを削除
print(df)

#組み合わせデータの挿入
df.loc[:, "歩数/カロリー"] = df.loc[:, "歩数"] / df.loc[:, "摂取カロリー"]   #歩数をカロリーで割ったカラムを挿入
print(df)


def exercise_judge(ex):
    if ex <= 3.0:
        return "Low"
    elif 3.0 < ex <= 6.0:
        return "Mid"
    else:
        return "High"

df.loc[:, "運動指数"] = df.loc[:, "歩数/カロリー"].apply(exercise_judge)   #applyメソッドを使用して、その結果を運動指数カラムを格納
print(df)

df.to_pickle("df_201704health.pickle")     #後で使うので書き出し

df_moved = pd.get_dummies(df.loc[:, "運動指数"], prefix = "運動")    #dummies関数
print(df_moved)

df_moved.to_pickle("df_201704moved.pickle")     #後で書き出し


#一ヶ月分のデータ
dates = pd.date_range(start="2017-04-01", end="2017-04-30")    #date_rangeで一ヶ月分のデータを作成
print(dates)

np.random.seed(123)
df = pd.DataFrame(np.random.randint(1, 31, 30), index=dates, columns=["乱数"])   #データフレーム作成
print(df)


#1年分のデータ
dates = pd.date_range(start="2017-01-01", periods=365)    #1年分のデータを作成
print(dates)

np.random.seed(123)
df = pd.DataFrame(np.random.randint(1, 31, 365), index=dates, columns=["乱数"])   #データフレーム作成
print(df)


#月平均のデータ
df.groupby(pd.Grouper(freq="M")).mean()     #毎月の平均値を作成

df.loc[:, "乱数"].resample('M').mean()       #resampleメソッドを使用して毎月の平均値を作成


#複雑な条件のインデックス
pd.date_range(start="2017-01-01", end="2017-12-31", freq="W-SAT")   #1年分の土曜日の日付データ作成

df_year = pd.DataFrame(df.groupby(pd. Grouper(freq="W-SAT")).sum(), columns=["乱数"])   #土曜日までの一週間単位でまとめる
print(df_year)


#欠損値
df_201705 = pd.read_csv("201705health.csv", encoding="utf-8", index_col="日付", parse_dates=True)
print(df_201705)

df_201705_drop = df_201705.dropna()     #欠損値の行を削除
print(df_201705_drop)

df_201705_fillna = df_201705.fillna(0)    #欠損値に0を代入
print(df_201705_fillna) 

df_201705_fill = df_201705.fillna(method='ffill')   #欠損値を一つ前の値で補完
print(df_201705_fill)

df_201705_fillmean = df_201705.fillna(df_201705.mean())     #欠損値を他の値の平均で補完
print(df_201705_fillmean)


#データの連結
df = pd.read_pickle("df_201704health.pickle")
print(df)

df_moved = pd.read_pickle("df_201704moved.pickle")
print(df_moved)


df_merged = pd.concat([df, df_moved], axis=1)   #列方向にデータ連結
print(df_merged)

df_merged_0405 = pd.concat([df_merged, df_201705_fill], axis=0, sort=True)   #行方向にデータを連結
print(df_merged_0405)


#統計データの扱い

df = pd.read_pickle("df_201704health.pickle")
print(df)

df.loc[:, "摂取カロリー"].max()                   #摂取カロリーの最大値
df.loc[:, "摂取カロリー"].min()                   #摂取カロリーの最小値
df.loc[:, "摂取カロリー"].mode()                  #摂取カロリーの最頻値
df.loc[:, "摂取カロリー"].mean()                  #摂取カロリーの平均値
df.loc[:, "摂取カロリー"].median()                #摂取カロリーの中央値
df.loc[:, "摂取カロリー"].std()                   #摂取カロリーの標準偏差
df.loc[:, "摂取カロリー"].std(ddof=0)             #摂取カロリーの母集団の標準偏差
df.loc[df.loc[:, "摂取カロリー"]==2300].count()   #摂取カロリーが2300のデータの件数を出力


#要約
df.describe()   #統計量をまとめて出力


#相関係数
df.corr()       #相関係数を出力


#散布図行列
import pandas as pd
from pandas.plotting import scatter_matrix

df = pd.read_pickle("df_201704health.pickle")
print(df)

graph = scatter_matrix(df)      #散布図行列を描写
print(graph)


#データ変換
df.loc[:, ["歩数", "摂取カロリー"]]
df.loc[:, ["歩数", "摂取カロリー"]].values     #NumPyの配列に変換