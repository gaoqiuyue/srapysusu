from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium_advance.yaml.capability_yaml import driver
import logging.config
import logging
#log配置中读取
CON_LOG="../appium_advance/log/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
# #自定义log配置
# logging.basicConfig(level=logging.INFO,filename="../appium_advance/log/suj.log",
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
logging.info("等待页面加载完成")
driver.implicitly_wait(8)
logging.info("划过页面")
for i in range(2):
    sleep(2)
    driver.swipe(620,572,100,572,1000)
WebDriverWait(driver,8).until(lambda x:x.find_element_by_id("com.mymoney:id/begin_btn"))
logging.info("点击开始随手记")
driver.find_element_by_id("com.mymoney:id/begin_btn").click()

WebDriverWait(driver,60).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text("设置")'))
logging.info("点击设置")
driver.find_element_by_android_uiautomator('new UiSelector().text("设置")').click()

logging.info("点击高级设置")
driver.find_element_by_android_uiautomator('new UiSelector().text("高级功能")').click()

WebDriverWait(driver,8).until(lambda x:x.find_element_by_android_uiautomator('new UiSelector().text("密码保护")'))
logging.info("点击密码保护")
driver.find_element_by_android_uiautomator('new UiSelector().text("密码保护")').click()

WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.mymoney:id/ll_gesture_psd"))
logging.info("点击手势密码")
driver.find_element_by_id("com.mymoney:id/ll_gesture_psd").click()

logging.info("开始绘制手势密码")
#touchaction是偏移量，不是每个点的坐标
for i in range(2):
    logging.info("第%s次绘制开始"%(i+1))
    TouchAction(driver).press(x=480,y=267).wait(2000)\
    .move_to(x=480,y=400).wait(1000)\
    .move_to(x=480, y=560).wait(100)\
    .move_to(x=340, y=560).wait(100).release().perform()
    logging.info("第%s次绘制结束"%(i+1))