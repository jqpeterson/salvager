
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(options=options)

# cookie: hotUtilsSession=<sessionkey>; hotUtilsAllyCode=<allycode>
hucookie1 = {'name':'hotUtilsSession','value':'<sessionkey>'}
hucookie2 = {'name':'hotUtilsAllyCode','value':'<allycode>'}

driver.get("https://hotutils.com/player/salvage/")
driver.add_cookie(hucookie1)
driver.add_cookie(hucookie2)
driver.get("https://hotutils.com/player/salvage/")
driver.implicitly_wait(15)

partHaveList = []

gearHaveList = driver.find_elements(By.XPATH, "*//tr[@data-row-key]")
for part in gearHaveList:
    pname = part.find_element(By.XPATH, './/td[2]/div').text
    phave = part.find_element(By.XPATH, './/td[4]').text
    partHaveEntry = {
        'part_name' : pname,
        'part_have' : phave
    }
    partHaveList.append(partHaveEntry)

with open('GearHave.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['part_name','part_have'])
    writer.writerows(partHaveList)

driver.get("https://swgoh.gg/p/<allycode>/gear-needed/")

driver.implicitly_wait(2)

partNeedList = []

gearNeedlist = driver.find_elements(By.XPATH, "*//li[@class='media list-group-item character gear-needed__header']")
for part in gearNeedlist:
    pname = part.find_element(By.XPATH, './/h5').text
    pnumber = part.find_element(By.XPATH, './/p/strong').text
    needEntry = {
        'part_name' : pname,
        'part_need' : pnumber
    }
    partNeedList.append(needEntry)
    
with open('GearNeed.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['part_name','part_need'])
    writer.writerows(partNeedList)
    
driver.quit()
