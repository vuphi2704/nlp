from selenium import webdriver
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC 
import contextlib
import time
from pymongo import MongoClient
data_final = {}
def lich_va_su_kien():
    client = MongoClient("116.105.223.232",27017)
    db=client.vndirect
    with contextlib.closing(webdriver.Firefox()) as browser:
        browser.get('https://www.vndirect.com.vn/lich-va-su-kien/')
        keys =  ("Ma Ck","Loai Su Kien","Ngày GDKHQ","Ngày chốt","Ngày thực hiện" , "Chi tiết")
        wait = UI.WebDriverWait(browser, 10)
        for i in range(2647):    
            next_page_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='next page-numbers']/i[@class='fa fa-angle-right']")))
            table_body = browser.find_element_by_xpath("//table[@id='eventsTable' and @class='table']").find_element_by_tag_name("tbody")
            rows = table_body.find_element_by_tag_name("tr")
            #print (len(rows))
            data_temp = {}        
            for x in range(1,16):
                for y in range(1,7):
                    cell = table_body.find_element_by_xpath("//tr[{}]/td[{}]".format(str(x),str(y))).text
                    if y == 1:
                        data_temp["_id"] = cell + str(x) + str(y) + str(i)
                    data_temp[keys[y-1]] =  cell
                db.Lich_Va_Su_Kien.insert_one(data_temp)
                
                print (data_temp)

                    
            #print(len(count_rows))
            
            
            next_page_link.click()
            
lich_va_su_kien()