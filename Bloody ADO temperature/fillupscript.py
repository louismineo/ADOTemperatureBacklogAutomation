from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

PATH=r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def UpdateTempBackLog(date,AMorPM):

    PATH=r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    #GO TO SITE
    driver.get("https://temptaking.ado.sg/group/95f05ea55662a81d10b65590f6f9cdc6")
    #print(driver.title)


    #DATE
    if(len(str(date))<8):
        date = "0"+str(date)
    dateInput = driver.find_element_by_id('date-input')
    dateInput.send_keys(str(date))

    #AM OR PM
    AMPM = Select(driver.find_element_by_id('meridies-input'))
    AMPM.select_by_visible_text(AMorPM)

    #NAME
    nameBox = Select(driver.find_element_by_id('member-select'))
    nameBox.select_by_visible_text("ZAI AN")

    #PIN
    PIN="3198"
    for x in range (0,4):
        pinID = "ep"+str(x+1)
        #print(pinID)
        #print(PIN[x])
        pinInput = driver.find_element_by_id(pinID)
        pinInput.send_keys(PIN[x])


    #TEMPERATURE
    temp = str(round(random.uniform(358, 371)))
    #print(temp)
    #print(temp[0])
    #print(temp[1])
    #print(temp[2])

    for x in range (0,3):
        tempBoxID = "td"+str(x+1)
        #print(tempBoxID)
        #print(temp[x])
        tempInput = driver.find_element_by_id(tempBoxID)
        tempInput.send_keys(temp[x])

    #SUBMIT BUTTON 
    #XPATH = //*[@id="submit-temperature-container"]/button
    driver.find_element_by_xpath('//*[@id="submit-temperature-container"]/button').click()


    #CONFIRM button 
    #//*[@id="submit-temp-btn"]
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="submit-temp-btn"]').click()
    #id = "submit-temp-btn"

    #clickThis = new SelectElement(nameBox)
    #clickThis.SelectByText("LOUIS MINEO")

    driver.quit()
    return