import requests
from  bs4 import BeautifulSoup
import json
from pymongo import MongoClient
def nhan_dinh_thi_truong_hang_ngay(urls):
    client = MongoClient("116.105.223.232",27017)
    db=client.vndirect
    data_final  = {}
    i = 0 
    for url in urls:
        print (url)
        page  =  requests.get(url).text
        soup  = BeautifulSoup(page , "html.parser")
        news_info = soup.find_all("div" , {"class":"news-infor"})
        for new in news_info:
            data_temp  = {}
            i = i +1
            content = ""
            title = new.find('a' , href = True).text
            #print(title)
            link = new.find('a' , href = True)['href']
            page_inside = requests.get(link).text
            soup_inside = BeautifulSoup(page_inside , "html.parser")
            content_inside  = soup_inside.find("section", {"class" :"single-content content-text"}).text
            data_temp["Title"] = title
            data_temp["Content"] = content_inside
            db.Nhan_Dinh_Thi_Truong_Hang_Ngay.insert_one(data_temp)
            data_final["Object " + str(i)] = data_temp
    #data_final_json = (json.dumps(data_final, ensure_ascii=False).encode('utf8')).decode()

    
    print (data_final)


urls = ["https://www.vndirect.com.vn/category/nhan-dinh-thi-truong/"]
for x in range(2,44):
    urls.append("https://www.vndirect.com.vn/category/nhan-dinh-thi-truong/page/" + str(x)+ "/")
nhan_dinh_thi_truong_hang_ngay(urls)