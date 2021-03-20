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
auto(475,845,1)
elem5=dr.find_element_by_class_name("layerFullBtn")
elem5.click()
elem6=dr.find_element_by_id("user_name_input")
elem6.send_keys("이유준")
elem7=dr.find_element_by_id("birthday_input")
elem7.send_keys("050624")
elem8=dr.find_element_by_id("btnConfirm")
elem8.click()
#elem9=dr.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input')
#elem9.click()
auto(1192,591,1)
pyperclip.copy("7862")
pt.hotkey('ctrl','v')
elem10=dr.find_element_by_id("btnConfirm")
elem10.click()
auto(537,971,1)
elem11=dr.find_element_by_id("survey_q1a1")
elem.click()
"""auto(903,697,1)
pt.click()
auto(681,443,1)
auto(743,884,1)#시, 도 설정
auto(675,569,1)
auto(676,815,1)#학력 설정
auto(765,687,1)
pyperclip.copy("양지고등학교")
pt.hotkey('ctrl','v')
auto(1592,697,1)
auto(388,852,1)
pt.scroll(-500)
auto(1038,883,1)#설정 완료
auto(911,843,1)
pyperclip.copy("이유준")
pt.hotkey('ctrl','v')
auto(862,995,1)
pyperclip.copy("050624")
pt.hotkey('ctrl','v')
pt.scroll(-600)
auto(1120,659,1)#개인정보 입력 완료
auto(1192,591,1)
pyperclip.copy("7862")
pt.hotkey('ctrl','v')
auto(1102,761,1)#비밀번호 입력
auto(537,971,1)
for i in range(5):
    pt.scroll(-200)
auto(139,864,1)
for i in range(12):
    pt.scroll(-300)
auto(124,446,1)
auto(124,779,1)
auto(857,910,1)"""
