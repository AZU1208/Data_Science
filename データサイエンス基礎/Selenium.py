
#pip install selenium
#brew install chromedriver (mac, chromeを使用する場合)

from selenium import webdriver
from time import sleep

sleep(3)              #三秒待つ
print("Here")

browser = webdriver.Chrome()    #macの場合

print(browser)

#browser = webdriver.Chrome("chromedriver.exe")     #Windowsの場合

browser.quit()

browser = webdriver.Chrome()

url = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(url)    #Webサイトにアクセス


elem_username = browser.find_element_by_id("username")    #idをusernameに指定
elem_username
elem_username.send_keys("imanishi")                       #imanishiを入力


elem_password = browser.find_element_by_id("password")    #idをpasswordに指定
elem_password.send_keys("kohei")                          #koheiを入力

elem_login_btn = browser.find_element_by_id("login-btn")   
elem_login_btn.click()                                     #loginボタンをクリック


elem = browser.find_element_by_id("name")
elem.text                                                  #テキストを抽出

elem = browser.find_element_by_id("company")
elem.text

elem = browser.find_element_by_id("birthday")
elem.text

elem = browser.find_element_by_id("come_from")
elem.text

elem = browser.find_element_by_id("hobby")
hobby = elem.text
hobby.replace("\n", " ")


#一括で情報を取り出す

elem_th = browser.find_element_by_tag_name("th")
elem_th.text  

elems_th = browser.find_elements_by_tag_name("th")
elems_th[1].text

keys = []
for elems_th in elems_th:
    key = elems_th.text
    keys.append(key)
print(keys)


elems_td = browser.find_elements_by_tag_name("td")

values =[]
for elems_td in elems_td:
    value = elems_td.text
    values.append(value)
print(values)

#データ化し、csvファイルに出力
import pandas as pd

df = pd.DataFrame()
df["項目"] = keys
df["値"] = values
print(df)

df.to_csv("講師情報.csv", index = False)  #indexの番号を削除する



#ランキングサイトから情報を取得

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")

elem_rankingBox = browser.find_element_by_class_name("u_areaListRankingBox")         #観光地１を取得
elem_title = elem_rankingBox.find_element_by_class_name("u_title").find_element_by_tag_name("h2")
title = elem_title.text  

title.split("\n")[1]
print(title)


elem = browser.find_element_by_class_name("u_rankBox")      #観光地１の総合評価を取得
elem = elem.find_element_by_class_name("evaluateNumber")
print(elem)


elem = browser.find_element_by_class_name("u_categoryTipsItem")     #楽しさの評価
elem = elem.find_elements_by_class_name("is_rank")[0]
elem = elem.find_element_by_class_name("evaluateNumber")


elem = browser.find_element_by_class_name("u_categoryTipsItem")     #人混みの多さの評価
elem = elem.find_elements_by_class_name("is_rank")[1]
elem = elem.find_element_by_class_name("evaluateNumber")


elem = browser.find_element_by_class_name("u_categoryTipsItem")      #景色の評価
elem = elem.find_elements_by_class_name("is_rank")[2]
elem = elem.find_element_by_class_name("evaluateNumber")


elem = browser.find_element_by_class_name("u_categoryTipsItem")       #アクセスの評価
elem = elem.find_elements_by_class_name("is_rank")[3]
elem = elem.find_element_by_class_name("evaluateNumber")













