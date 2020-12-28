# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import unittest
import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


def appium_start(host, post_num):
    p = os.popen(f'lsof -i tcp:{post_num}')
    p0 = p.read()
    if p0.strip() != '':
        p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
        os.popen(f'kill {p1}')  # 结束进程
        print('appium server已结束')

    cmd = f'appium -a 127.0.0.1 -p {post_num} --log xxx.log --local-timezone  & '
    os.system(cmd)
    time.sleep(3)  # 等待启动完成
    print('appium启动成功')



def setUp():
    print("Enter SetUp")
    dc = {}
    dc['app'] = "/Users/tron/Documents/Work/TronTest/TronLink.apk"
    dc['automationName'] = "uiautomator1"
    dc['noReset'] = "true"
    dc['appPackage'] = "com.tronlinkpro.wallet"
    dc['platformVersion'] = "9"
    dc['deviceName'] = "platina"
    dc['platformName'] = "Android"
    dc['unicodeKeyboard'] = "true"
    dc['resetKeyboard'] = "true"
    url = "http://" + ip + ":" + str(port) + "/wd/hub"
    print(url)
    driver = webdriver.Remote(url, dc)
    driver.implicitly_wait(15)
    time.sleep(10)
    os.system("adb shell settings put secure default_input_method io.appium.settings/.UnicodeIME")
    return driver

def tearDown():
    driver.close_app()
    os.system("adb shell settings put secure default_input_method com.baidu.input_mi/.ImeService")
    driver.quit()

def import_Privatekey(privatekey,name):
    driver.find_element_by_id("com.tronlinkpro.wallet:id/iv_wallet_manager").click()
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout").click()
    driver.find_element_by_id("com.tronlinkpro.wallet:id/et_content").send_keys(privatekey)
    driver.find_element_by_id("com.tronlinkpro.wallet:id/bt_next").click()
    shortName = name[len(name)-4:]
    driver.find_element_by_id("com.tronlinkpro.wallet:id/et_name").send_keys(shortName)
    el6 = driver.find_element_by_id("com.tronlinkpro.wallet:id/creat")
    el6.click()
    el7 = driver.find_element_by_id("com.tronlinkpro.wallet:id/et_password")
    el7.send_keys("Test0001")
    driver.hide_keyboard()
    el9 = driver.find_element_by_id("com.tronlinkpro.wallet:id/creat")
    el9.click()
    time.sleep(3)
    el10 = driver.find_element_by_id("com.tronlinkpro.wallet:id/et_password")
    el10.send_keys("Test0001")
    driver.hide_keyboard()
    el11 = driver.find_element_by_id("com.tronlinkpro.wallet:id/creat")
    el11.click()
    time.sleep(8)

def deletetNowWallet():
    el2 = driver.find_element_by_id("com.tronlinkpro.wallet:id/tv_walletname")
    el2.click()
    time.sleep(5)
    selec = 'className("android.widget.TextView").text("删除钱包")'
    el3 = driver.find_element_by_android_uiautomator(selec)
    el3.click()
    el4 = driver.find_element_by_id("com.tronlinkpro.wallet:id/et_password")
    el4.send_keys("Test0001")
    el5 = driver.find_element_by_id("com.tronlinkpro.wallet:id/tv_ok")
    el5.click()
    time.sleep(10)

def importwalletFormDict(walletDict):
    for key,value in walletDict.items():
        import_Privatekey(value,key)

def isElement(self,identifyBy,c):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    time.sleep(1)
    flag=None
    try:
        if identifyBy == "id":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath(c)
        elif identifyBy == "class":
            self.driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            self.driver.find_element_by_link_text(c)
        elif identifyBy == "partial link text":
            self.driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            self.driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            self.driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            self.driver.find_element_by_css_selector(c)
        flag = True
    except NoSuchElementException as e:
        flag = False
    finally:
        return flag


def deleteAllWallet():
    # driver.find_element_by_id("com.tronlinkpro.wallet:id/tv_import")
    while isElement("id","com.tronlinkpro.wallet:id/tv_walletname"):
        try:
            deletetNowWallet()
        except IOError:
            print("over delete")
        else:
            print("delete success")


if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 4723
    appium_start(ip,port)
    driver = setUp()
    walletDict = {"TEDguVMSsFw3HSizQXFK1BsrGWeuRMNN7t":"3d16a04b7d01712667b40cb7f4c9bbe73ca111ac14a13a4f8e12a7f557d2c89c",
                  "TDkSQtBhZx7Ua8qvenM4zuH52u2BsYTwzc":"978c0a1832fd091c60dff74f9bca04dca39ec118480880f2a7ed2c90b5908640",
                  "TDVveQuK5NMVoA1zzAqMmQuxNjxQr4xZ3z":"7f1769c7882c3e9e488251005422f6a5fb373630e84589cff4d95e8b3f8a308f",
                  "TUVh41otFahZVe8o8FSp8ARBWZ9Uxeg9f1":"c74fb4d8101572041c6fab30e1602ba1ec8247e1ead19641fb985b3ed3a8261e",
                  "TZ7U1WVBRLZ2umjizxqz3XfearEHhXKX7h":"25f98ac22c9fd02aa8a2ef354db0aa13ebc2a6c31377ea7e2b342f0d3898af0d"
                  }
    importwalletFormDict(walletDict)
    # deletetNowWallet()
    # deleteAllWallet()
    tearDown()


# Press the green button in the gutter to run the script.

#
#     import_Privatekey(privatekey)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
