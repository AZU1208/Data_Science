#%%
import pandas as pd

customer_master = pd.read_csv('customer_master.csv')
customer_master.head()

#%%
item_master = pd.read_csv('item_master.csv')
item_master.head()

#%%
transaction_1 = pd.read_csv('transaction_1.csv')
transaction_1.head()

#%%
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
transaction_detail_1.head()

#%%
#結合（ユニオン）: データの行（縦方向）に増やす

transaction_2 = pd.read_csv('transaction_2.csv')
transaction = pd.concat([transaction_1, transaction_2], ignore_index = True)
transaction.head()

#%%
#ユニオンされているか確認

print(len(transaction_1))
print(len(transaction_2))
print(len(transaction))

#%%
#ユニオン

transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail = pd.concat([transaction_detail_1,transaction_detail_2], ignore_index = True)
transaction_detail.head()

#%%
#結合（ジョイン）：　データの列（横方向）に増やす
#transaction_idをキーに結合される

join_data = pd.merge(transaction_detail, transaction[["transaction_id","payment_date","customer_id"]], on = "transaction_id", how = "left")
join_data.head()

#%%
#データ件数確認

print(len(transaction_detail))
print(len(transaction))
print(len(join_data))

# %%
#マスターデータをジョイン

join_data = pd.merge(join_data, customer_master, on = "customer_id", how = "left")
join_data = pd.merge(join_data, item_master, on = "item_id", how = "left")
join_data.head()

# %%
#price列を作成
#price = quantity * item_price

join_data["price"] = join_data["quantity"] * join_data["item_price"]
join_data[["quantity", "item_price", "price"]].head()

# %%
#priceのデータ数を検算

print(join_data["price"].sum())
print(transaction["price"].sum())
join_data["price"].sum() == transaction["price"].sum()

# %%
#欠損値の確認

join_data.isnull().sum()

#%%
#各種統計量の確認

join_data.describe()

# %%
#データ期間範囲の確認

print(join_data["payment_date"].min())
print(join_data["payment_date"].max())

# %%
#月別でデータを集計する
#payment_dateのデータ型を確認

join_data.dtypes

# %%
#payment_dateがobject(文字)型なのでdatetime型に変換

join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])  #to_datetimeでdatetime型に変換
join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")  #dt.strftimeで年月を作成
join_data[["payment_date", "payment_month"]].head() 

# %%
#月別データの確認

join_data.groupby("payment_month").sum()["price"]

# %%
#月別、商品別でデータを集計

join_data.groupby(["payment_month", "item_name"]).sum()[["price", "quantity"]]

# %%
#pivot_tableを使用して集計

pd.pivot_table(join_data, index='item_name', columns='payment_month', 
values=['price', 'quantity'], aggfunc='sum')

#%%
#商品別の売上推移を可視化

graph_data = pd.pivot_table(join_data, index='payment_month', 
columns='item_name', values='price', aggfunc='sum')
graph_data.head()

# %%

import matplotlib.pyplot as plt
%matplotlib inline 

plt.plot(list(graph_data.index), graph_data["PC-A"], label='PC-A')
plt.plot(list(graph_data.index), graph_data["PC-B"], label='PC-B')
plt.plot(list(graph_data.index), graph_data["PC-C"], label='PC-C')
plt.plot(list(graph_data.index), graph_data["PC-D"], label='PC-D')
plt.plot(list(graph_data.index), graph_data["PC-E"], label='PC-E')
plt.legend()