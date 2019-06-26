
from selenium.webdriver.support.wait import WebDriverWait
from  appiumtest.capability import driver
driver.implicitly_wait(5)
#取消
try:
    cancelbtn=driver.find_element_by_id("android:id/button2")
except Exception:
    print("没有取消按钮")
else:
    cancelbtn.click()
print("划过页面")
for i in range(2):
    driver.swipe(620,572,100,572)
print("点击立即体验")
driver.find_element_by_id("com.tal.kaoyan:id/activity_splash_guidfinish").click()
