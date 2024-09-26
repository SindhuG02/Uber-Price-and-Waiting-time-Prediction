from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import mysql.connector
import time
from datetime import datetime
import pandas as pd

# Initialize the WebDriver
chrome_options = Options()

service = Service( r'C:\chromedriver-win64\chromedriver.exe')  
driver = webdriver.Chrome(service=service, options=chrome_options)

def scroll_to_bottom(val):
    driver.execute_script(f"window.scrollTo(0,{val});")
    #driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

def convert_to_24hr(time_str):
    
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    # Format the datetime object to 24-hour format
    return time_obj.strftime("%H:%M")

def getdata(path,source_details,destination_details,count):

    dt_obj = datetime.now()
    ts_am_pm = dt_obj.strftime('%H:%M')
    driver.get(path)
    if count==0:
        time.sleep(180)
    else:
        time.sleep(10)
    
    loop_count=0
    for i in range(1,7):
        try:
            print(loop_count)
            if loop_count==2:
                break

            car_details=driver.find_element(By.XPATH,f'//*[@id="wrapper"]/div[1]/div/main/div/section/div[2]/ul/li[{i}]')
            print(car_details.text.split('\n'))
            details=car_details.text.split('\n')
            car_name=details[0][:-1]
            if car_name == 'Uber Go' or car_name=='Go Sedan':

                print(details[0][:-1])
                
                source.append(source_details)
                destination.append(destination_details)
                Car_name.append(details[0][:-1])
                capacity.append(details[0][-1:])
                waiting_time.append(details[1][:2])
                
                timeValue=details[1][-7:]
                
                converted_time=convert_to_24hr(timeValue)
                
                reaching_time.append(converted_time)
                current_time.append(ts_am_pm)
                price.append(details[3][1:])
                scroll_to_bottom(100)
                time.sleep(2)
                loop_count=loop_count+1
        except:
            pass
    

places=['Kempegowda International Airport Bengaluru->Nikoo Homes 2',
        'Kempegowda International Airport Bengaluru->Mysore Bank Colony',
        'Kempegowda International Airport Bengaluru->Majestic',
        'Kempegowda International Airport Bengaluru->Sarjapura',
        'Nikoo Homes 2->Mysore Bank Colony',
        'Nikoo Homes 2->Majestic',
        'Nikoo Homes 2->Sarjapura',
        'Nikoo Homes 2->Kempegowda International Airport Bengaluru',
        'Mysore Bank Colony->Majestic',
        'Mysore Bank Colony->Nikoo Homes 2',
        'Mysore Bank Colony->Sarjapura',
        'Mysore Bank Colony->Kempegowda International Airport Bengaluru',
        'Majestic->Kempegowda International Airport Bengaluru',
        'Majestic->Sarjapura',
        'Majestic->Nikoo Homes 2',
        'Majestic->Mysore Bank Colony',
        'Sarjapura->Mysore Bank Colony',
        'Sarjapura->Nikoo Homes 2',
        'Sarjapura->Kempegowda International Airport Bengaluru',
        'Sarjapura->Majestic']

