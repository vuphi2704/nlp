# NLP - GIT - VUPHI - 0510

## crawler_mubannet
Using bs4 , request , pymongo library 

This module contains two function : **crawler_outside** and **crawler_inside** . 

The **crawler_outside** takes the list of URL as a parameter , it will lopp through all the news and retrieve infomation like title , area , price , location of the real estate.

The **crawler_inside** will get into specific new to retrieve detail information , URL links , additional information.

## vndirect

All  modules uses bs4 , request , pymongo libray except **lich_va_su_kien_crawler.py**.

The principal of this modules just like the crawler_mubannet module , it will lopp through all the news and get into every new to retrieve information.

The **lich_va_su_kien_crawler.py** is different from the other modules , because when clicking to go to next page of the category "lich va su kien " , the URL do not change . So this module use **selenium** library to simulate the click action .

**Note : If you using Firefox as the selenium driver , you must download the [geckodriver](https://github.com/mozilla/geckodriver/releases) , extract it and copy the driver to /usr/local/bin and finally make it executable (chmod +x geckodriver)**.


