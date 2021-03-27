from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pyautogui as pt
import time
import pyperclip
ps="7862"
def auto(x,y,t):
    pt.moveTo(x,y,duration=t)
    pt.click()
#dr=webdriver.Chrome()
pt.FAILSAFE=False
op=webdriver.ChromeOptions()
op.add_argument("--start-maximized")
dr=webdriver.Chrome(options=op)
dr.get("https://hcs.eduro.go.kr/#/relogin")
elem=dr.find_element_by_id("btnConfirm2")
elem.click()
elem1=dr.find_element_by_id("schul_name_input")
elem1.click()
elem2=dr.find_element_by_id("sidolabel")
elem2.click()
ele=Select(elem2)
ele.select_by_index(8)
elem3=dr.find_element_by_id("crseScCode")
elem3.click()
ele2=Select(elem3)
ele2.select_by_index(4)
dr.find_element_by_id("orgname").send_keys("양지고등학교")
elem4=dr.find_element_by_class_name("searchBtn")
elem4.click()
dr.find_element_by_class_name("layerSchoolArea").click()
time.sleep(2)
elem5=dr.find_element_by_class_name("layerFullBtn")
elem5.click()
time.sleep(2)
elem6=dr.find_element_by_id("user_name_input")
elem6.send_keys("이유준")
elem7=dr.find_element_by_id("birthday_input")
elem7.send_keys("050624")
elem8=dr.find_element_by_id("btnConfirm")
elem8.click()
time.sleep(3)
dr.find_element_by_class_name("input_text_common").click()
pyperclip.copy("7862")
pt.hotkey('ctrl','v')
elem10=dr.find_element_by_id("btnConfirm")
elem10.click()
time.sleep(2)
dr.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click()
time.sleep(2)
dr.find_element_by_id("survey_q1a1").click()
dr.find_element_by_id("survey_q2a1").click()
dr.find_element_by_id("survey_q3a1").click()
time.sleep(2)
dr.find_element_by_id("btnConfirm").click()






