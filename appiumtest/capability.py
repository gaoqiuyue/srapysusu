from appium import webdriver
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="127.0.0.1:21503"
#可捕获toast
desired_caps['automationName']='uiautomator2'
desired_caps["app"]=r"D:\iosmac\kaoyan3.1.0.apk"
desired_caps["appPackage"]="com.tal.kaoyan"
desired_caps["appActivity"]="com.tal.kaoyan.ui.activity.SplashActivity"
desired_caps["noReset"]="True"
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)