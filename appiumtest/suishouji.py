from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="127.0.0.1:21503"
#可捕获toast
#desired_caps['automationName']='uiautomator2'
desired_caps["app"]=r"C:\Users\top\Downloads\suishouji_12014000.apk"
desired_caps["appPackage"]="com.mymoney"
desired_caps["appActivity"]="com.mymoney.biz.splash.SplashScreenActivity"
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(8)
print("划过页面")
for i in range(2):
    sleep(2)
    driver.swipe(620,572,100,572,1000)
WebDriverWait(driver,8).until(lambda x:x.find_element_by_id("com.mymoney:id/begin_btn"))
print("点击开始随手记")
driver.find_element_by_id("com.mymoney:id/begin_btn").click()

WebDriverWait(driver,60).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text("设置")'))
print("点击设置")
driver.find_element_by_android_uiautomator('new UiSelector().text("设置")').click()

WebDriverWait(driver,8).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text("高级功能")'))
print("点击高级设置")
driver.find_element_by_android_uiautomator('new UiSelector().text("高级功能")').click()

WebDriverWait(driver,8).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text("密码保护")'))
print("点击密码保护")
driver.find_element_by_android_uiautomator('new UiSelector().text("密码保护")').click()

WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.mymoney:id/ll_gesture_psd"))
print("点击手势密码")
driver.find_element_by_id("com.mymoney:id/ll_gesture_psd").click()

print("开始绘制手势密码")
#touchaction是偏移量，不是每个点的坐标
for i in range(2):
    TouchAction(driver).press(x=480,y=228).wait(2000)\
    .move_to(x=0,y=120).wait(1000)\
    .move_to(x=0, y=120).wait(100)\
    .move_to(x=-125, y=0).wait(100).release().perform()