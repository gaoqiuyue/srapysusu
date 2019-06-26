from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="127.0.0.1:21503"
#可捕获toast
desired_caps['automationName']='uiautomator2'
desired_caps["app"]=r"D:\iosmac\dr.fone3.2.0.apk"
desired_caps["appPackage"]="com.wondershare.drfone"
desired_caps["appActivity"]="com.wondershare.drfone.ui.activity.WelcomeActivity"

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

driver.implicitly_wait(5)
print("点击backup按钮")
driver.find_element_by_id("com.wondershare.drfone:id/btnBackup").click()

WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.wondershare.drfone:id/btnRecoverData"))
print("点击next按钮")
driver.find_element_by_id("com.wondershare.drfone:id/btnRecoverData").click()

print("等待H5页面加载")
WebDriverWait(driver,20).until(lambda x:x.find_element_by_class_name("android.webkit.WebView"))
contexts=driver.contexts
print(contexts)

print("切换到H5页面")
driver.switch_to.context("WEBVIEW_com.wondershare.drfone")
print("输入邮箱")
driver.find_element_by_id('email').send_keys('shuqing@wondershare.cn')
print('click sendBtn')
driver.find_element_by_class_name('btn_send').click()

#切换context 点击返回
driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()