links=['https://m.uber.com/go/product-selection?_gl=1%2Agczqyb%2A_gcl_au%2AMTEwMjk3OTk0Mi4xNzI1NjgxNjE1%2A_ga%2AMTE0MDY1Nzk4OC4xNzI1NTQ0MjQ2%2A_ga_XTGQLY6KPT%2AMTcyNTk2ODkwOC43LjAuMTcyNTk2OTA5NC4wLjAuMA..&drop%5B0%5D=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%22%2C%22addressLine2%22%3A%22Bhartiya%20City%2C%20Thanisandra%20Main%20Rd%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&pickup=%7B%22addressLine1%22%3A%22Kempegowda%20International%20Airport%20Bengaluru%22%2C%22addressLine2%22%3A%22Karnataka%22%2C%22id%22%3A%22ChIJZWJEdf4crjsRjkEpoelwbCk%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.198909%2C%22longitude%22%3A77.7068926%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Kempegowda%20international%20airport%22%2C%22addressLine2%22%3A%22Terminal%202%2C%20Airport%20City%20South%2C%20Bengaluru%2C%20Hunachur%2C%20Karnataka%22%2C%22id%22%3A%22ChIJnWP5QgAdrjsRw58Z8sryK4M%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.1937132%2C%22longitude%22%3A77.6975724%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Kempegowda%20international%20airport%22%2C%22addressLine2%22%3A%22Terminal%202%2C%20Airport%20City%20South%2C%20Bengaluru%2C%20Hunachur%2C%20Karnataka%22%2C%22id%22%3A%22ChIJnWP5QgAdrjsRw58Z8sryK4M%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.1937132%2C%22longitude%22%3A77.6975724%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Kempegowda%20international%20airport%22%2C%22addressLine2%22%3A%22Terminal%202%2C%20Airport%20City%20South%2C%20Bengaluru%2C%20Hunachur%2C%20Karnataka%22%2C%22id%22%3A%22ChIJnWP5QgAdrjsRw58Z8sryK4M%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.1937132%2C%22longitude%22%3A77.6975724%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%22%2C%22addressLine2%22%3A%22Bhartiya%20City%2C%20Thanisandra%20Main%20Rd%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%22%2C%22addressLine2%22%3A%22Bhartiya%20City%2C%20Thanisandra%20Main%20Rd%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%22%2C%22addressLine2%22%3A%22Bhartiya%20City%2C%20Thanisandra%20Main%20Rd%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Kempegowda%20International%20Airport%20Bengaluru%22%2C%22addressLine2%22%3A%22Karnataka%22%2C%22id%22%3A%22ChIJZWJEdf4crjsRjkEpoelwbCk%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.198909%2C%22longitude%22%3A77.7068926%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%22%2C%22addressLine2%22%3A%22Bhartiya%20City%2C%20Thanisandra%20Main%20Rd%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&vehicle=20001457',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%22%2C%22addressLine2%22%3A%22Bhartiya%20City%2C%20Thanisandra%20Main%20Rd%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&vehicle=20009513',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Kempegowda%20international%20airport%22%2C%22addressLine2%22%3A%22Airport%20City%20South%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJnWP5QgAdrjsRw58Z8sryK4M%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.1937132%2C%22longitude%22%3A77.6975724%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&vehicle=20001457',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Kempegowda%20international%20airport%22%2C%22addressLine2%22%3A%22Airport%20City%20South%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJnWP5QgAdrjsRw58Z8sryK4M%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.1937132%2C%22longitude%22%3A77.6975724%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&vehicle=20001457',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%20Bhartiya%20City%22%2C%22addressLine2%22%3A%22Thanisandra%20Main%20Road%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Mysore%20Bank%20Colony%22%2C%22addressLine2%22%3A%22Srinivasnagar%2C%20Banashankari%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJTQavniM-rjsRmvEMjosdZrM%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.939043%2C%22longitude%22%3A77.5526275%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&vehicle=20009513',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Nikoo%20Homes%202%20Bhartiya%20City%22%2C%22addressLine2%22%3A%22Thanisandra%20Main%20Road%2C%20Devin%20Paradise%20Enclave%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJaVcsLZMZrjsRDgNCSzkKj0s%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.0809606%2C%22longitude%22%3A77.6401636%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Kempegowda%20international%20airport%22%2C%22addressLine2%22%3A%22Airport%20City%20South%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJnWP5QgAdrjsRw58Z8sryK4M%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A13.1937132%2C%22longitude%22%3A77.6975724%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&vehicle=20001457',
       'https://m.uber.com/go/product-selection?drop%5B0%5D=%7B%22addressLine1%22%3A%22Majestic%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJi-t8KwUWrjsRlp-L9ykb2_k%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.9766637%2C%22longitude%22%3A77.5712556%2C%22provider%22%3A%22google_places%22%7D&effect=&pickup=%7B%22addressLine1%22%3A%22Sarjapura%22%2C%22addressLine2%22%3A%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22id%22%3A%22ChIJfyvmH-FyrjsRD0NBLLRY-5A%22%2C%22source%22%3A%22SEARCH%22%2C%22latitude%22%3A12.8575579%2C%22longitude%22%3A77.7864057%2C%22provider%22%3A%22google_places%22%7D&vehicle=2007'
       
       ]

count=0
while True:
    source=[]
    destination=[]
    Car_name=[]
    capacity=[]
    waiting_time=[]
    reaching_time=[]
    current_time=[]
    price=[]

    for i in range (len(links)):
        val=places[i]
        val=val.split('->')
        source_details=val[0]
        destination_details=val[1]
        getdata(links[i],source_details,destination_details,count)
        count=count+1
        

    CarDetails={'source':source,'destination':destination,"car_type":Car_name,'capacity':capacity,'currenttime':current_time,'drop_off_time':reaching_time,'waiting_time':waiting_time,'Price':price}
    df=pd.DataFrame(data=CarDetails)
    #df.to_csv('Car_details.csv')
    
    print(current_time)
    print(reaching_time)
    
    #once each government bus gets completed now we will store in SQL
    con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678'
        )
    cursor=con.cursor()
        
    cursor.execute('use Uber')
    data = [tuple(row) for row in df.values]
    print(data)
    sql = "INSERT INTO uber_details (source,destination,car_type,capacity,currenttime,drop_off_time,waiting_time,Price) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"

    cursor.executemany(sql, data)
    #save permentaly into db
    con.commit()
    print("Sleeping")
    
    time.sleep(900)    #sleep for 30 minutes
    print("WokeUp")