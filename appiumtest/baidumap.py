from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="127.0.0.1:21503"
#可捕获toast
#desired_caps['automationName']='uiautomator2'
desired_caps["app"]=r"C:\Users\Henry\Desktop\python+appium\baiduditu_920.apk"
desired_caps["appPackage"]="com.baidu.BaiduMap"
desired_caps["appActivity"]="com.baidu.baidumaps.WelcomeScreen"
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(8)
##进入一系列操作到搜索页面
WebDriverWait(driver,60).until(lambda x:x.find_element_by_id("com.baidu.BaiduMap:id/ok_btn"))
print("点击同意")
driver.find_element_by_id("com.baidu.BaiduMap:id/ok_btn").click()
WebDriverWait(driver,60).until(lambda x:x.find_element_by_id("com.baidu.BaiduMap:id/btn_enter_map"))
print("点击进入地图")
driver.find_element_by_id("com.baidu.BaiduMap:id/btn_enter_map").click()

WebDriverWait(driver,60).until(lambda x:x.find_element_by_id("com.baidu.BaiduMap:id/guide_close"))
print("关闭弹窗")
driver.find_element_by_id("com.baidu.BaiduMap:id/guide_close").click()


#获取屏幕尺寸
x=driver.get_window_size()["width"]
y=driver.get_window_size()["height"]



def toBiger():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    big_action=MultiAction(driver)

    action1.press(x=x*0.4,y=y*0.4).wait(1000).move_to(x=x*0.2,y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6,y=y*0.6).wait(1000).move_to(x=x*0.8,y=y*0.8).wait(1000).release()
    print("开始放大")
    big_action.add(action1,action2)
    big_action.perform()

def toSmaller():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    big_action=MultiAction(driver)

    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()
    print("开始缩小")
    big_action.add(action1,action2)
    big_action.perform()


for i in range(3):
    toBiger()

for i in range(3):
    toSmaller()