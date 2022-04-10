#SOLコマンド実行順番
1.FROM
2.WHERE
3.GROUP BY
4.HAVING
5.SELECT
6.ORDER BY


#select カラム名
#from テーブル名;

select ID
from test_table;


select ID, 売上日, 社員ID　　　#複数のカラムを指定
from test_table;


select ID as id_number      #asで名前を変換
from test_table;


select *                   #*はワイルドカード
from test_table;



#whereの使い方

select *　　　　　　　　　　　　#select カラム名
from test_table             #from テーブル名
where id = 2　　　　　　　　　 #where 条件式;


select * 
from test_table
where id > 2


select *
from test_table
where 商品名 = "ニット"


#order byの使い方

#select カラム名
#from テーブル名
#order by 並び替え条件


select *
from test_table
order by 売上金額 ASC        #昇順（ascending)に並び替え


select *
from test_table
order by 売上金額 DESC       #降順（descending)に並び替え


select *
from test_table
order by 売上金額, 売上日      #複数を指定（最初のカラムが優先）


select *
from test_table
order by 売上金額 DESC , 売上日 ASC   #複数の昇順、降順を指定


#Groupbyの使い方

#SELECT グルーピングをするカラム, 集計関数(集計対象カラム)
#FROM テーブル式
#WHERE 条件式
#GROUP BY  グルーピングするカラム
#ORDER BY　ソート条件式


select 商品分類, sum(売上金額)
from test_table
group by  商品分類


select 商品分類, sum(売上金額)
from test_table
group by  商品名


select 商品分類, sum(売上金額)
from test_table
group by  商品名
order by sum(売上金額)


select 
	商品名
	, avg(売上金額)
	,min(売上金額)
	,max(売上金額)
from test_table
group by  商品名


select 
	商品名
	, count(売上金額)
from test_table
group by  商品名


select  count(*)
from test_table


#Havingの使い方

#SELECT グルーピングをするカラム, 集計関数(集計対象カラム)
#FROM テーブル式
#WHERE 条件式
#GROUP BY  グルーピングするカラム
#HAVING 集計関数(集計対象カラム)で条件式
#ORDER BY　ソート条件式

select
    商品名
    ,sum(売上金額)
from test_table
group by 商品名
having sum(売上金額) >= 1000000


select
    商品名
    ,sum(売上金額)
from test_table
where 商品名 != "ジャケット"
group by 商品名
having sum(売上金額) <= 1000000
