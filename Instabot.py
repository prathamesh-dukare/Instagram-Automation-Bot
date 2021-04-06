import selenium
from selenium import webdriver
from  Credentials import mypass,myuser
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

def instalogin():
    print('Validating Credentials \n ')
    driver.get("https://www.instagram.com/")
    time.sleep(3)
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(myuser,Keys.TAB,mypass,Keys.ENTER)
    #driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(mypass,Keys.ENTER)
    time.sleep(3)
    #driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    driver.find_element_by_class_name('yWX7d').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    #driver.find_element_by_class_name('HoLwm').click()
    time.sleep(2)
    print('Access Granted ...\n ')

def scroll():
    print('Your Feed is scolling automatically...\n ')
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    count=0
    while True:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        count+=1
        time.sleep(1)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        if (screen_height) * i > scroll_height or count>10:
                break
    time.sleep(2)

def dm():
    print('sending messesge to @shotbyduke_...')
    driver.find_element_by_class_name('xWeGp').click()
    time.sleep(5)
    driver.find_element_by_class_name('wpO6b').click()
    time.sleep(3)
    driver.find_element_by_name('queryBox').send_keys('shotbyduke_')
    time.sleep(4)
    driver.find_element_by_name('queryBox').send_keys(Keys.TAB,Keys.ENTER)
    time.sleep(2.5)
    driver.find_element_by_class_name('rIacr').click()
    time.sleep(3.2)
    driver.find_element_by_tag_name('textarea').send_keys('Hello , Loved your Photos',Keys.ENTER)
    time.sleep(0.6)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/button[2]').click()
    time.sleep(2.5)
    driver.find_element_by_class_name('Fifk5').click()
    print('Messeges sent Succcesfully ! \n ')

def hashtag():
    print('Searching for desired hashtags - #shotbyduke_\n ')
    list=['Kadakk Post','Beautiful Picture','Best Click','Rada Post Bhava']
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('#shotbyduke_')
    time.sleep(2.4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.TAB,Keys.TAB,Keys.ENTER)
    time.sleep(2.1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/button').click()
    time.sleep(2.5)
    #first post
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]').click()
    time.sleep(2.5)
    print('Looping over the posts and automated engagements...')
    for i in list:
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()#like
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
        time.sleep(1.5)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(i,Keys.ENTER)#comment
        time.sleep(2.5)
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[4]/div/div/button/div').click()#save
        time.sleep(1.2)
        driver.find_element_by_class_name('_65Bje  ').click()
        time.sleep(2.5)
        print(i,'commented')

    def savedata():
        print("started downloading Photos and Media.....\n")
        images=driver.find_elements_by_tag_name('img')
        images=[image.get_attribute('src') for image in images]

        path=os.getcwd()
        path=os.path.join(path,'Downloaded')
        os.mkdir(path)
        count=0
        for image in images:
            save_as = os.path.join(path,'photo'+ str(count) + '.jpg')
            wget.download(image, save_as)
            count += 1
        time.sleep(3.5)
    savedata()
    print('Photos are downloaded...!\n Closing your instance....!')
    time.sleep(1)
    driver.close()


if __name__=='__main__':  
    instalogin()
    scroll()
    dm()
    hashtag()

        
