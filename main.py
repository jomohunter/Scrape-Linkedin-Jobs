from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
import pyperclip



driver = webdriver.Chrome("C:/Users/Admin/Downloads/chromedriver_win32/chromedriver")


driver.get("https://linkedin.com/uas/login")


time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys("maghraoui.joseph@gmail.com") 

pword = driver.find_element(By.ID, "password")
pword.send_keys("jomo2002")       


driver.find_element(By.XPATH, "//button[@type='submit']").click()




time.sleep(2)



url = "https://www.linkedin.com/jobs/search/?currentJobId=3487736739&distance=25&f_E=1%2C2&geoId=92000000&keywords=cyber%20security&location=Worldwide&refresh=true"



driver.get(url)


button = driver.find_element_by_id("ember285")
actions = ActionChains(driver)
actions.context_click(button).perform()

copy_link = driver.find_element_by_xpath("//span[text()='Copy link address']")
copy_link.click()
copied_link = pyperclip.paste()
print(copied_link)





# find the ul element
ul_list = driver.find_element(By.XPATH,'//ul[@class="scaffold-layout__list-container"]')

# find all the li elements inside the ul element
li_elements = ul_list.find_elements(By.XPATH,'.//li')

number = 0 
# click each li element
for li_element in li_elements:
    
    src = driver.page_source
    actions = ActionChains(driver)
    actions.move_to_element(li_element).click().perform()

    time.sleep(2)
    soup = bs(src, 'lxml')

    jobDesc = soup.find('div', {'class': 'relative jobs-unified-top-card__container--two-pane'})



    job_title = jobDesc.find('h2', {'class': 't-24 t-bold jobs-unified-top-card__job-title'}).text
    company_name = jobDesc.find('a', {'class': 'ember-view t-black t-normal'}).text
    location = jobDesc.find('span', {'class': 'jobs-unified-top-card__bullet'}).text
    

    with open('result', 'a') as f:
        f.write("\n")
        f.write(str(number))
        f.write(" begins here:")
        number += 1




        f.write(str(job_title))
        f.write(str(company_name))





        f.write("Seperator =============================================================================")
        f.write("\n")
        f.write("\n")
        f.write("\n")
        time.sleep(1)




