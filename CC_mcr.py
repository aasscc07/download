from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

ClassName = ""
ID = ""
PW = ""
try :

    ClassName = sys.argv[1]
    ID = sys.argv[2]
    PW = sys.argv[3]
except:
    pass

# if(ClassName == None & ID == None & PW == None):        
#     ClassName = input("ClassName : ")
#     ID = input("ID : ")
#     PW = input("PW : ")
# else:
#     pass

ClassName = input("ClassName : ")
ID = input("ID : ")
PW = input("PW : ")
MemorizationCount = int(input("암기(횟수) : "))
ReCallCount = int(input("리콜(횟수) : "))
SpellCount = int(input("스펠(횟수) : "))

# url = 'https://www.classcard.net/set/664099/958465'
LoginUrl = 'https://www.classcard.net/Login'


def Information(ClassUrl):
    response = requests.get(ClassUrl)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        font_bold = soup.find_all('div',class_='font-bold')
        # print(fo
        # nt_bold)
        wordset = soup.find_all('div',class_='cc-table middle fill-parent')
        EwordSet = []
        KwordSet = []

        for i,words in enumerate(wordset):
            if i % 2 == 0:
                #English
                Eword = words.div.text.strip()
                EwordSet.append(Eword)
            else:
                #Korean
                Kword = words.div.text.strip()
                KwordSet.append(Kword)

        return (EwordSet,KwordSet)
        
        
    else : 
        print(response.status_code)


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# # driver = webdriver.Chrome('cd/chromedriver')
# driver = webdriver.Chrome('cd/chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(2)


#========< Login Page >============#
driver.get(LoginUrl)

LoginID = driver.find_element(By.ID,"login_id")
LoginPW = driver.find_element(By.ID,'login_pwd')
LoginButton = driver.find_element(By.XPATH,"//*[@class=\'checkbox primary text-primary text-center m-t-md\']/button")


LoginID.send_keys(ID)
LoginPW.send_keys(PW)

LoginButton.click()

time.sleep(1)

#Main Page
driver.get(driver.current_url)

ClassName1 = "고교공통 NE능률 양현권 레슨 4"
# ClassName1 = ClassName.strip()
ClassSpan1 = driver.find_element(By.PARTIAL_LINK_TEXT,ClassName1)
ClassSpan1.click()

time.sleep(0.5)

#Current Class Page
ClassPage = driver.current_url
driver.get(driver.current_url)
time.sleep(1)

EwordSet,KwordSet = Information(ClassPage)


#암기 부분
def spell(Repeat):
    for k in range(Repeat):
        # MemorizationButton = driver.find_element(By.XPATH,"//*[@class=\'cc-table fill-parent m-t\']/div[@class=\'font-0\']/div[3]")
        # MemorizationButton.click()
        MemorizationButton = driver.find_element(By.XPATH,"//*[@class=\'cc-table fill-parent m-t\']/div[@class=\'font-0 pos-relative\']/div[3]")
        MemorizationButton.click()



        #스펠
        time.sleep(1)
        driver.get(driver.current_url) 

        StartSpellStudy = driver.find_element(By.PARTIAL_LINK_TEXT,"스펠 학습 시작")
        StartSpellStudy.click()

        time.sleep(2)
        spellInput = driver.find_elements(By.XPATH,f"//*[@class='text-normal spell-input']/input[1]")

        spellInput = driver.find_elements(By.XPATH,f"//*[@class='text-normal spell-input']/input[1]")

        for i in range(int(driver.find_element(By.XPATH,"//*[@class='total_count']").text)):
            time.sleep(1)
            ENSpellCheckDiv = driver.find_element(By.XPATH,"//*[@class=\'study-body fade in\']")
            spellCheckButton = driver.find_element(By.XPATH,"//*[@class='btn btn-xl btn-primary shadow mw-250 btn-confirm']")
            spellCheckButton2 = driver.find_element(By.XPATH,"//*[@class='btn-text btn-next-box']/a[@class='btn btn-xl btn-default shadow mw-250 btn-short-change-next']")

            word__ = ENSpellCheckDiv.text.replace("힌트보기","").strip()
            knownCound_ = driver.find_element(By.CLASS_NAME,'known_count').text
            a = driver.find_element(By.XPATH,"//*[@class='text-success']/span[@class='known_count']").text

            # print(word__)
            for j,w in enumerate(KwordSet):
                # print(j)
                if word__ == w:

                    spellInput[i].send_keys(EwordSet[j])

            spellCheckButton.click()
            time.sleep(2)
            spellCheckButton2.click()
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT,"다음 구간으로 이동").click()
        time.sleep(1) 
        # driver.find_element(By.PARTIAL_LINK_TEXT,"학습종류").click()    
        # time.sleep(0.4)
        # driver.find_element(By.LINK_TEXT,"학습종류").click()
        # time.sleep(1)
        driver.get(ClassPage)
        time.sleep(1)
    
#리콜
def recall(Repeat):
    for cction in range(Repeat):
        driver.find_element(By.XPATH,"//*[@class=\'cc-table fill-parent m-t\']/div[@class=\'font-0\']/div[2]").click()
        time.sleep(3)
        driver.find_element(By.PARTIAL_LINK_TEXT,"리콜 학습 시작").click()

        recallstudyEnword = driver.find_elements(By.XPATH,"//*[@class='normal-body']")
        # choA = driver.find_elements(By.XPATH,"//*[@class='card-quest card-quest-front']")
        # A = driver.find_elements(By.XPATH,"//*[@class='card-quest-list']/div[@class='cc-ellipsis l1']")

        time.sleep(3)
        total_count_recall = int(driver.find_element(By.XPATH,"//*[@class='total_count']").text.strip())
        known_count_recall = int(driver.find_elements(By.XPATH,"//*[@class='known_count']")[1].text.strip())
        for i in range(total_count_recall - known_count_recall):
            cho_ = driver.find_elements(By.XPATH,"//*[@class='card-quest-list']")
            for j,w in enumerate(EwordSet):
                ctemp = 4 * i
                if recallstudyEnword[i].text.strip() == w:
                    if KwordSet[j] == cho_[0 + ctemp].text.strip():
                        cho_[0 + ctemp].click()

                    elif KwordSet[j] == cho_[1 + ctemp].text.strip():
                        cho_[1 + ctemp].click()

                    elif KwordSet[j] == cho_[2 + ctemp].text.strip():
                        cho_[2 + ctemp].click()

            time.sleep(3)
            
        driver.get(ClassPage)
        time.sleep(2)


def easy(Repeat):
    for cction in range(Repeat):
        driver.find_element(By.XPATH,"//*[@class=\'cc-table fill-parent m-t\']/div[@class=\'font-0\']/div[1]").click()
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT,"암기 학습 시작").click()
        time.sleep(3)
        total_count_recall = int(driver.find_element(By.XPATH,"//*[@class='total_count']").text.strip())
        known_count_recall = int(driver.find_elements(By.XPATH,"//*[@class='known_count']")[1].text.strip())
        for i in range(total_count_recall - known_count_recall):
            driver.find_element(By.PARTIAL_LINK_TEXT,"의미 보기").click()
            time.sleep(1)
            driver.find_element(By.PARTIAL_LINK_TEXT,"이제 알아요").click()
            time.sleep(3)

        driver.get(ClassPage)
        time.sleep(2)
            
easy(MemorizationCount)
recall(ReCallCount)
spell(SpellCount)
driver.quit()
